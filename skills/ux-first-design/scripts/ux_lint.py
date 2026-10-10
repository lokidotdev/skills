#!/usr/bin/env python3
"""Heuristic UX / accessibility smell scanner for front-end code.

Usage:
  python3 ux_lint.py PATH [PATH ...] [--strict] [--only rule1,rule2]

Scans .html .jsx .tsx .js .ts .vue .svelte .astro .css .scss .less files
(skipping node_modules, build output and VCS folders) and prints
`file:line  [rule]  message`. Every hit is a *candidate*: open the code and
judge it. Use it before a revamp (baseline) and after (regressions).
Exit code is 0 unless --strict is given and something was found.
"""
import argparse
import os
import re
import sys

EXTS = {".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro",
        ".css", ".scss", ".less"}
STYLE_EXTS = {".css", ".scss", ".less"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "coverage",
             ".turbo", "vendor", ".svelte-kit", ".output", "storybook-static"}

I = re.IGNORECASE
S = re.DOTALL

# (rule id, applies to markup?, applies to styles?, regex, flags, message)
RULES = [
    ("img-alt", True, False,
     r"<img\b(?![^>]*\balt\s*=)[^>]*>", I,
     "Image without alt text (use alt=\"\" if purely decorative)."),
    ("icon-button-label", True, False,
     r"<button\b(?![^>]*\baria-label)(?![^>]*\btitle\s*=)[^>]*>\s*"
     r"(?:<svg\b.*?</svg>|<[A-Z][\w.]*\b[^>]*/>|<i\b[^>]*>\s*</i>|<span\b[^>]*class=[^>]*icon[^>]*>\s*</span>)\s*</button>",
     I | S, "Icon-only button without aria-label/tooltip: unlabeled actions fail recognition and screen readers."),
    ("placeholder-as-label", True, False,
     r"<(?:input|textarea)\b(?=[^>]*\bplaceholder\s*=)(?![^>]*\baria-label)(?![^>]*\baria-labelledby)(?![^>]*\bid\s*=)[^>]*>",
     I, "Input with placeholder but no id/aria-label: is the placeholder acting as the label? Add a visible <label>."),
    ("clickable-non-interactive", True, False,
     r"<(?:div|span|li|td|tr|img)\b(?=[^>]*\bon[Cc]lick\b)(?![^>]*\brole\s*=)[^>]*>",
     0, "Click handler on a non-interactive element: use <button>/<a>, or add role, tabIndex and key handling."),
    ("positive-tabindex", True, False,
     r"tab[iI]ndex\s*=\s*[\"'{]?\s*[1-9]", 0,
     "Positive tabindex breaks natural focus order."),
    ("zoom-disabled", True, False,
     r"user-scalable\s*=\s*(?:no|0)|maximum-scale\s*=\s*1(?:\.0)?\b", I,
     "Viewport blocks pinch-zoom; never disable zoom."),
    ("native-dialog", True, False,
     r"(?:\bwindow\.|(?<![\w.]))(?:alert|confirm|prompt)\s*\(", 0,
     "Native alert/confirm/prompt: use a designed dialog with a specific consequence and verb (or an undo toast)."),
    ("vague-cta", True, False,
     r">\s*(?:Submit|OK|Ok|Click here|Yes|No|Go|Proceed)\s*</(?:button|a)>", 0,
     "Vague button/link label: name the outcome (e.g. 'Publish changes', 'Send to 12 recipients')."),
    ("placeholder-copy", True, False,
     r"lorem ipsum|dolor sit amet|\bTODO:?\s*copy\b|\bxxx+\b", I,
     "Placeholder copy left in UI: ship realistic, varied content."),
    ("outline-removed", True, True,
     r"outline\s*:\s*(?:none|0)\b|\boutline-none\b", I,
     "Focus outline removed: make sure a :focus-visible style replaces it."),
    ("tiny-font", True, True,
     r"font-size\s*:\s*(?:[0-9]|1[01])(?:\.\d+)?px|\btext-\[(?:[0-9]|1[01])px\]", I,
     "Font size under 12px: too small for readable UI text."),
    ("transition-all", True, True,
     r"transition\s*:\s*all\b|\btransition-all\b", I,
     "transition: all animates layout properties too; list specific properties (transform, opacity, colors)."),
]

MOTION_RE = re.compile(r"@keyframes|\banimation\s*:|\banimate-[a-z]|\bmotion\.[a-z]|<motion\.|framer-motion|\bgsap\b", I)
REDUCED_RE = re.compile(r"prefers-reduced-motion|useReducedMotion|motion-reduce|reducedMotion", I)
FOCUS_VISIBLE_RE = re.compile(r"focus-visible|focus:ring|focus:outline|focus-within", I)


def iter_files(paths):
    for root in paths:
        if os.path.isfile(root):
            yield root
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
            for name in filenames:
                if os.path.splitext(name)[1].lower() in EXTS and not name.endswith(".min.js"):
                    yield os.path.join(dirpath, name)


def main():
    ap = argparse.ArgumentParser(description="Heuristic UX/accessibility smell scanner")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--strict", action="store_true", help="exit 1 when anything is found")
    ap.add_argument("--only", help="comma-separated rule ids to run")
    args = ap.parse_args()

    only = set(args.only.split(",")) if args.only else None
    rules = [(rid, mk, st, re.compile(rx, fl), msg) for rid, mk, st, rx, fl, msg in RULES
             if not only or rid in only]

    findings = []
    uses_motion = has_reduced = False
    for path in iter_files(args.paths):
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                text = fh.read()
        except OSError:
            continue
        ext = os.path.splitext(path)[1].lower()
        is_style = ext in STYLE_EXTS
        uses_motion |= bool(MOTION_RE.search(text))
        has_reduced |= bool(REDUCED_RE.search(text))
        for rid, markup, style, rx, msg in rules:
            if (is_style and not style) or (not is_style and not markup):
                continue
            if rid == "outline-removed" and FOCUS_VISIBLE_RE.search(text):
                continue
            for m in rx.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                findings.append((path, line, rid, msg))

    if (not only or "reduced-motion" in only) and uses_motion and not has_reduced:
        findings.append(("(project)", 0, "reduced-motion",
                         "Animations found but no prefers-reduced-motion handling anywhere."))

    findings = sorted(set(findings))  # one report per file/line/rule
    for path, line, rid, msg in findings:
        loc = f"{path}:{line}" if line else path
        print(f"{loc}  [{rid}]  {msg}")

    counts = {}
    for _, _, rid, _ in findings:
        counts[rid] = counts.get(rid, 0) + 1
    print(f"\n{len(findings)} candidate issue(s)" +
          ("".join(f"\n  {rid}: {n}" for rid, n in sorted(counts.items(), key=lambda kv: -kv[1])) if counts else ""))
    sys.exit(1 if args.strict and findings else 0)


if __name__ == "__main__":
    main()
