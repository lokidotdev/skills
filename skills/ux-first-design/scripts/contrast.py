#!/usr/bin/env python3
"""WCAG 2.x contrast checker.

Usage:
  python3 contrast.py FG BG [FG BG ...]
  python3 contrast.py "#6B6B75" "#FFFFFF" "rgba(255,255,255,0.6)" "#131316"

Colors: #rgb, #rrggbb, #rrggbbaa, rgb(r,g,b), rgba(r,g,b,a).
A translucent foreground is composited over its background; a translucent
background is composited over --base (default white).

Thresholds: AA body 4.5, AA large text (>=24px or >=18.66px bold) 3.0,
AAA body 7.0, non-text UI (icons, input borders, focus rings) 3.0.
Exit code 1 if any pair fails AA for body text (use --large to judge as large text).
"""
import argparse
import re
import sys


def parse(color):
    c = color.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{6}|[0-9a-f]{8})", c)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(ch * 2 for ch in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return r, g, b, a
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*(?:,\s*([\d.]+%?)\s*)?\)", c)
    if m:
        r, g, b = (float(m.group(i)) for i in (1, 2, 3))
        a_raw = m.group(4)
        if a_raw is None:
            a = 1.0
        elif a_raw.endswith("%"):
            a = float(a_raw[:-1]) / 100
        else:
            a = float(a_raw)
        return r, g, b, a
    raise ValueError(f"Unrecognized color: {color!r}")


def over(fg, bg):
    """Composite fg (r,g,b,a) over an opaque bg (r,g,b)."""
    r, g, b, a = fg
    return tuple(a * f + (1 - a) * k for f, k in zip((r, g, b), bg))


def luminance(rgb):
    def channel(v):
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg, base):
    bg_rgb = over(bg, base[:3]) if bg[3] < 1 else bg[:3]
    fg_rgb = over(fg, bg_rgb)
    l1, l2 = sorted((luminance(fg_rgb), luminance(bg_rgb)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def main():
    p = argparse.ArgumentParser(description="WCAG contrast checker")
    p.add_argument("colors", nargs="+", help="FG BG pairs")
    p.add_argument("--base", default="#ffffff", help="canvas behind a translucent background")
    p.add_argument("--large", action="store_true", help="judge pass/fail as large text (3:1)")
    args = p.parse_args()
    if len(args.colors) % 2:
        p.error("colors must come in FG BG pairs")

    base = parse(args.base)
    failed = False
    for fg_s, bg_s in zip(args.colors[::2], args.colors[1::2]):
        r = ratio(parse(fg_s), parse(bg_s), base)
        need = 3.0 if args.large else 4.5
        ok = r >= need
        failed |= not ok
        marks = lambda t: "pass" if r >= t else "FAIL"
        print(f"{fg_s:>24} on {bg_s:<24} {r:5.2f}:1  "
              f"AA body {marks(4.5)} · AA large/UI {marks(3.0)} · AAA body {marks(7.0)}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
