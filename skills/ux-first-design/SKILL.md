---
name: ux-first-design
description: "UX-first product design for creating, updating, revamping and auditing app interfaces. It starts from the user's job, the flow, every state and the consequences of each action, writes the UI copy, and only then applies the visual layer. Ships a WCAG contrast checker and a UX/accessibility lint script. Use when someone asks to design, build, redesign, polish, review or audit a screen, flow, page or component (SaaS dashboards, CRMs, data tables, inboxes, chat, settings, signup, onboarding, pricing, paywalls, AI assistants, workflow builders, mobile apps), or says 'improve the UX/UI', 'make it look modern', 'fix usability', 'make this page better', or needs empty, loading and error states. Keywords: ux, ui, product design, usability, accessibility, wcag, dashboard, onboarding, ux audit, design review."
---

# UX-First Design

## Initial Response

When this skill is invoked without a concrete task, respond only with:

> Ready. Tell me what you're working on (a new screen or flow, a change to an existing one, a full revamp, or a UX audit) and who uses it. I'll start with the user's job and the flow, then every state, and only then the pixels.

Do not provide any other information until the user describes the task.

## The Core Idea

Most of good design is decisions nobody sees about what a person needs to know and do next. At every moment, on every screen, the interface must answer five questions:

1. **Where am I?**
2. **What is this telling me, and is it good or bad?**
3. **What can I do here, and which one thing do I most likely want to do?**
4. **What will happen if I do it?**
5. **What just happened, and what now?**

The UI is how those answers look. If the answers are wrong, no amount of polish saves the screen. If they're right, a calm, consistent visual layer makes them feel effortless. So **UX comes first and UI second, always in that order.** The references were all well polished, and many of them still failed on UX: the wrong colour on a delta, a placeholder used as the only label, unlabeled icon buttons. Polish doesn't prevent UX bugs.

Answering the five questions doesn't mean writing them out. The best screens in the reference set answer most of them with structure (placement, grouping, a chip, a count, the verb on the button) and save sentences for the few moments where a user would otherwise hesitate. Good UX guides the user. It doesn't spoon-feed them. See [Restraint: Words and Space](#restraint-words-and-space).

## Order of Work

| # | Step | Question | Output |
|---|---|---|---|
| 1 | **Job** | Who, in what situation, wants what outcome? | Job story + success signal |
| 2 | **Flow** | Which steps lead from trigger to done, and where can each one fail? | Numbered steps, decision and failure points |
| 3 | **Structure** | Which objects, which hierarchy, what goes where? | Object model, screen inventory, priority per screen |
| 4 | **States** | What does each screen look like when it's empty, loading, partial, failed, done, locked, and so on? | State matrix |
| 5 | **Consequences** | What is irreversible, costly, public or shared? | Review, undo and confirm plan |
| 6 | **Words** | What does each label, button and message say, and which few places need a description? | Copy deck |
| 7 | **Interaction** | How does it respond, how fast, and with what feedback? | Feedback map |
| 8 | **Visual** | How does it look? | Tokens + components ([visual-system](references/visual-system.md)) |
| 9 | **Verify** | Can a first-time user and a daily expert both succeed? | Walkthrough + [audit checklist](references/audit-checklist.md) |

Don't jump ahead to step 8 just because it's the visible part. When time is short you can compress steps, but never skip 1, 4 or 5.

## Modes

### Create (new screen, flow, or product)
1. Fill in the [UX brief](templates/ux-brief.md). Infer what you can from the code, the product and the request. Ask only for what you can't infer, in at most 1–3 questions.
2. Write the flow as numbered steps before writing any markup.
3. Choose a familiar pattern for each screen from [patterns](references/patterns.md). Use a novel pattern only when you can say why it's better.
4. Write the state matrix and the copy, then build.
5. Apply the visual system, then run the audit checklist on your own output.

### Update (add or change a feature in an existing product)
1. **Read the existing product first**: its tokens, components, navigation, naming and tone. Consistency beats your own taste, so reuse before inventing.
2. **Put the feature where the job already happens**, next to the object it affects. Don't give it a new nav item by default.
3. **Trace the ripple.** List the empty states, permissions, notifications, settings, onboarding, search and analytics this change touches.
4. Ship the smallest change that completes the job and list any follow-ups separately.

### Revamp (redesign something that exists)
1. **Audit first** (see the next mode). Record what works today, because users have muscle memory.
2. Re-derive the jobs and the top tasks, then rank them by frequency × importance.
3. Restructure the information architecture around jobs (for example *Build / Data / Monitor*), not around database tables or the org chart.
4. **Keep what people rely on**: object names, URLs, shortcuts, and where the primary actions sit. Change them only when you have a reason.
5. Redesign the states and the copy, then the visual layer.
6. Plan the transition: "what's new" hints, a temporary "View legacy dashboard" escape hatch for heavy users, and migration of saved views and filters.

### Audit (review only)
Use [audit-checklist](references/audit-checklist.md). Walk through the top tasks twice, once as a first-time user and once as a daily expert. Rank findings P0–P3. For each one give where it is, what's wrong, the impact on the user, and the fix. Start with the few findings that matter most and finish with quick wins.

## Restraint: Words and Space

The reference screens guide with structure first and words second, and the calm ones leave a lot of space empty. Every rule below is applied within these limits. The aim is balance: no sentence that the layout already says, and no missing sentence where a user would guess wrong.

**Guide with the lightest tool that works.**
1. **Structure**: placement, grouping, order, emphasis.
2. **Signals**: a specific label, an outcome verb, a chip, a count, a delta, an icon, an example placeholder, an ⓘ.
3. **Sentences**: a subtitle, helper text, an explanation.

Write a sentence only when structure and signals can't carry the meaning.

**A description earns its place** when it says something that isn't in the title, the control or the value, and the user needs it to act or to avoid a mistake. That covers a hidden consequence or scope ("Applied the moment someone accepts an invite"), surprising system logic ("Goals are funded based on their deadline"), a format or constraint ("Leave empty for public buckets"), reassurance at a real worry ("Applying is always free"), a definition of jargon, or a state with its way out ("Paused until July 20, 2026").

**It's noise** when it:
- restates the title ("Select cluster: select the cluster you want to use", "Profile: profile data")
- appears on every sibling because one of them needed it
- repeats something already on screen
- narrates the UI ("Here you can see…")
- is generic filler ("A comprehensive view of your statistics")

| Element | Default | Add one line when |
|---|---|---|
| Page | Title | The scope, cost or effect isn't obvious from the title. Inbox, Home and Overview need none |
| Section | Title (+ count) | It's a settings or form section whose effect isn't obvious |
| KPI or chart card | Label, value, delta, baseline | Never a sentence. Definitions go behind ⓘ. At most one insight sentence per dashboard |
| Row, or card in a grid | Title + one meta line of data | It's a catalog the user chooses from (templates, integrations, plans). Clamp every sibling to the same line count |
| Setting row, option card | Title | The consequence isn't obvious from the title |
| Form field | Label (+ example placeholder) | There's a format, a constraint or a consequence |
| Empty state | Headline + one CTA | The concept is new, so add one line on how it works |

Keep a subtitle to one line and helper text to one short sentence. Anything longer belongs in a tooltip, a "Learn more" link or the docs.

**Breathing space.** Space is the first separator: whitespace before lines, lines before boxes. The gap between groups is at least twice the gap inside a group: 4–8px inside a unit (label to value, title to subtitle), 12–16px between items, 24–32px between cards and from the header to the content, 40–64px between page sections. Use comfortable density by default and compact only for tables, logs and lists people scan. Keep forms, settings, review steps, onboarding and empty states in a narrow column with open space around them. A unit carries at most three text levels: a label, a value and a meta line.

**Alignment.** Each column has one left edge. Siblings share one anatomy: if one card in a row needs a description, all of them get one, clamped to the same number of lines with actions pinned to the bottom, or none of them do. Uneven descriptions are the most common cause of ragged cards and misaligned values. Details are in [content-design §2](references/content-design.md) and [visual-system §5](references/visual-system.md).

## The Twelve UX Rules

Each rule is covered in more depth in the references. These are the ones you must not break. Apply them through the restraint limits above: a rule that calls for context or explanation means *where it's needed*, not on every element.

### 1. Design for a job, not a page
- Write it down: *When ___, I want to ___, so I can ___.* The situation changes the design. "Monday morning" calls for a summary of what's due today. "A deal slipped" calls for an alert with a way to fix it.
- Give each screen one primary job. Secondary jobs should be reachable, not equal.
- Name navigation after its contents or job ("Runs", "Pipelines", "Slipping deals"), not after vague umbrellas ("Hub", "Center").
- **Put create actions where the list is.** For example, "+ New variable" inside the group, "+" on each kanban column, and "+ Add a task for today… press Enter" at the end of Today.

### 2. Wayfinding on every screen
- Give every page a specific title. Add a **one-line subtitle only when the title doesn't carry the scope or effect**, for example "Monitoring status for Framework SOC 2 Type II" or "Scan deployed AI agents. API usage applies." Pages like Inbox, Home, Tasks and Overview need none.
- Use breadcrumbs from depth 2 onward, and give the nav a clear active state.
- When a global scope exists (workspace, position, environment), keep the selector visible and **restate the scope in the header**, for example "All positions · Oct 15–22".
- Steppers name every step, mark finished steps ✓, and show "x of y".
- There is always a way out: ✕, Back, Cancel, Skip for now, or Esc.

### 3. Every number gets context, in a few characters
A bare number is noise, and so is a number buried in sentences. The default is **label, value, delta and baseline**: `Engaged views  3,028  ▲ 3.5% vs last period`. Add a target, a verdict or freshness only when the user acts on it, put definitions behind ⓘ, and show freshness once per page or data source, not on every card. The full menu of parts is in [data-display §1](references/data-display.md).
- **Delta colour follows meaning, not direction.** Bounce rate going up is bad (red) and returns going down is good (green). Store a polarity for every metric. Several polished designs in the reference set get this wrong.
- Show quotas as "x / limit" (16/50 seats, 96/264 credits). For budgets, show both used and remaining.
- Give a verdict as a word or short chip when non-experts need meaning: "0.88 · Optimal", "18.4% · Stable".
- Plain noun titles are fine for charts ("Sales trend"). Give an insight title to the one chart the page is about ("We've generated 3,920 leads today"), and add a recommendation only when there's a concrete action.

### 4. Design every state
The happy path is one state out of about fifteen. Cover first-use empty, no results, loading, partial or missing data, error with a fix path, success with the next step, disabled *with a reason*, locked *with an unlock path*, permission denied, stale data, the draft → saved → published lifecycle, paused, live vs test mode, limit reached, lapsed or expired, and overflow. The matrix and the copy patterns are in [ux-foundations §5](references/ux-foundations.md) and [content-design](references/content-design.md).

### 5. Show consequences before a commit, and make commits reversible
- Before anything that spends money, sends, publishes or deletes, **show exactly what will happen**: recipients ("12 recipients, each message sent individually"), fee, ETA, total, and what data is shared ("Lumora receives everything below").
- Add a review step for multi-field commits ("Review & deploy", "Review & send").
- Prefer **undo, drafts, autosave, version history, test mode and pause** to confirmation dialogs. Confirm only irreversible actions. Name the consequence and use a specific verb such as "Delete node", never "OK".
- Default to safety: "Stop if they reply" on, "Test mode" visible, destructive actions separated, red, and last.

### 6. Reassure at the moment of anxiety
Find where the user hesitates (sharing data, paying, applying, connecting accounts, granting permissions) and answer the unspoken worry right there, in one line:
*"Applying is always free. We never apply on your behalf."* · *"Your credentials are encrypted and used only to…"* · *"You can change this later in Settings."* · *"7-day free trial, then $900/year. Cancel anytime."*
Use one line per real decision point, not a reassurance on every section. Never hide terms. Honesty is part of UX.

### 7. Common path first, advanced one level deeper
- Show the 20% of features that get 80% of use, and collapse the rest ("Advanced options", "Show more").
- On mobile onboarding, ask one question per screen. Desktop forms get titled sections. A section gets a description only when its effect isn't obvious ("Leave empty for public buckets"), never one that restates the title.
- When there are ≤5 options, show them all as segmented controls or option cards (one tap) instead of a dropdown.
- Disclosure isn't hiding: collapsed groups still show counts, as in "This week (3)" and "Later (4)".

### 8. Inputs are a conversation
- Put **visible labels above fields**. A placeholder only shows an example ("e.g. Training data") or syntax ("Use @ to mention").
- Mark whichever is rarer, required or optional. Add helper text only for a format, a constraint or a consequence. Most fields need just a label and an example. Validate when the user leaves a field, not on submit.
- Use smart defaults, presets (25/50/75%/Max) and in-field constraints ("Min 0.00025 BTC"), and add counters near limits ("107/1600 · 2 SMS").
- For sensitive or unusual questions, say why you're asking ("We'll use this to personalize your feed"). Always offer an honest escape: "None of the above", "No preference", "I don't have one".

### 9. One obvious next action
- Each view (or card) gets exactly one primary button. Everything else is secondary or tertiary.
- Labels are **verbs that name the outcome**: "Publish changes", "Send to 12 recipients", "Renew for $249.90", "Continue with this swarm". Never "Submit", "OK" or "Yes".
- After success, say what happened and what comes next, with a single CTA ("Your agents are live → Go to dashboard").
- Dashboards lead with what needs attention, such as "3 conflicts · 2 overtime, Fix warnings" or "Confirm pending payouts (19)".

### 10. Fast for experts, safe for novices
- Offer ⌘K search and commands, and teach shortcuts where they're used ("Click here to reply, or press R", "Shift+Enter for a new line").
- Support inline quick-add with Enter, bulk select with a floating action bar, saved views and filters, templates, and duplicate.
- Use row hover actions, inline status editing, and a **side detail panel** that keeps the list visible.
- Every shortcut needs a visible equivalent. Speed features are never the only way to do something.

### 11. Explain the system where it would surprise
Make hidden logic visible when a user would otherwise guess wrong. If the behaviour is what anyone would expect, don't explain it.
- Filter logic: "OR within, AND across groups".
- When a setting applies: "Applied the moment someone accepts an invite".
- How a score is computed, and why AI suggested something: reasons plus evidence.
- What automation will do next.
- Why something is disabled: "Coming soon".
- Data lag: "Metrics may be delayed by an hour".

For AI, see [ai-and-automation](references/ai-and-automation.md).

### 12. Motivate honestly
Progress bars, "2/4 steps", streaks, XP and celebrations all work when they're tied to the user's real goal. Also:
- Design the lapsed state ("3-day streak lost").
- Use one unit per leaderboard.
- Make paywalls name the value and the exact price and renewal terms.
- Offer *pause* before *cancel*.
- No dark patterns: no confirmshaming, no hidden renewals, no fake scarcity.

## The UI Layer, in Brief

The UI serves the UX. Full tokens and rules are in [visual-system](references/visual-system.md).
- **A calm canvas**: a neutral background, white (or near-black) cards, hairline borders, and soft shadows only on floating layers.
- **One accent colour** for primary actions, active states, selection, focus and links. Semantic colours are **only for status**: green for success, amber for warning or pending, red for error or destructive, blue for info or in progress, grey for neutral or draft. Show them as tinted chips with an icon or dot plus text. Never rely on colour alone.
- **Type**: one sans-serif for the UI, with **tabular or mono figures** for numbers, IDs, code and timestamps. Section and table headers are small uppercase mono labels. Build hierarchy from size, weight and colour together.
- **Space**: a 4px grid at comfortable density. Gaps between groups are at least twice the gaps inside them, sections are separated by space before lines, focused tasks sit in a narrow column, and everything aligns to columns. See [Restraint](#restraint-words-and-space) and [visual-system §5](references/visual-system.md).
- **Icons**: one outline set with a consistent stroke, used as leading icons on nav, properties and KPI labels. Icon-only buttons need a tooltip and an `aria-label`. Primary navigation keeps its text labels.
- **Motion and touch feel**: follow the `apple-design` skill if installed (instant press feedback, springs, interruptible motion, reduced motion).
- **Verify contrast** with `scripts/contrast.py`: 4.5:1 for body text, 3:1 for large text and UI parts.

## Anti-Patterns Found in Polished Designs

| Anti-pattern | Fix |
|---|---|
| Placeholder used as the only label | Label above the field; placeholder shows an example |
| Icon-only tab bars, footer actions or "revoke ✕" with no label | Text labels, or tooltip + `aria-label` |
| Delta coloured by direction (bounce ▲ shown green) | Colour by metric polarity |
| Two fields with the same label ("Provider", "Provider") | Unique, specific labels ("Provider", "Model") |
| Copy that contradicts the layout ("Or sign in with email" placed above the social buttons) | Copy describes what actually follows |
| Identical KPI values, lorem ipsum, the same helper text pasted under every field | Realistic, varied content. Placeholder data is a bug |
| Typos in the UI ("Taks", "firts", "periode", "Is you skin") | A proofreading pass on every deliverable |
| Dark-blue title on a dark card | Run the contrast check |
| Mixed units in one ranked list (XP vs $) | One unit per column or list |
| Large blank area with no guidance | An empty state with the next action |
| A subtitle that restates the title ("Profile: profile data", "Overview: a comprehensive view of your statistics") | Delete it, or say what the title can't (scope, effect, cost) |
| A description on every card in a grid or every chart, so cards end up different heights and values don't line up | Label + value + meta, with definitions behind ⓘ. If a description is needed, give one to every sibling and clamp them all to the same length |
| The same explanation twice (a wizard step card and the page header, a page subtitle and a section subtitle) | Say it once, in the place closest to the decision |
| Everything at the dense end: tight card padding, no section spacing, text on every line | Comfortable density, a clear spacing rhythm, at most three text levels per unit |
| "Submit" / "OK" / "Are you sure?" | Outcome verbs and specific consequences |
| Confirmation dialog for a reversible action | Undo toast |

## Reference Files

| File | Read when |
|---|---|
| [references/ux-foundations.md](references/ux-foundations.md) | Every create, update or revamp: jobs, IA, navigation, wayfinding, states, feedback, safety, forms, search and filtering, collaboration, accessibility, mobile ergonomics |
| [references/data-display.md](references/data-display.md) | Dashboards, KPIs, charts, tables, analytics, finance, monitoring |
| [references/ai-and-automation.md](references/ai-and-automation.md) | AI chat, copilots, agents, generated content, workflow and automation builders |
| [references/onboarding-and-growth.md](references/onboarding-and-growth.md) | Signup and login, onboarding, empty states, activation, gamification, pricing, paywalls, trials, referrals |
| [references/content-design.md](references/content-design.md) | Any UI text: how much to write, titles, buttons, helper text, errors, empty states, confirmations, success messages |
| [references/patterns.md](references/patterns.md) | Anatomy of specific screens and components: app shell, page header, KPI card, table, detail panel, kanban, inbox, chat, settings, modal, wizard, canvas, mobile home, sheets |
| [references/visual-system.md](references/visual-system.md) | The visual layer: colour, type, spacing rhythm and breathing room, alignment, radius, elevation, icons, density, dark mode, charts |
| [references/audit-checklist.md](references/audit-checklist.md) | Audits, reviews, revamps, and the final self-check before delivering |
| [references/reference-set.md](references/reference-set.md) | Where these rules come from, with example screens for each pattern |
| [templates/ux-brief.md](templates/ux-brief.md) | The start of every create or revamp |
| `scripts/contrast.py` | Checking colour pairs: `python3 scripts/contrast.py "#6B6B75" "#FFFFFF"` |
| `scripts/ux_lint.py` | Scanning a codebase for UX and accessibility smells: `python3 scripts/ux_lint.py src/` |

Related skills: use `apple-design` for motion, gestures, springs and materials. Use `ui-ux-pro-max` (if installed) for style, palette and font-pairing exploration. This skill decides *what the interface must do and say*. Those skills help decide *how it moves and looks*.

## Delivering Work

1. Open with the **UX rationale** in 3–6 bullets: the job, the flow, the key states, the safety decisions, and any assumptions you made about users.
2. Then present the design or code.
3. End with the checklist results and open questions, such as decisions the user should make or things to test with real users.

## Quick Reference

| Need | Do |
|---|---|
| Start anything | Job story → flow → state matrix, *then* layout |
| Page header | Breadcrumb · title + status chip · subtitle *only if the title can't carry it* · tabs · secondary actions · **one** primary action (rightmost) |
| KPI | Label ⓘ · tabular value + unit · delta chip coloured by polarity · "vs [baseline]". No sentence |
| Empty state | Headline + one primary CTA. Add one line on how it works only for a new concept, and an optional import or template |
| Error | What happened + why + how to fix, next to the cause, with the user's input kept |
| Destructive | Undo if possible. If not: name the object and consequence, use a specific verb, red, separated |
| Paying or sending | Review step: amount, fee, ETA, recipients, masked method; price on the button |
| Form field | Label above · example placeholder · helper text only for format, constraint or consequence · inline validation · required/optional marked |
| Description or subtitle | Only if it says what the title, control or value can't, and the user needs it. One line. Same anatomy across siblings |
| Spacing | 4–8 inside a unit · 12–16 between items · 24–32 between cards · 40–64 between sections · comfortable by default |
| ≤5 options | Segmented control or option cards, not a dropdown |
| Filters | `Label: value` pills · applied filters as removable chips · counts · Clear all · Save view |
| Table | Type icons in headers · right-aligned tabular numbers · status chips · hover actions · bulk bar · explicit empty cells |
| AI output | Show the work (steps, sources) · why · uncertainty flags · edit, retry, 👍👎 · human approves before effects |
| Onboarding | Name the steps · say why you ask · one question per screen on mobile · skip · "change later" |
| Mobile | Labeled bottom tabs ≤5 · separate create action · actions in the thumb zone · sheets for tasks · 44pt targets |
| Status colour | Green ok · amber pending/warn · red error/destructive · blue info/in progress · grey neutral, always with text |
| Before delivering | Proofread · cut descriptions that restate titles · check spacing rhythm and sibling alignment · contrast check · keyboard pass · every state rendered · realistic data |
