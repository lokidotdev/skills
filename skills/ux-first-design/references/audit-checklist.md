# Audit Checklist and Revamp Method

Use this to review existing UI, to plan a revamp, and as the final self-check on your own work. UX sections come first because UX problems matter more.

## Contents
1. How to run an audit
2. Severity scale
3. Checklist (UX first, then UI)
4. Anti-pattern catalog
5. Audit report format
6. Revamp plan format

---

## 1. How to run an audit
1. **Collect context**: who uses the product, their top 3–5 tasks, the platform, and any known complaints or metrics. If you don't know, infer it and state your assumptions.
2. **Walk the top tasks twice**:
   - once as a *first-time user* (no product knowledge; read only what's on screen)
   - once as a *daily expert* (speed, shortcuts, bulk work, density)
3. **Force the states**: empty, loading (throttle the network), error (break the request), long content, no permission, small viewport, keyboard only, 200% zoom, dark mode, reduced motion.
4. **Scan the code** if available: `python3 scripts/ux_lint.py <src>`. Check key colour pairs with `scripts/contrast.py`.
5. **Score** each checklist area (0 = broken, 1 = weak, 2 = solid) and log findings with a severity.
6. **Prioritize** by severity × frequency of the affected task. Group related findings into themes ("numbers lack context", "unsafe destructive actions").

---

## 2. Severity scale
| Level | Meaning | Examples |
|---|---|---|
| **P0 Blocker** | Users can't complete a core task, lose data or money, or are harmed or misled | No way to undo or recover a destructive action; payment without a review step; an inaccessible primary flow; misleading delta colours on financial data |
| **P1 Major** | Significant confusion, error-prone flows, broken trust | Placeholder-only labels; unlabeled icon actions on key paths; missing error states; no feedback on save; hidden pricing terms |
| **P2 Minor** | Friction or inconsistency with a workaround | Dropdown for 3 options; inconsistent chip colours; missing counts; vague button labels; a description on every card or section that buries the ones that matter; a cramped layout with no spacing rhythm |
| **P3 Polish** | Craft and delight | Spacing rhythm, alignment, micro-interactions, typography tuning |

---

## 3. Checklist

### A. Job and flow
- [ ] The primary job of each screen is clear within 5 seconds.
- [ ] Top tasks take the fewest steps and are reachable in ≤2 clicks or taps from where the user starts.
- [ ] Create actions live where the list or object is.
- [ ] Flows have no dead ends. Every step has a next action and a way back.
- [ ] Work in progress is resumable ("Continue where you left off", drafts).

### B. Wayfinding and IA
- [ ] A specific title on each page, with a subtitle only where the title doesn't carry the scope or effect. Breadcrumbs from depth 2.
- [ ] Clear active nav state. Nav is grouped by job and labels are specific.
- [ ] Global scope (workspace, environment, date range) is visible and restated.
- [ ] Steppers name steps and show progress. "x of y" positions are given.
- [ ] Back preserves filters, tab and scroll. Deep links work.
- [ ] Mobile: labeled tabs (≤5), primary action in the thumb zone.

### C. Hierarchy and primary action
- [ ] One primary action per view, with a verb + object label.
- [ ] The most important information is the most prominent, and secondary info is muted but readable.
- [ ] Related items are grouped. Controls sit next to what they affect.
- [ ] Destructive actions are separated, styled, and placed last.

### D. States
- [ ] First-use empty: says what goes here + one CTA (+ one line on how it works for a new concept).
- [ ] No results: echoes the query, offers clear or adjust.
- [ ] Loading: skeleton or labeled progress, no layout shift, nothing blocking the whole UI unnecessarily.
- [ ] Errors: what, why, fix; input preserved; placed next to the cause.
- [ ] Partial or missing data is labeled. Disabled and locked items explain why.
- [ ] Lifecycle chips (draft, saved, published, running, paused, failed) are present where relevant.
- [ ] Limits, trials and stale data are communicated with numbers and dates.
- [ ] Overflow handled: long names, many items, 99+, huge numbers.

### E. Feedback
- [ ] Press feedback is instant. Anything over 1s shows progress.
- [ ] Save state is visible (autosave indicator, or dirty state + guard).
- [ ] Success messages are specific and say what's next.
- [ ] New content doesn't shift what the user is reading or clicking.

### F. Consequences and trust
- [ ] Money, sending, publishing and sharing flows have a review step showing amount, fee, ETA, recipients and visibility.
- [ ] Undo, trash or version history exists for reversible destructive actions.
- [ ] Confirmations are reserved for irreversible actions, name the consequence, and use specific verbs.
- [ ] Safe defaults (test mode, drafts, stop conditions) are in place.
- [ ] Reassurance appears at anxiety points. Pricing and renewal terms are visible before commit.
- [ ] Sensitive data is masked, with a reveal toggle. Permissions are requested in context, with a reason.

### G. Forms and input
- [ ] Visible labels. Placeholders are examples only. Required or optional is marked.
- [ ] Helper text is specific to each field. No duplicated labels.
- [ ] Inline validation on blur, with fix-oriented messages.
- [ ] The right control for the job (segmented or cards for ≤5 options, toggles for instant settings).
- [ ] Smart defaults, presets, constraints in-field, counters near limits.
- [ ] Honest escape options. Each question says why it's asked.

### H. Data and numbers
- [ ] Every KPI has a baseline + delta. **Delta colour follows metric polarity.**
- [ ] Quotas show used/limit. Verdicts include thresholds. Freshness is shown.
- [ ] Charts have clear titles, legends and tooltips. Subtitles, annotations and recommendations appear only where something needs explaining.
- [ ] KPI cards carry label, value, delta and baseline, with no description sentences. Freshness is shown once per source.
- [ ] Tables: right-aligned tabular numbers, explicit empty cells, status chips, bulk actions, side detail.
- [ ] Filters are readable (`Label: value`) and applied filters are visible and clearable.
- [ ] No placeholder or duplicate data in demos or screenshots.

### I. AI and automation (if present)
- [ ] The AI shows its plan, progress, sources and what it changed.
- [ ] Suggestions explain *why*. Uncertainty is flagged.
- [ ] Human approval comes before external effects. Draft → publish. Overrides are possible.
- [ ] Costs, credits and model are visible. A disclaimer is near the input.
- [ ] Builder nodes are readable as sentences. Incomplete nodes say what's missing.

### J. Content
- [ ] Zero typos. Proofread every string, including error and empty states.
- [ ] One term per concept. Copy matches the layout.
- [ ] Buttons name outcomes. No "Submit", "OK" or "Click here".
- [ ] Jargon is defined (ⓘ or inline).
- [ ] No description restates its title, repeats something on screen, or narrates the UI.
- [ ] No sentence where a label, chip, count, verb or ⓘ would do. Each remaining line answers "what would the user get wrong without it?"
- [ ] Nothing is under-explained either: irreversible actions, costs, hidden consequences and sensitive asks each have their one line.

### K. Accessibility
- [ ] Contrast: text ≥4.5:1, large text and UI ≥3:1 (checked with `contrast.py`).
- [ ] Fully keyboard operable, visible focus, logical order, Esc closes overlays.
- [ ] Labels on all inputs. `aria-label` on icon buttons. Alt text on images.
- [ ] Colour is never the only signal.
- [ ] Touch targets ≥44pt. Desktop targets ≥24px.
- [ ] Reduced motion and zoom (200%) supported. Async changes announced.

### L. Visual consistency
- [ ] One accent colour. A semantic status palette used consistently.
- [ ] Spacing on a 4px grid with a visible rhythm: gaps between groups are at least twice the gaps inside them, and sections are separated by space.
- [ ] Comfortable density by default. Compact only where people scan many rows.
- [ ] Forms, settings, review steps, onboarding and empty states sit in a narrow column with room around them.
- [ ] Sibling cards share one anatomy. Labels, values and actions line up across a row, and no card is taller only because its description wrapped.
- [ ] At most three text levels per card or row.
- [ ] Consistent radii, row heights, icon set and stroke.
- [ ] Typographic scale applied consistently. Tabular numbers.
- [ ] Elevation used only for floating layers. Hairlines over heavy borders.
- [ ] Dark mode checked separately.

---

## 4. Anti-pattern catalog
| Anti-pattern | Why it hurts | Fix |
|---|---|---|
| Placeholder as the only label | The label vanishes on typing; it's low contrast and inaccessible | Label above; placeholder shows an example |
| Icon-only actions (tab bar, footer, revoke ✕) | Users can't guess; screen readers can't announce | Text labels, or tooltip + `aria-label`; keep text on primary nav |
| Delta coloured by direction | Says "good" when it's bad | Polarity per metric (`data-display.md` §2) |
| Duplicate field labels | Users can't tell the fields apart | Unique, specific labels |
| Copy contradicting layout | Erodes trust; confuses | Rewrite to match what follows |
| Placeholder or duplicate data | Looks broken; hides real layout issues | Realistic, varied data in every state |
| Typos | Undoes a premium impression instantly | Proofreading pass |
| Low-contrast titles on dark cards | Unreadable | Check contrast; use `--text` tokens |
| Mixed units in one list | Ranking is meaningless | One unit per list or column |
| Blank area with no guidance | Users stall | Empty state with a headline + CTA |
| Subtitle restating the title ("Profile: profile data") | Adds reading, says nothing, and trains users to skip the subtitles that matter | Delete it, or state the scope, effect or cost |
| A description on every card, chart or section | Noise, ragged card heights, values that don't line up | Label + value + meta; ⓘ for definitions; if needed, give every sibling one, clamped to the same length |
| The same explanation twice | Clutter and doubt ("is this different?") | Say it once, nearest the decision |
| Cramped layout (dense everywhere, no section spacing) | Nothing reads as a group, the page feels heavy | Spacing rhythm (group gap ≥ 2× item gap), comfortable density, narrow focused columns |
| Generic CTAs and "Are you sure?" | Users click through without reading | Outcome verbs, specific consequences, undo |
| Confirm dialog for reversible actions | Friction plus habituation | Undo toast |
| Dropdown for 2–5 options | Hides choices; costs 2 taps | Segmented control or option cards |
| Silent disabled button | Users don't know what's missing | Explain the reason, or keep it enabled and validate |
| Hiding pricing or renewal terms | Breaks trust; chargebacks | Terms under the CTA |
| Auto-inserting new content | Users lose their place and misclick | "N new items" pill |
| Modal over modal | Context is lost | Inline expansion, a side panel, or a sheet with steps |
| Novel navigation for its own sake | Muscle memory breaks | Familiar patterns; test anything novel |

---

## 5. Audit report format
```
# UX Audit: <product/area>
Context & assumptions: <users, top tasks, platform, what was tested>

## Summary
<3–5 sentences: overall state, the 3 most important themes, the biggest win available>

## Scorecard
| Area | Score (0–2) | Note |
| Job & flow | | |
| Wayfinding | | |
| States | | |
| Consequences & trust | | |
| Forms | | |
| Data display | | |
| Content | | |
| Accessibility | | |
| Visual consistency | | |

## Findings (ranked)
| # | Sev | Where | Problem | User impact | Fix |
|---|-----|-------|---------|-------------|-----|
| 1 | P0 | Checkout › Pay | No review step before charging | Unexpected charges, refunds | Add review: amount, fee, method, total; price on button |

## Quick wins (≤1 day each)
- ...

## Bigger bets
- ...
```

---

## 6. Revamp plan format
1. **Keep**: what works and what users rely on (names, URLs, shortcuts, positions).
2. **Fix**: the P0/P1 findings, grouped by theme.
3. **Restructure**: IA and flow changes, with a before → after map of navigation and screens.
4. **Redesign**: states, copy, then visuals. List the components to build or replace.
5. **Transition**: "What's new" hints, a legacy escape hatch, migration of saved views and filters, release notes, and a feedback channel.
6. **Measure**: the success signal for each job (task completion, time to first value, error rate, support tickets, retention), with a baseline before and a comparison after.
