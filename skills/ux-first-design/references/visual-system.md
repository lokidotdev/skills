# Visual System: the UI Layer

The visual layer exists to make the UX decisions legible. The reference set converges on one calm, modern SaaS look:
- neutral canvases
- white (or near-black) cards
- hairline borders
- one accent colour
- semantic status chips
- tabular figures
- small uppercase labels
- generous space

**If the product already has a design system, use it.** The tokens below are a sensible default and a checklist, not a mandate. All colour pairs below were checked with `scripts/contrast.py`.

## Contents
1. Principles
2. Colour tokens (light and dark)
3. Status colour system
4. Typography
5. Spacing, layout and density
6. Shape and elevation
7. Iconography and imagery
8. Components: visual rules
9. Charts: visual rules
10. Dark mode
11. Brand personality without breaking UX
12. Motion

---

## 1. Principles
1. **Calm by default, loud on purpose.** Most of the screen is neutral, and colour marks only action, selection or status.
2. **One accent colour.** It's used for the primary action, active nav, selection, focus ring and links. Two accents compete.
3. **Hierarchy from size, weight and colour together**, never size alone.
4. **Whitespace before lines, and lines before boxes.** Separate with space first, then hairlines, then cards.
5. **Consistency is the craft.** The same thing looks the same everywhere: chips, deltas, row heights, radii, icon stroke.
6. **Every value is a deliberate choice you can defend.** Use tokens, not one-off hex codes or px values.

---

## 2. Colour tokens

```css
:root {
  /* Neutrals: light */
  --bg:            #F6F6F7;  /* app canvas */
  --surface:       #FFFFFF;  /* cards, panels, table */
  --surface-2:     #FAFAFB;  /* subtle fill: hover rows, inputs on cards */
  --surface-3:     #F1F1F3;  /* chips, segmented track, neutral tint */
  --border:        #E8E8EB;  /* hairlines, card borders (decorative) */
  --border-input:  #8E8E96;  /* input/checkbox boundaries: 3.25:1 on white */
  --text:          #111113;  /* primary text: 18.9:1 */
  --text-2:        #52525B;  /* secondary text: 7.7:1 */
  --text-3:        #6B6B75;  /* meta / placeholder: 5.3:1 (lightest allowed for text) */

  /* One accent */
  --accent:        #4F46E5;  /* buttons, links, active: 6.3:1 on white, white on it 6.3:1 */
  --accent-hover:  #4338CA;
  --accent-tint:   #EEF0FF;  /* selected row, active nav pill */
  --on-accent:     #FFFFFF;

  /* Semantic (text on its own tint passes AA) */
  --success:       #15803D;  --success-tint: #E8F7EE;
  --warning:       #B45309;  --warning-tint: #FFF4E5;
  --danger:        #B91C1C;  --danger-tint:  #FDECEC;   /* text/chips */
  --danger-solid:  #DC2626;                              /* destructive button bg, white text 4.8:1 */
  --info:          #1D4ED8;  --info-tint:    #EAF1FF;
  --neutral:       #52525B;  --neutral-tint: #F1F1F3;

  --focus-ring: 0 0 0 2px var(--surface), 0 0 0 4px var(--accent);
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:           #0B0B0D;
    --surface:      #131316;
    --surface-2:    #1A1A1F;
    --surface-3:    #222228;
    --border:       #26262C;
    --border-input: #6B6B76;  /* 3.5:1 on surface */
    --text:         #F4F4F5;  /* 16.9:1 */
    --text-2:       #A1A1AA;  /* 7.2:1 */
    --text-3:       #8B8B95;  /* 5.5:1 */
    --accent:       #8B8FFF;  /* text/links on dark: 6.6:1 */
    --accent-solid: #5B5FEF;  /* button bg, white text 4.85:1 */
    --accent-tint:  #1E1F3A;
    --success: #4ADE80; --success-tint: #132A1C;
    --warning: #FBBF24; --warning-tint: #2A2210;
    --danger:  #F87171; --danger-tint:  #2C1517;
    --info:    #60A5FA; --info-tint:    #121F33;
  }
}
```

Rules:
- Text never goes lighter than `--text-3`. Lighter greys (such as #9A9AA3, which is 2.8:1) are for disabled decoration only, never for content.
- Input boundaries need 3:1. Hairline card borders don't, because they're decorative.
- **Swap the accent hue for the brand**, then re-run `contrast.py` for the accent on surface and white on the accent.
- Never put brand colour on large backgrounds behind dense text. Brand moments belong on heroes, auth side panels and empty states.

---

## 3. Status colour system
| Meaning | Colour | Typical words |
|---|---|---|
| Success, positive, done, verified, active, good delta | Green | Completed · Success · Verified · Active · Enabled · Optimal |
| Warning, pending, attention, in review, medium | Amber/orange | Pending · In review · Awaiting · Needs improvement · Medium |
| Error, destructive, failed, overdue, critical, bad delta | Red | Failed · Overdue · Rejected · Critical · Vulnerable |
| Info, in progress, new, selected | Blue (or the accent) | In progress · Processing · New · Running |
| Neutral, draft, inactive, unknown | Grey | Draft · Paused · Archived · Not set · Idle |

**Chip anatomy**: a tint background + text in the strong shade of the same hue + a leading dot or icon + a word (radius 6px or full, padding 2×8px, 12px/500).

**Never rely on colour alone.** Always add a word, icon or shape. Keep the mapping identical across the whole product. The same "Pending" is amber everywhere.

---

## 4. Typography

| Role | Size / line-height | Weight | Notes |
|---|---|---|---|
| Display (marketing, onboarding hero) | 32–48 / 1.1 | 600 | −0.02em tracking |
| Page title | 20–24 / 1.25 | 600 | −0.01em |
| Section title / card title | 15–16 / 1.4 | 600 | |
| Body (desktop SaaS) | 13–14 / 1.5 | 400 | |
| Body (mobile) | 15–17 / 1.45 | 400 | respect Dynamic Type / user font size |
| Meta, helper, timestamps | 12–13 / 1.4 | 400 | `--text-3` |
| Micro label (section/table headers, sidebar groups) | 11–12 / 1.3 | 500 | UPPERCASE, +0.04–0.06em, often mono |
| KPI number | 24–32 / 1.1 | 600 | tabular, −0.02em |
| Hero number (mobile balance) | 32–44 / 1.05 | 600 | tabular; de-emphasize the cents and currency |

- **Families.** Use one sans for the UI (Inter, Geist, SF / system-ui) and one mono for numbers, IDs, code and micro labels (JetBrains Mono, Geist Mono, SF Mono). A serif or display face is fine for *brand personality* in headings or a whole warm product, but never for dense data.
- `font-variant-numeric: tabular-nums;` goes on every number in tables, KPIs, timers and prices.
- Tracking is size-specific: tighten large type and leave body at 0. See `apple-design` §15.
- Line length for prose is 60–80 characters. Settings descriptions stay at 1–2 lines.

---

## 5. Spacing, layout and density
- **4px grid**: 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64.
- Card padding is 16–24px. Gaps between cards are 12–16px (dense) or 16–24px (airy). Sections are 32–48px apart.
- Layout widths:
  - sidebar: 232–264px
  - inspector/detail panel: 320–400px
  - settings column: ≤720px
  - forms: ≤560px
  - reading content: ≤720px
- Controls are 32–36px high on desktop (28px compact, 40px large) and 44–52px on mobile.
- Table rows are 36–44px in standard density and 32px compact. Mobile list rows are 56–72px.
- Align everything to columns. Numbers align right and labels left. Check vertical rhythm between cards.

---

## 6. Shape and elevation
- Radius scale:
  - chips: 6px or full
  - inputs and buttons: 8–10px
  - cards: 12–16px
  - modals and sheets: 16–20px
  - mobile cards: 16–24px

  Nested radius = outer radius − padding.
- Elevation is mostly **borders, not shadows**. Cards get a 1px `--border` plus at most `0 1px 2px rgba(16,16,20,.04)`.
- Floating layers (menus, popovers, toasts, dragged cards, modals) get a real shadow: `0 8px 24px rgba(16,16,20,.08), 0 2px 6px rgba(16,16,20,.04)`. The higher the layer, the bigger the shadow.
- Use a scrim to focus attention on modal tasks: `rgba(10,10,12,.4)`, optionally with a slight blur. Non-blocking panels don't get a scrim (see `apple-design` §12).

---

## 7. Iconography and imagery
- Use one outline icon set (Lucide, Phosphor or similar) at 16px (dense) or 20px (default), with a consistent 1.5px stroke. Filled versions are only for active or selected states.
- Use leading icons on nav items, property labels, KPI labels, tabs and option cards. They aid scanning, but the text label stays.
- **Icon-only buttons** are fine for universally known actions (close, more, search, settings), and they still need a tooltip and an `aria-label`. Ambiguous icons (duplicate? folder? revoke?) need text.
- Avatars and logos are recognition aids: show people and companies with their image or initials next to the name. Use colour-coded initials with consistent colours per entity.
- Use illustrations for empty states, onboarding and celebrations only, in one consistent style.
- Don't use emoji as UI icons in professional tools. In user-made content (collection names, tags) they're fine.

---

## 8. Components: visual rules
- **Buttons**: primary (accent fill) · secondary (surface + border) · tertiary/ghost (text only) · destructive (danger outline or text; danger-solid fill only inside the confirmation itself). One primary per view. A loading state keeps the button's width and swaps the label for a spinner + "Saving…".
- **Inputs**: 1px `--border-input`, radius 8–10px, label above at 13px/500, helper below at 12px `--text-3`. The focus ring is accent. Errors get a danger border + message + icon.
- **Segmented control**: a `--surface-3` track, with the selected item raised as a white pill with a subtle shadow.
- **Tabs**: text + optional icon + count. The active tab gets a 2px accent underline or a filled pill. Inactive tabs use `--text-2`.
- **Nav item (active)**: an `--accent-tint` pill or a white raised pill on a grey sidebar, or a left 2px accent bar, plus label weight 500→600.
- **Selected row/card**: an `--accent-tint` background and/or an accent border. Never only a checkbox.
- **Badges/counts**: small pill; red only for things that need action (unread mentions, errors), neutral grey for plain counts.
- **Tooltips**: dark surface, 12px, ≤1 line, 300–500ms delay, never holding essential info.
- **Toasts**: bottom-left (desktop) or top (mobile), icon + message + action (Undo), auto-dismiss after 4–6s, paused on hover.
- **Skeletons**: match the final layout's shapes, use a subtle shimmer (none under reduced motion), and show for at least 300ms to avoid flicker.

---

## 9. Charts: visual rules
- Background gridlines in `--border`, with ≤5–6 ticks and abbreviated labels.
- Related series use tints of one hue. Unrelated series use a small categorical palette (≤6) with **consistent colour per series across the product**.
- Highlight what matters: the current or selected bar in full strength, the rest in tint. Use hatching or stripes for projected, incomplete or "previous" data, and a dashed line for baselines and averages.
- Polarity colours (green/red) are only for good/bad deltas, never as plain series colours. A category isn't "bad".
- Tooltips use a dark or white floating card with the date, series swatches + values, and the difference.
- Use the `dataviz` skill (if available) for palette validation and accessible chart styling.

---

## 10. Dark mode
- Base on near-black (#0B0B0D), not pure #000. Raise surfaces with lighter greys rather than shadows.
- Lower saturation and raise lightness for accents and status hues (see the tokens). Text on tints still has to pass 4.5:1.
- Borders matter more in dark mode: use `--border` (#26262C) hairlines to separate surfaces.
- Avoid large saturated fills. Use glows sparingly, and only on the single primary action ("+ Add data").
- Ease the light↔dark switch, and respect the system setting with a manual override (System / Light / Dark, each with a description).
- Re-check every contrast pair. Dark modes in the reference set failed on dark-blue titles over dark cards.

---

## 11. Brand personality without breaking UX
Personality comes from type choice (a serif for a warm product, a mono for a technical one), illustration style, a signature accent, mascot moments, and empty and celebration states. It must **not** come from:
- unreadable contrast
- non-standard controls
- hidden labels
- novel navigation
- surprise placements of primary actions

Rule of thumb: be expressive where the user is *not* working (auth side panels, onboarding, empty states, celebrations, marketing) and quiet where they are (tables, forms, settings, editors).

---

## 12. Motion
Motion explains change (where something came from and where it went). It never decorates. Follow the `apple-design` skill:
- feedback on press (≤100ms)
- critically damped springs by default, with bounce only after a flick
- enter and exit along the same path
- everything interruptible
- `prefers-reduced-motion` swaps to cross-fades

Typical durations, if not using springs:
- 120–180ms for hover/press/colour
- 200–280ms for small moves and popovers
- 300–400ms for sheets and panels

Animate only `transform` and `opacity`.
