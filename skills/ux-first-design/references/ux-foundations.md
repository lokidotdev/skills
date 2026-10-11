# UX Foundations

This file holds the detail behind the twelve rules in SKILL.md. Skim the headings and read the sections your task touches. Examples in quotes come from the reference set (see `reference-set.md`).

## Contents
1. Jobs, tasks and objects
2. Navigation and information architecture
3. Wayfinding
4. Hierarchy and attention
5. States: the state matrix
6. Feedback and system status
7. Consequences, safety and trust
8. Forms and input
9. Search, filters, sort and views
10. Collaboration, notifications and communication
11. Accessibility baseline
12. Mobile and touch ergonomics
13. Responsive adaptation

---

## 1. Jobs, tasks and objects

**Job story.** `When <situation>, I want to <motivation>, so I can <outcome>.` Write one for every primary flow. The situation shapes the screen as much as the goal does:
- *When I open the app in the morning* → greeting, plus a summary sentence, plus what's due today ("Wednesday 7 October · 2 tasks due today").
- *When a deal starts slipping* → a saved risk view ("Slipping deals ⚠") with the reason and a fix action.
- *When I come back to unfinished work* → "Currently working on" or "Continue listening", with relative time ("Last edited 12 minutes ago").

**Rank the tasks.** List every task the screen supports and score each by frequency (daily / weekly / rare) × importance (blocking / valuable / nice). The top 1–3 get the prime position and one-click access. Everything else goes one level deeper: an overflow menu, a tab, "More", or settings.

**Object model before layout.** Fill this table before you draw anything:

| Object (noun) | Key attributes | Relationships | Actions (verbs) |
|---|---|---|---|
| Deal | value, stage, owner, win %, last activity | belongs to Company, has Contacts | create, move stage, assign, mark lost |

- A collection of objects becomes a nav item or list page. A single object becomes a detail page or side panel. Actions live on the object (row hover, detail header, context menu). Bulk actions live on the selection.
- The attribute type decides how it's displayed:
  - dates → relative time, with the absolute date on hover
  - money → right-aligned tabular figures
  - status → chip
  - person → avatar + name
  - URL → link with an icon
  - strength or score → icon + colour + word ("⚡ Very strong")

**Mapping.** Put a control next to the thing it changes. Put create actions where the list is: "+ New variable" inside the group, "+" on each kanban column, "+ Add a subtask" under the subtasks. A setting that affects one object belongs on that object, not in global settings.

---

## 2. Navigation and information architecture

### Desktop app shell (sidebar, top to bottom)
1. **Workspace or account switcher** (logo + name + chevron). It tells people with more than one workspace where they are.
2. **Search / ⌘K**. Show the shortcut in the field.
3. **Primary nav grouped by job**, with small uppercase group labels, for example *Build · Data · Monitor · Workspace*, *Main · Create · Enhance*, or *Money · Workflows · Receivables · Admin*. Use 3–7 items per group.
4. **User-made collections**: favorites, pinned items, saved views, teams and spaces. These are collapsible and may use emoji or colour dots so people can recognise them at a glance.
5. **A utility zone pinned to the bottom**: a usage or upgrade card, Help & support (include a human route such as "Talk to an engineer"), Invite teammates, Settings, and an account card (avatar, name, email, chevron).

Rules:
- Show counts where volume matters ("Inbox 3", "Deals 241") and cap badges at "99+". Use at most 1–2 "New"/"Beta" badges at a time.
- The active item gets a filled or tinted pill, or a left accent bar, plus a heavier label. Colour alone isn't enough.
- Show nested items with an indent guide line. A collapsed (icon-only) sidebar keeps tooltips.
- Name items specifically ("Runs", "Clusters", "Storage"). Avoid umbrella names like "Hub" and "Center".

### Levels
Possible levels are: app rail (spaces, communities, workspaces) → section sidebar → content → detail panel. Core tasks should never sit more than one level of hidden navigation deep.

### Global scope
If one choice filters the whole app (workspace, job position, environment, product, account), make it a selector above the nav or in the header, **and restate it in page headers**: "All positions · Oct 15–22, 2025".

### Tabs vs segmented control vs view switcher
| Control | Use for | Example |
|---|---|---|
| Tabs | Sibling sections of one page or object; show counts | Overview · Applicants 9 · Settings |
| Segmented control | 2–4 modes of the same thing | Edit · Preview · Insights; Build · Activity; Spreadsheet · Dashboard |
| View switcher | The same data in a different shape, with saved views | List · Board · Calendar · Timeline · + Add view |

### Mobile navigation
- A bottom tab bar with **≤5 destinations and text labels**. Icon-only tab bars fail recognition, even when the icons look nice.
- Keep the primary create action out of the tab bar: use a FAB or a "+ Add" pill next to it. Expanding into a labeled speed-dial with a dimmed background is fine.
- Back goes top-left. Contextual actions ("+", "…") go top-right.
- Put search and composers in the thumb zone. A bottom "Jump to or search…" field works well.
- Use sheets for create, edit and confirm. Use full screens for browsing.

### State persistence
Filters, sort, the active tab and scroll position all survive Back. Shareable state goes in the URL. Deep links open the exact object, and in master-detail layouts they also select it.

---

## 3. Wayfinding

Every screen answers: *Where am I? What's here? Where can I go? How do I get out?*

**Page header anatomy.** The parts, in order:
1. Breadcrumb (from depth 2; the current item is last and isn't a link).
2. Title + status chip (Draft / Active / Running) + optional star.
3. An optional **one-line subtitle**, only when the title doesn't carry the scope, cost or effect ("Monitoring status for Framework SOC 2 Type II"). Familiar pages (Inbox, Home, Tasks, Overview with a greeting) need none. Never write one that restates the title.
4. View tabs.
5. Actions: secondary actions first, the single primary action rightmost.
6. On editors, a save indicator ("✓ Saved" / "• Unsaved changes").

**Steppers.**
- Name every step ("Select plan · Create account · Compliance · General setup").
- Mark finished steps ✓, highlight the current one, and mute the upcoming ones.
- On mobile, add a progress bar or "Step 2 of 4".
- Going back must never lose entered data.

**Position in a set**: "1 of 4 installments", "Day 8 of 14", "File 1 of 2", "Showing 4 of 4", "Module 1 · 3 lessons".

**Exits.** Every overlay has ✕ and closes on Esc. Flows offer Back, Cancel, "Skip for now" or "← Back to page". Nothing traps the user. A deliberate trap, such as a blocking payment failure, still needs a way to get help.

---

## 4. Hierarchy and attention

- Decide the **one thing** each screen is for. Make it the largest, highest-contrast element *and* first in reading order (top-left on desktop, top on mobile).
- Build hierarchy from a set: size + weight + colour (+ position). Using size alone flattens the page.
- Mute secondary information, but don't shrink it below readable size (body ≥14px, meta ≥12px).
- Group by proximity, and separate groups with space before reaching for lines. The gap between groups is at least twice the gap inside one. Use cards for independent modules and plain sections for related content. See `visual-system.md` §5 for the spacing rhythm.
- **Every extra line of text competes with the one thing.** Hierarchy comes from what you leave out as much as from size and weight. Keep each unit to three text levels (label, value, meta), and let structure and signals do the explaining (`content-design.md` §2).
- Right-align numbers. Keep actions in the same place on every screen.
- **Signal that more exists.** Let the next carousel card or board column peek past the edge, and keep scrollbars or fades visible.
- Pick one density per surface. Data tools are dense (32–36px rows), while consumer and mobile surfaces are airy (56–72px rows).

---

## 5. States: the state matrix

For every screen and major component, specify each state that can happen.

| State | What the user must get | Example |
|---|---|---|
| **First-use empty** | A headline saying what goes here and **one** primary action. If the concept is new, add one line on how it works. An import, template or sample data shortcut is optional | "No experience added yet · Add experience" · "Speak or type to begin. Your assistant takes it from there." · "Streamline your outreach with workflows" + one line + "Create workflow" for a new feature |
| **No results** | Repeat the query and filters, offer to clear or adjust them, keep the filters visible | "No companies match 'acme' with 3 filters · Clear filters" |
| **Loading** | <300ms: nothing (avoid flashes). 300ms–2s: a skeleton in the final layout or an inline spinner *with a label*. >2s: progress with steps. >10s: run in the background and notify | "Loading outcomes…" · "Wrapped up 2 actions · ran through 5 files" |
| **Partial or missing data** | Name the gap and offer the fix. Never leave a silent blank | "No contact" · "Overnight data missing ›" · Receipt: **Missing** / Attached / N/A |
| **Error** | What happened + why (if known) + how to fix it. Keep the user's input. Retry. Put it next to the cause. System banners carry an action | "Connect your account to sync replies. **Connect**" |
| **Success** | A specific confirmation, what happens next, and one CTA | "Your $750.00 transfer to Chase ••4281 has started. It arrives tomorrow. **Done**" |
| **Disabled** | Why, and how to enable it | "Create new bucket · Coming soon" · Sign in stays disabled until both fields are valid, *and it's obvious which one isn't* |
| **Locked** | Lock icon + the unlock condition | Lesson 🔒 "Complete Module 1 to unlock" · "Available on Pro" |
| **Permission denied** | Who can grant access + "Request access" | |
| **Stale or offline** | Freshness, a refresh action, the refresh interval, and any data-delay disclaimer | "Last sync Sep 8, 09:14:02" · "Updates take up to 1 hour" |
| **Lifecycle** | A visible chip for each stage | Draft · Unsaved · Saving… · Saved · Scheduled · Published · Running · Paused until Jul 20 · Completed · Failed · Archived |
| **Environment** | Unmistakable live vs test | "Test mode" toggle beside the data · "Live trading" / "Demo trading" chip |
| **Limits** | Warn before the limit with numbers, then say what to do at the limit | "96 / 264 credits" · "Daily sending limit: 300 emails. New accounts start low. Contact support to raise it." · "Starter limit reached → Upgrade" |
| **Lapsed or expired** | State it plainly and give a recovery path | "3-day streak lost" · "This invite expires in 7 days" · "Trial ends in 4 days" |
| **Overflow** | Truncate with a tooltip; "+2" for extra chips or avatars; "99+"; paginate or virtualize, with counts | |

Never ship a screen whose only designed state is "full of perfect data". Render each state at least once with realistic content.

---

## 6. Feedback and system status

**Timing thresholds**:
- Under 100ms feels instant, so show the press state immediately (see `apple-design` §1).
- Up to 1s keeps the user in flow, and no spinner is needed.
- From 1 to 10s, show a spinner or progress with a label.
- Over 10s, move the work to the background, show progress, and notify on completion.

**Four kinds of feedback**, each with its own look and copy pattern:
- *Status*: what is happening now.
- *Completion*: it's done.
- *Warning*: before a problem.
- *Error*: after a problem.

**Where to put feedback**, in order of preference:
1. Inline at the cause.
2. Toast (temporary, with Undo).
3. Banner (persistent, page- or system-wide, with an action).
4. Modal, only when you must interrupt.

**Live status signals**: "● Recording…", "● Live", "Last sync 2m ago", "Running · 2 positions · 2 profitable", "Detecting audio issues… Troubleshoot", typing indicators, and progress like "Finalize and deliver · 3/3".

**Saving**:
- Editors autosave and show "✓ Saved" or "Saving…".
- Forms with an explicit Save show "• Unsaved changes" and guard navigation away.
- Autosave + version history ("Versions", "Version 2 · Last saved 1 min ago") beats save buttons for documents.

**New content.** Never push content under the user's cursor. Show a pill instead ("Show 24 new posts", "↓ 1 unread message", "3 new comments" divider) and let them choose.

**Optimistic UI** suits cheap, reversible actions (star, check off, move a card). Roll back on failure with an error toast.

---

## 7. Consequences, safety and trust

### Match the safeguard to the risk

| Risk | Safeguard |
|---|---|
| Trivial and reversible (star, reorder, mark read) | Just do it, optimistically |
| Reversible but tedious to redo (archive, delete to trash, move) | Do it, show a toast with **Undo**, keep a trash ("Recently deleted") |
| Sends or publishes to other people | Preview or test send, plus a review step; show the recipients and how it's sent ("12 recipients, each message sent individually"); a draft → publish model; scheduling with an explicit timezone |
| Moves money | A review screen with amount, fee, ETA, masked method and total; the price on the button ("Renew for $249.90"); a receipt after |
| Irreversible destruction | A confirmation that names the object and the consequence ("This permanently removes the node and its connections. This can't be undone."), a specific verb ("Delete node"), destructive styling. For catastrophic actions, type-to-confirm |
| Ongoing automation | Safe defaults ("Stop if they reply" on), pause and resume, run history, test mode, and a heads-up before consequential runs ("We'll let you know before the next auto-save") |
| High-stakes mobile toggle | Slide to confirm ("Slide to resume") |

### Destructive styling
Red text or a red outline. Keep it physically separate from the primary action: the other end of the footer, or the bottom of a menu after a divider. Never make it the default focus. Never make it look identical to the primary button.

### Privacy
- Mask by default ("•••• 1234") and offer a hide-balance toggle.
- Anonymize modes are a real feature, for example for bias reduction.
- Ask for permissions in context, with the reason.
- Offer honest privacy choices with an explanation of each ("Help improve Lemon: we collect…" vs "Privacy mode").
- State who will see what ("Public: anyone with the link can view").

### Trust signals at decision points
Use one per decision point, placed beside the control it's about. Stacking several on the same decision dilutes all of them.
- A testimonial next to signup.
- A security note next to credential inputs ("Your credentials are encrypted and stored securely. They're used only to…").
- A cost note next to apply and trial buttons ("Free to post, takes about 3 minutes").
- A reversibility note next to preferences ("You can always change this later in Settings").
- Promises about behaviour ("No auto-applying. No AI cover letters. You stay in control." · "We never cold-message your talent or resell applicants.").

---

## 8. Forms and input

### Layout
- Use a single column. Put labels above fields. Fields that belong together can share a row (first/last name, start/end time).
- Break long forms into titled sections. Give a section a one-line description only when it says something the title can't: "Access credentials (optional): leave empty for public buckets" earns its place, while "Select cluster: select the cluster you want to use for your run" doesn't. Collapse optional sections ("Attach storage (optional)", "Advanced options").
- Space the form by its structure: 6–8px from label to input, 16–20px between fields, 32–40px between sections, in a column no wider than 560px.
- Use logical order and smart defaults ("Auto allocate", today's date, the detected language "English, detected").
- For long or high-stakes forms, add steps plus a **review** step. For anything visual, show a **live preview** (a job post preview next to the editor, with projected reach "~2,000 matching").

### Field anatomy
`Label (+ * or "(Optional)")` → input (optional leading icon, prefix or suffix, e.g. `+1 ▾` country code, `.txtcrt.io` suffix) → helper text, only when there's a format, a constraint or a consequence to state → error text, which **replaces** the helper text, in red with an icon → character counter near the limit. Most fields are just a label, an input and an example placeholder.

### Choosing the control
| Situation | Control |
|---|---|
| ≤5 mutually exclusive options | Segmented control, or radio *cards* with a description of each option's consequence ("File: customers download your product directly") |
| Many options | Select with search; group the options; show recent and recommended ones first ("Claude Sonnet · Recommended") |
| Multi-select with few options | Chips or checkbox cards, plus "Select all that apply", plus a count on the CTA ("3 selected") |
| A binary setting that applies immediately | A toggle, with a description of its effect |
| A binary choice that applies on submit | A checkbox |
| A range or intensity | A slider with end labels and a live value label ("Sleeping: little to no physical exertion"), stepped when discrete |
| Dates | Presets (Today, Tomorrow, This week) + a picker; ranges with "compare to"; always show the timezone ("GMT+1 Paris", "UTC+07:00") |
| Amounts | Presets ($100 / $250 / $500, or 25% / 50% / 75% / Max), the currency, the min/max shown inside the field |
| Durations or delays | A stepper ("− Wait 2 days +") or a ruler slider |
| Time | Wheel or dial on mobile, typed input with a format hint on desktop |

### Specific fields
- **Password**: a show/hide toggle; list requirements up front; drop "Re-enter password" when show/hide exists; put "Forgot password?" beside the label.
- **OTP**: auto-advance between boxes, accept paste, say where the code went ("We've sent a 6-digit code to hello@company.com"), and show a resend countdown ("Didn't get the code? Resend in 0:44").
- **Rich text and variables**: insert variables as chips (`{first_name}` → "Customer first name"), offer a `/` command menu, and teach `@` in the placeholder.

### Validation
- Validate a field when the user leaves it, and re-validate on every keystroke after an error.
- Error copy says what's wrong *and* how to fix it.
- Keep what the user typed. On submit failure, focus the first error.
- A disabled submit is acceptable only when the missing piece is obvious. Otherwise keep it enabled and show errors on click.

### Saving model
| Surface | Model |
|---|---|
| Single toggles and preferences | Apply immediately, with an optional "Saved" toast |
| Multi-field settings | An explicit **Save changes** + **Discard**; show the dirty state and guard navigation |
| Documents, canvases, editors | Autosave + "Saved" indicator + version history; a separate **Publish** step if others will see it |

### Say why, and offer an honest way out
Every unusual question says why you're asking ("We'll use this to personalize your TxtCart experience"). Every choice set allows the honest answer: "None of the above", "No preference: mix all models", "No, I don't have a business registration number", "Skip for now".

---

## 9. Search, filters, sort and views

- **Search**: let the placeholder list what's searchable ("Search order, date, ID…"). Scope it to the page, and make ⌘K global. Show recent searches. Highlight matches.
- **Filters as readable pills**: `Sort by: Pipeline value`, `Stage: Any`, `Last activity: 90 days`, `Budget: $850K–$1.2M`. The muted label plus a bold value makes each filter self-describing.
- **Applied filters are always visible** as removable chips, with **Clear all**. Show the result count ("17 investment-ready properties in your selected area").
- **Facets show counts** ("Verified only (12)", "All 63 · Carpool 21 · Bus 42").
- **Explain the logic** when it's non-trivial: "0 active · OR within, AND across groups". Offer include/exclude, and tri-state parent checkboxes for trees.
- **Quick filters plus detailed filters**: common toggles on top, the long tail collapsed below.
- **Save** filters and views ("Saved filter ▾", "Apply saved filters", "Set as default").
- **Sorting** shows its indicator and, when it's not obvious, its reason ("Sorted by yield potential").
- **Views**: list, board, calendar and timeline over the same data, with "+ Add view" and per-user defaults.

---

## 10. Collaboration, notifications and communication

- **Comments**:
  - the placeholder teaches syntax ("Write a comment… Use @ to mention")
  - reactions with counts; reply threads collapsed to "4 replies from Carlos, Maria, Leo…"
  - Resolve, and "Assign to anyone"
  - attachments show their type and size ("PDF · 32 MB")
- **Activity feed** in plain language: actor + verb + object, with state changes as chips ("You changed design status from `In research` to `In design`"), plus relative time.
- **Notification inbox**:
  - filters (All · Mentions · Assigned to me)
  - groups by time (Today · Yesterday · Earlier)
  - each item is actor avatar + sentence + snippet + project chip + time + unread dot
  - "Mark all as read"
  - the selected item opens **in context** (the full thread, a "3 new comments" divider, reply inline, "Open task ↗")
- **Messaging**:
  - day dividers ("Today")
  - a jump pill for unread messages
  - hover actions (react, reply, forward, more) and reply quotes ("Replied to: …")
  - attachment chips; voice notes with a waveform that shows played vs unplayed, plus duration
  - a personal composer placeholder ("Message Maya Chen…")
- **Sharing and roles**: each role has a one-line description of its access ("Support user: read-only access to the admin console"). Show the share link, invite and expiry together. Avatar stacks show presence.
- **Notification preferences**: each toggle is an icon + title, plus one line saying *what you'll receive* when the title doesn't already say it.

---

## 11. Accessibility baseline (non-negotiable)

- Contrast is ≥4.5:1 for body text and ≥3:1 for large text, icons, borders of inputs, and focus rings. Check with `scripts/contrast.py`.
- Everything is reachable and operable by keyboard. Tab order is logical. Focus is always visible (`:focus-visible`, never a bare `outline: none`).
- Every input has a programmatic label. Icon-only buttons have an `aria-label` and a tooltip. Images have `alt` (empty when decorative).
- Colour is never the only signal. Status uses colour + icon or shape + text.
- Targets are ≥24×24 CSS px on desktop and ≥44×44pt on touch, with ≥8px between them.
- Respect `prefers-reduced-motion`, `prefers-contrast` and `prefers-reduced-transparency` (see `apple-design` §14).
- Layout survives 200% text zoom. Use `rem`/`em` spacing for text containers and never disable pinch-zoom.
- Announce async results (toasts, form errors, live counts) through `aria-live` regions.
- Use semantic HTML first (`button`, `a`, `nav`, `main`, `table`, `label`) and ARIA only to fill gaps.

---

## 12. Mobile and touch ergonomics

- **Thumb zone.** Primary actions, composers and search go at the bottom. Sticky full-width CTAs ("Complete", "Request to book", "Add task") sit above the home indicator.
- **One task per screen** in focused flows. Use bottom sheets for create, confirm and pick actions, with a grabber and ✕.
- Touch targets are ≥44pt, and list rows are ≥56pt when they carry two lines.
- Every swipe action needs a visible alternative, such as a "…" menu.
- Use system pickers (wheel, date) and the right keyboard type (`inputmode`, `autocomplete`).
- **Glanceable home**: a greeting, a summary line, 2–4 primary actions as labeled round buttons (Add · Send · Request · Swap), then cards with "See all".
- Respect safe areas. Keep the floating tab bar or FAB off the content's last row by adding bottom padding.
- Haptics confirm meaningful commits (snap, success, error) and nothing else. See `apple-design` §13.

---

## 13. Responsive adaptation

Keep the same information architecture and adapt the components:

| Desktop | Mobile |
|---|---|
| Sidebar nav | Bottom tabs (≤5) + "More" |
| 3-pane list / detail / inspector | List → push to detail → inspector becomes a sheet |
| Data table | Cards that keep the 2–3 key columns, with the rest in the detail view |
| Hover actions | "…" menu or swipe, plus long-press |
| Modal | Full-screen sheet |
| Filter sidebar | Filter sheet + chips row |
| Multi-column KPIs | Horizontally scrollable KPI cards or a 2×2 grid |
| Tooltips | Tap to reveal, or inline helper text |
