# Content Design: UI Copy

Words are UX, and so is leaving them out. In the reference set, the best copy is short and sits exactly where a decision happens: a button that names its outcome, one line saying when a setting applies, a reassurance beside the payment field. Most of each screen carries no sentences at all. The weaker screens describe everything, every card and section included, and the extra text makes them look cluttered and misaligned. Typos undo the trust a premium visual builds.

## Contents
1. Voice and principles
2. How much to write
3. Copy patterns, with templates
4. Microcopy library
5. Terminology and consistency
6. Proofreading pass

---

## 1. Voice and principles
- **Plain and specific.** "Send to 12 recipients", not "Proceed". "Slipping deals", not "At-risk opportunities pipeline view".
- **Short.** Front-load the important words, because users scan the first 2–3. Keep a subtitle to one line and helper text to one sentence.
- **Human, not cute.** A greeting or a 👋 on a dashboard is fine. Jokes inside errors and money flows are not.
- **Sentence case** for everything (titles, buttons, labels). Use Title Case only if the product already does.
- **Numerals** for numbers ("3 tasks", not "three tasks"). Units and periods always attached ("+12% vs last month").
- **Active voice, user as the subject** where possible: "You changed the status", "You have 8 days left in your trial".
- **No jargon without a definition.** Put an ⓘ on terms like "slippage", "P95" or "10DLC", or define them inline.

---

## 2. How much to write

The goal is balance. Cutting every description leaves people guessing, and describing everything buries the few lines that matter. Decide line by line.

### Three tools, lightest first
1. **Structure**: placement, grouping, order and emphasis. Putting a control next to the thing it changes explains the control.
2. **Signals**: a specific label ("Slipping deals"), an outcome verb ("Send to 12 recipients"), a status chip ("Paused"), a count ("This week (3)"), a delta ("▲ 3.5% vs last period"), an example placeholder ("e.g. Training data"), an ⓘ for a definition.
3. **Sentences**: a subtitle, helper text, an explanation, a reassurance.

Reach for a sentence only when the first two can't carry the meaning.

### The test for any description
Cover the line and ask: *what would the user get wrong, or hesitate over, without it?* If the answer is "nothing", delete it. If the answer is real, keep it and make it as short as it can be.

### Lines that earn their place (from the reference set)
| Kind | Example |
|---|---|
| A consequence or scope you can't see | "Applied the moment someone accepts an invite, so nobody lands on an empty screen." · "Lumora receives everything below, including your name and contact, when you send." |
| System logic that would surprise | "Goals are funded based on their deadline." · "OR within, AND across groups" |
| When you can skip something | "Provide credentials to access private buckets. Leave empty for public buckets." |
| A format or constraint | "Min 0.00025 BTC" · "Leave empty for AWS S3" |
| Reassurance at a real worry | "Applying is always free. We never apply on your behalf." |
| Jargon or a test name | "Tests whether attackers can reveal hidden system instructions." |
| A state and its way out | "Auto saves are paused · Paused until July 20, 2026" · "3 prompts require immediate attention." |
| A cost before acting | "Scan deployed AI agents for vulnerabilities. API usage applies." |

### Lines that are noise (also from the reference set)
| Kind | Example | Instead |
|---|---|---|
| Restates the title | "Select cluster: select the cluster you want to use for your run." · "Storage configuration: configure your storage instance settings." · "Profile: profile data" | Title only |
| Generic filler | "Overview: a comprehensive view of your statistics" · "Lorem ipsum dolor sit amet" | Title only, or a real scope ("All products · Last 7 days") |
| One per sibling because one needed it | A description under every chart card ("Monitor milestone progress over time"), every KPI, every nav item | Label + value; definitions behind ⓘ |
| Said twice | The wizard step card and the page header both describe the step. The page subtitle repeats as the first section's subtitle | Say it once, nearest the decision |
| Narrates the UI | "Here you can see your recent activity." · "Click the button below to continue." | The layout and the button label |
| Explains the obvious | "Toggle this switch to enable notifications" | The label and the toggle |

### Budget
| Element | Default | Add one line when |
|---|---|---|
| Page | Title | The scope, cost or effect isn't in the title |
| Section | Title (+ count) | It's a settings or form section whose effect isn't obvious |
| KPI or chart card | Label, value, delta, baseline | Never a sentence. ⓘ for definitions. One insight sentence per dashboard at most |
| Row or grid card | Title + one meta line of data ("8 tasks · 2 done", "Started 2 minutes ago") | The user is choosing from a catalog (templates, integrations, plans). Clamp all siblings to the same line count |
| Setting row or option card | Title | The consequence isn't obvious from the title |
| Form field | Label (+ example placeholder) | There's a format, a constraint or a consequence |
| Empty state | Headline + one CTA ("No experience added yet" · "Add experience") | The concept is new: add one line on how it works |
| Reassurance | None | It's a real decision point: money, data, sending, permissions |

### Length
- Subtitle: one line, about 60–90 characters.
- Helper text: one short sentence.
- Option-card consequence: one line, two at most.
- Anything longer belongs behind "Learn more", in a tooltip, or in the docs. Long text on a work surface clamps to two lines with "Show more".

### Where it shows up visually
A description is a design element, not free. Each one adds a text level, pushes content down and can wrap differently from its neighbours. Count text levels per unit (label, value, meta) and stop at three. If sibling cards need descriptions, give all of them one and clamp them to the same number of lines. Otherwise give none of them one.

---

## 3. Copy patterns, with templates

These are templates for when a line *is* needed. They are not a list of lines every screen must have. Check each one against §2 first.

| Element | Template | Good example |
|---|---|---|
| Page subtitle (when the title can't carry it) | `[What it covers or affects] [scope/cost].` | "Monitoring status for Framework SOC 2 Type II." · "Your account, and how this workspace behaves for everyone in it." |
| Section description (settings and forms only) | `[What this controls], [for whom/when].` | "Leave empty for public buckets." |
| Setting row | Title + `[What happens] [when it applies] [why].` | "New teammates start with… Applied the moment someone accepts an invite, so nobody lands on an empty screen." |
| Option card | Label + `[Consequence for the user].` | "URL: customers access your content via a shared link." |
| Helper text | `[Format/why]. e.g. [example]` | "Leave empty for AWS S3. e.g. Training Data" |
| Placeholder | An example or syntax, never the label | "Write a comment… Use @ to mention" · "Search order, date, ID…" |
| Button | `[Verb] [object]` naming the outcome | "Publish changes", "Add holding", "Request to book" |
| Primary after review | `[Verb] [object] [key value]` | "Send 12 messages", "Renew for $249.90", "Launch scan" |
| Error | `[What happened]. [Why, if known]. [How to fix].` | "Couldn't connect to Slack. The token expired. Reconnect Slack." |
| Field error | `[What's needed]` | "Enter an email like name@company.com" |
| Empty state | `[What goes here or why it matters]` + CTA. Add `[how it works]` only for a new concept | "No experience added yet" + "Add experience" · "Speak or type to begin. Your assistant takes it from there." |
| No results | `No [things] match [query/filters].` + fix | "No results for 'acme' with 3 filters. Clear filters" |
| Success | `[What happened, specific]. [What's next].` | "Withdrawal started. $750.00 to Chase ••4281 arrives tomorrow." |
| Confirmation title | `[Verb] [object name]?` | "Delete 'Q4 Growth Plan'?" |
| Confirmation body | `[Exact consequence]. [Reversibility].` | "This removes the node and its connections. This can't be undone." |
| Confirmation buttons | `Cancel` + `[Same verb] [object]` | "Cancel" · "Delete node" |
| Warning / limit | `[Limit/state]. [Why]. [Path].` | "Daily sending limit: 300 emails. New accounts start low. Contact support to raise it." |
| Disabled reason | `[Why] / [when]` | "Coming soon" · "Add a payment method to enable" |
| Reassurance | `[Worry answered], [promise].` | "Applying is always free. We never apply on your behalf." |
| Why we ask | `We'll use this to [benefit].` | "We'll use this to personalize your experience." |
| Status chip | One word or a short phrase in a consistent tense | Draft · Running · Paused · Failed · Pending · Verified |
| Activity item | `[Actor] [verb past] [object] [context]` | "Matthew mentioned you in Pick hero photography" |
| Greeting + summary | `Good [time], [name].` + `[the one thing that matters today]` | "Good morning, Erşad. Wednesday 7 October · 2 tasks due today" |
| Chart title | The insight or question | "We've generated 3,920 leads today!" |
| Data disclaimer | `[What may be off] [by how much] [when].` | "Metrics may be delayed by an hour and aren't updated for inactive projects." |
| AI disclaimer | `[Name] can make mistakes. Double-check important info.` | |

---

## 4. Microcopy library
- **Relative time**: "just now", "12m", "2h ago", "Yesterday", "Mar 20". Show the full timestamp on hover.
- **Counts in labels**: "Applicants 9", "Inbox 3", "This week (3)", "Showing 4 of 4".
- **Freshness**: "Last updated: just now", "Updated Monday, Oct 21, 11:30 AM", "Last sync 2m ago".
- **Saving**: "Saving…", "✓ Saved", "• Unsaved changes", "Last saved 1 minute ago · Version 2".
- **Progress**: "2 of 4 steps completed", "Day 8 of 14", "1 of 4 installments", "22/25 posts this cycle · 2 days left".
- **Undo toast**: "Task archived · Undo", "3 rows deleted · Undo".
- **Keyboard hints**: "Press R to reply", "⌘K", "Shift + Enter for a new line, Enter to submit", "Use ⌘K for shortcuts".
- **New content**: "Show 24 new posts", "3 new comments", "1 unread message".
- **Trust**: "Your credentials are encrypted and only used to…", "You can always change this later", "No commitment. Cancel anytime."
- **Escape options**: "Skip for now", "None of the above", "No preference", "Not now", "Back to page".

---

## 5. Terminology and consistency
- Keep **one word per concept** across the product. If it's "Workspace", it's never also "Team space" or "Org". Maintain a small glossary in the project.
- **Use the same verb from button to toast**: "Archive" → "Archived · Undo". "Publish" → "Published".
- Don't mix singular and plural carelessly: "1 item" vs "2 items" (handle pluralisation, and avoid "1 items").
- Name things after the user's language, not internal or engineering terms ("Saved filter", not "Persisted query").
- Labels must be **unique within a form**. Two fields labeled "Provider" is a bug. Make them "Provider" and "Model".
- Copy must **match the layout**: a divider that says "or sign in with email" must sit above the email fields.

---

## 6. Proofreading pass (run every time)
1. **Cut pass first.** Delete every description that restates its title, sits on every sibling because one needed it, repeats something already on screen, or narrates the UI. For each line left, ask what the user would get wrong without it (§2). Then check the opposite: every irreversible action, cost, hidden consequence and sensitive ask has its one line.
2. Spell-check every visible string, including placeholders, tooltips, empty states and the error states nobody renders. The reference set shipped "Taks", "firts", "periode", "Is you skin", "No at all", "You have don't account?", "Allergies" spelled "Alergies".
3. Check grammar on pluralisation, articles and possessives.
4. Replace placeholder data (lorem ipsum, identical KPI values, the same description pasted on every card) with realistic, varied content.
5. Check that helper text is specific to its field and not copy-pasted.
6. Check that numbers, units and periods are consistent (no "$" in one column and "USD" in the next).
7. Read the flow aloud. Every button label should make sense without its surrounding text.
