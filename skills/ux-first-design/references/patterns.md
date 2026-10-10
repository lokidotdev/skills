# Pattern Library: Screen and Component Anatomy

Each pattern lists its anatomy (what goes where) and the UX rules that make it work. Reach for familiar patterns first. Users already know them.

## Contents
- Shells: desktop app shell · page header · toolbar · three-pane layout · mobile shell
- Data: KPI card · chart card · table · detail side panel · properties list · activity feed
- Work: kanban board · inbox · chat and messaging · comments · calendar and timeline · canvas builder
- Forms: modal · settings page · wizard and stepper · review step · bottom sheet · option cards · segmented control · slider
- Mobile: home · bottom tab bar · FAB and speed dial · player · date strip · tracking timeline · map and list
- Commerce: checkout and payment · plan cards · usage meter

---

## Shells

### Desktop app shell
```
┌───────────────┬────────────────────────────────────────────┐
│ ◉ Workspace ▾ │ Breadcrumb › Page            ⌕   🔔  ? (+) │
│ ⌕ Search   ⌘K │ Title [Status]  ★                          │
│               │ One-line purpose subtitle                  │
│ GROUP LABEL   │ [Tab] [Tab] [Tab]          [Secondary][Pri]│
│ ▸ Item     12 │ ─────────────────────────────────────────  │
│ ▸ Item  ⚠     │ content…                                   │
│ GROUP LABEL   │                                            │
│ ▸ Item        │                                            │
│ ───────────── │                                            │
│ [Usage 96/264 │                                            │
│  Upgrade]     │                                            │
│ ? Help  ⚙     │                                            │
│ (A) Name   ›  │                                            │
└───────────────┴────────────────────────────────────────────┘
```
Sidebar width is 232–264px, collapsible to 56–64px with tooltips. Group labels are small uppercase, optionally mono. See `ux-foundations.md` §2.

### Page header
Breadcrumb → title + status chip + favorite → subtitle → tabs (with counts) → actions, with exactly one primary action on the right. Editors add an autosave state. Detail pages add an ID with a copy button (`ID ab12…ef ⧉`).

### Toolbar
Search (the placeholder names its fields) · filter pills `Label: Value ▾` · `+ Add filter` · sort · group by · view toggle (list/grid) · date range with "compare to" · granularity · Export / Share. Applied filters show as removable chips under it, along with a result count.

### Three-pane (list → detail → inspector)
Left: the collection (selected row tinted, with a left accent). Middle: the object. Right: properties or settings (320–360px), closable. Keyboard: ↑/↓ moves through the list, Esc closes the panel. The URL tracks the selection.

### Mobile shell
- **Header**: back · title · action.
- **Content**: cards and lists with "See all".
- **Tab bar**: ≤5 labeled tabs, or a floating pill bar with the active item expanded, plus a separate primary "+" FAB.
- **Sheets** for tasks.

---

## Data

### KPI card
Icon + label ⓘ · ↗ drill-in · large tabular value + muted unit · delta chip (arrow, %, polarity colour) + "vs [baseline]" · optional sparkline or mini-bars · optional verdict chip · optional composition rows. Full rules are in `data-display.md` §6.

### Chart card
Title (an insight or question) + description · controls (period, compare, group by) · legend · chart · annotations · footer insight or recommendation · expand, share, export.

### Table
See `data-display.md` §8. Essentials: type-icon headers, tabular right-aligned numbers, status chips, explicit empty cells, hover actions, bulk bar, side-panel detail.

### Detail side panel
Header: breadcrumb or parent, title, copy link, open full page, more, ✕. Body: a **properties list**, then description, subtasks, attachments, and comments or activity. The composer is pinned to the bottom.

### Properties list
Each row is an icon + muted label on the left and an editable value on the right (Status chip, Assignee avatar, Due "Today", Priority bar icon, Project, Created by). Empty values are invitations that explain their purpose: "+ Set a deadline or schedule", "+ Organize content with labels", "+ Mark importance level". End with "+ Add property".

### Activity feed
Grouped by day (Today / Yesterday). Each item: actor avatar + a sentence ("Roger changed the assignee to…") with state chips + relative time. Comments sit inline. Long runs collapse to "Show more" or "View 3 more replies".

---

## Work

### Kanban board
- **Column**: status icon (todo ○ / in progress ◐ / done ✓, with colour) + name + count + "+" + "…". Hidden or overflow columns peek at the edge.
- **Card**: title, meta ("Created Aug 9 · Team"), divider, chips (priority signal icon, assignees + "+2", due date or **"Overdue" in red**).
- **Drag state**: the card lifts with a slight tilt (~3°), a shadow and an accent outline. A dashed placeholder holds its slot. Columns highlight as drop targets. Follow `apple-design` §2–3 for 1:1 tracking.
- Keyboard and menu alternative: "Move to ▸ [status]".

### Inbox (notifications or messages)
List (filters with counts, grouped by time, unread dots, "Mark all as read") + preview pane (the full thread in context, a "N new" divider, inline reply, "Open ↗"). Triage: archive, snooze, assign, label, done. Show and teach shortcuts ("press R").

### Chat and messaging
- Day dividers, sender grouping, timestamps on hover.
- Reactions shown as counts. Hover action cluster: react · reply · forward · more.
- Attachment chips (type, size), voice notes (waveform with played vs unplayed, duration), replies quoting the original.
- An unread jump pill. Typing and online presence.
- Composer: a personal placeholder, attach, `@` and `/` commands, a send button that's disabled while empty.

### Comments
"Write a comment… Use @ to mention" · attachments · reactions · threaded replies collapsed ("4 replies from…") · Resolve · Assign to.

### Calendar and timeline
- A **today** marker (filled date or a red now-line), with weekends shaded.
- Events are colour-coded by type, with a legend and conflict flags ("Conflicted" filter).
- Event detail: date, start/end, duration, timezone, recurrence ("Repeats every Monday"), participants (+), join link.
- Day view: a time column with a now-line. Month view: dots or bars for events.
- Gantt and timeline: bars span dates, labels sit inside the bars, dependencies are optional, and the view switcher lists Board / Timeline / Table and so on.

### Canvas builder
See `ai-and-automation.md` §8. A dot grid, typed nodes, labeled edges, "+" insert points, an inspector, a floating toolbar (zoom, fit, undo/redo, Ask AI), and Draft/Publish.

---

## Forms and overlays

### Modal
Title (+ subtitle) · ✕ · content · footer: **secondary on the left** ("Discard changes"), destructive separated (icon with a tooltip, or text in red), **primary on the right**. Width ≤640px for forms. A dimmed scrim. Esc and outside-click close it, unless there's unsaved input (then confirm discarding). Keep context modals two-pane when the context matters: "You're applying to…" on the left, login on the right.

### Settings page
- Tabs with icons (Profile · Security · API · Notifications · Integrations · Billing) and doc links on the right.
- A narrow content column (≤720px).
- Section title + description.
- **Rows**: icon tile + title + muted meta ("Last changed 3 months ago") + ONE right-aligned action (Change / toggle / Download), with status badges where relevant ("2FA · Enabled").
- A danger zone at the bottom, separated ("Delete account").
- Session lists mark "This device" and offer "Sign out of all other sessions".

### Wizard and stepper
A named stepper (✓ done, current, upcoming) · one focused question or section per step · a live preview where it helps · Back + Continue (the CTA names the next step or result) · Skip for non-essential steps · a review step before commit · data survives Back.

### Review step
A summary card per section, each with "Edit" / "Change" and its source ("from your profile"), then totals or consequences, the exact list of who receives what, and a final CTA with the verb and key value.

### Bottom sheet (mobile)
Grabber · title · ✕ · content · a sticky primary CTA. Use it for create, quick edit, pickers, confirmation and celebrations. It dims the background. Swipe down dismisses, unless there's unsaved input.

### Option cards
For ≤5 choices that need explanation: icon + title + one line of consequence + a radio or checkbox in the corner. The selected card gets an accent border and tint. Disabled cards show the reason ("Coming soon").

### Segmented control
2–5 short options of the same kind (Weekly / Monthly / Yearly; 1D 1W 1M 3M 1Y; HD 2K 4K; Light / Dark / System). It shows the current value at a glance and switches in one tap. Use it instead of a dropdown.

### Slider
End labels (min/max meaning), a live value label, steps for discrete scales, a large thumb on touch, and a keyboard-adjustable fallback input when precision matters.

---

## Mobile

### Mobile home
Greeting + one summary line → hero metric or card (balance with a hide toggle, today's goal) → 2–4 primary actions as labeled round buttons → "Continue where you left off" → sections with "See all" → contextual upsell or tip cards that can be dismissed.

### Bottom tab bar
≤5 tabs, icon + label, a clear active state (filled icon + colour or pill). Primary create sits outside the tabs. It stays visible on top-level screens and hides in focused flows.

### FAB and speed dial
A single "+" for the main create action. If there are several create types, it expands into a **labeled** speed dial over a blurred or dimmed background, and the "+" morphs into ✕.

### Player
Big title and artist · scrubber (waveform or bar) with **elapsed and remaining** time · a primary play/pause that's visually dominant · skip ±10/15s · tabs for Lyrics / Up next / Related.

### Date strip
A week row (S M T W T F S) with today highlighted and the selected day filled. Dots mark days with content. Swipe for weeks, and offer a month picker for jumps.

### Tracking timeline
Vertical steps (Packing → Shipped → In transit → Delivery). Each has an icon, title, description ("Package is waiting for the delivery process"), and a timestamp. The current step is emphasized and the ETA is stated. On maps: a route, a live position, and ETAs per stop ("32 mins left", "3 mins away").

### Map and list
A list ↔ map toggle. Pins carry the key value ("$2.1m"). Tapping a pin shows a detail card with the primary actions (View, Compare). Applied filters show as chips. The count and the sort reason are stated.

---

## Commerce

### Checkout and payment
Saved methods masked (Visa •••• 1937) with an add-new option · order summary (items, fees, total) · promo field collapsed · the price on the CTA · security reassurance near the payment fields · a confirmation with a receipt and the next steps.

### Plan cards
See `onboarding-and-growth.md` §7.

### Usage meter
Label + "used / limit" + a bar that warns near the limit + a reset date + an upgrade or contact link. Place it where the consumption happens (the sidebar footer, or the top of the relevant page).
