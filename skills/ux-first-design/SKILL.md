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

## Order of Work

| # | Step | Question | Output |
|---|---|---|---|
| 1 | **Job** | Who, in what situation, wants what outcome? | Job story + success signal |
| 2 | **Flow** | Which steps lead from trigger to done, and where can each one fail? | Numbered steps, decision and failure points |
| 3 | **Structure** | Which objects, which hierarchy, what goes where? | Object model, screen inventory, priority per screen |
| 4 | **States** | What does each screen look like when it's empty, loading, partial, failed, done, locked, and so on? | State matrix |
| 5 | **Consequences** | What is irreversible, costly, public or shared? | Review, undo and confirm plan |
| 6 | **Words** | What does each label, button, helper text and message say? | Copy deck |
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

## The Twelve UX Rules

Each rule is covered in more depth in the references. These are the ones you must not break.

### 1. Design for a job, not a page
- Write it down: *When ___, I want to ___, so I can ___.* The situation changes the design. "Monday morning" calls for a summary of what's due today. "A deal slipped" calls for an alert with a way to fix it.
- Give each screen one primary job. Secondary jobs should be reachable, not equal.
- Name navigation after its contents or job ("Runs", "Pipelines", "Slipping deals"), not after vague umbrellas ("Hub", "Center").
- **Put create actions where the list is.** For example, "+ New variable" inside the group, "+" on each kanban column, and "+ Add a task for today… press Enter" at the end of Today.

### 2. Wayfinding on every screen
- Give every page a title and a **one-line purpose subtitle**, for example "Transactions: monitor cash flow and net change across your accounts."
- Use breadcrumbs from depth 2 onward, and give the nav a clear active state.
- When a global scope exists (workspace, position, environment), keep the selector visible and **restate the scope in the header**, for example "All positions · Oct 15–22".
- Steppers name every step, mark finished steps ✓, and show "x of y".
- There is always a way out: ✕, Back, Cancel, Skip for now, or Esc.

### 3. Every number gets context
A bare number is noise. Write the full **number sentence**: value + unit + baseline + direction coloured *by meaning* + target or limit + verdict + freshness + definition.
`3,028 engaged views · ▲ 3.5% vs 1,384 last period · updated 2 min ago ⓘ`
- **Delta colour follows meaning, not direction.** Bounce rate going up is bad (red) and returns going down is good (green). Store a polarity for every metric. Several polished designs in the reference set get this wrong.
- Show quotas as "x / limit" (16/50 seats, 96/264 credits). For budgets, show both used and remaining.
- Give a verdict for non-experts: "0.88 · Optimal", or "72 · Needs improvement (under 75% had a good experience)".
- Lead with titles that state the insight ("We've generated 3,920 leads today") and add a recommendation when there is one.

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
Never hide terms. Honesty is part of UX.

### 7. Common path first, advanced one level deeper
- Show the 20% of features that get 80% of use, and collapse the rest ("Advanced options", "Show more").
- On mobile onboarding, ask one question per screen. Desktop forms get titled sections with a one-line description each.
- When there are ≤5 options, show them all as segmented controls or option cards (one tap) instead of a dropdown.
- Disclosure isn't hiding: collapsed groups still show counts, as in "This week (3)" and "Later (4)".

### 8. Inputs are a conversation
- Put **visible labels above fields**. A placeholder only shows an example ("e.g. Training data") or syntax ("Use @ to mention").
- Mark whichever is rarer, required or optional. Helper text says why or gives the format. Validate when the user leaves a field, not on submit.
- Use smart defaults, presets (25/50/75%/Max) and in-field constraints ("Min 0.00025 BTC"), and add counters near limits ("107/1600 · 2 SMS").
- Explain why you're asking ("We'll use this to personalize your feed"), and always offer an honest escape: "None of the above", "No preference", "I don't have one".

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

### 11. Explain the system
Make the hidden logic visible:
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
- **Space**: a 4px grid. Group by proximity, use whitespace before divider lines, and align to columns.
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
| "Submit" / "OK" / "Are you sure?" | Outcome verbs and specific consequences |
| Confirmation dialog for a reversible action | Undo toast |

## Reference Files

| File | Read when |
|---|---|
| [references/ux-foundations.md](references/ux-foundations.md) | Every create, update or revamp: jobs, IA, navigation, wayfinding, states, feedback, safety, forms, search and filtering, collaboration, accessibility, mobile ergonomics |
| [references/data-display.md](references/data-display.md) | Dashboards, KPIs, charts, tables, analytics, finance, monitoring |
| [references/ai-and-automation.md](references/ai-and-automation.md) | AI chat, copilots, agents, generated content, workflow and automation builders |
| [references/onboarding-and-growth.md](references/onboarding-and-growth.md) | Signup and login, onboarding, empty states, activation, gamification, pricing, paywalls, trials, referrals |
| [references/content-design.md](references/content-design.md) | Any UI text: titles, buttons, helper text, errors, empty states, confirmations, success messages |
| [references/patterns.md](references/patterns.md) | Anatomy of specific screens and components: app shell, page header, KPI card, table, detail panel, kanban, inbox, chat, settings, modal, wizard, canvas, mobile home, sheets |
| [references/visual-system.md](references/visual-system.md) | The visual layer: colour, type, spacing, radius, elevation, icons, density, dark mode, charts |
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
| Page header | Breadcrumb · title + status chip · purpose subtitle · tabs · secondary actions · **one** primary action (rightmost) |
| KPI | Label ⓘ · tabular value + unit · delta chip coloured by polarity · "vs [baseline]" · freshness |
| Empty state | Why it's empty + value of filling it + one primary CTA + optional import or template |
| Error | What happened + why + how to fix, next to the cause, with the user's input kept |
| Destructive | Undo if possible. If not: name the object and consequence, use a specific verb, red, separated |
| Paying or sending | Review step: amount, fee, ETA, recipients, masked method; price on the button |
| Form field | Label above · example placeholder · helper text · inline validation · required/optional marked |
| ≤5 options | Segmented control or option cards, not a dropdown |
| Filters | `Label: value` pills · applied filters as removable chips · counts · Clear all · Save view |
| Table | Type icons in headers · right-aligned tabular numbers · status chips · hover actions · bulk bar · explicit empty cells |
| AI output | Show the work (steps, sources) · why · uncertainty flags · edit, retry, 👍👎 · human approves before effects |
| Onboarding | Name the steps · say why you ask · one question per screen on mobile · skip · "change later" |
| Mobile | Labeled bottom tabs ≤5 · separate create action · actions in the thumb zone · sheets for tasks · 44pt targets |
| Status colour | Green ok · amber pending/warn · red error/destructive · blue info/in progress · grey neutral, always with text |
| Before delivering | Proofread · contrast check · keyboard pass · every state rendered · realistic data |
