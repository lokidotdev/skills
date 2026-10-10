# Content Design: UI Copy

Words are UX. The reference set shows that good copy does most of the heavy lifting: subtitles that state purpose, helper text that explains when a setting applies, and buttons that name outcomes. It also shows that typos undo the trust a premium visual builds.

## Contents
1. Voice and principles
2. Copy patterns, with templates
3. Microcopy library
4. Terminology and consistency
5. Proofreading pass

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

## 2. Copy patterns, with templates

| Element | Template | Good example |
|---|---|---|
| Page subtitle | `[Verb] [what] [scope/benefit].` | "Monitor cash flow and net change across your accounts." |
| Section description | `[What this section controls], [for whom/when].` | "Your account, and how this workspace behaves for everyone in it." |
| Setting row | Title + `[What happens] [when it applies] [why].` | "New teammates start with… Applied the moment someone accepts an invite, so nobody lands on an empty screen." |
| Option card | Label + `[Consequence for the user].` | "URL: customers access your content via a shared link." |
| Helper text | `[Format/why]. e.g. [example]` | "Leave empty for AWS S3. e.g. Training Data" |
| Placeholder | An example or syntax, never the label | "Write a comment… Use @ to mention" · "Search order, date, ID…" |
| Button | `[Verb] [object]` naming the outcome | "Publish changes", "Add holding", "Request to book" |
| Primary after review | `[Verb] [object] [key value]` | "Send 12 messages", "Renew for $249.90", "Launch scan" |
| Error | `[What happened]. [Why, if known]. [How to fix].` | "Couldn't connect to Slack. The token expired. Reconnect Slack." |
| Field error | `[What's needed]` | "Enter an email like name@company.com" |
| Empty state | `[Value headline]` + `[how it works]` + CTA | "Capture & share special moments with friends." + "Add moment" |
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

## 3. Microcopy library
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

## 4. Terminology and consistency
- Keep **one word per concept** across the product. If it's "Workspace", it's never also "Team space" or "Org". Maintain a small glossary in the project.
- **Use the same verb from button to toast**: "Archive" → "Archived · Undo". "Publish" → "Published".
- Don't mix singular and plural carelessly: "1 item" vs "2 items" (handle pluralisation, and avoid "1 items").
- Name things after the user's language, not internal or engineering terms ("Saved filter", not "Persisted query").
- Labels must be **unique within a form**. Two fields labeled "Provider" is a bug. Make them "Provider" and "Model".
- Copy must **match the layout**: a divider that says "or sign in with email" must sit above the email fields.

---

## 5. Proofreading pass (run every time)
1. Spell-check every visible string, including placeholders, tooltips, empty states and the error states nobody renders. The reference set shipped "Taks", "firts", "periode", "Is you skin", "No at all", "You have don't account?", "Allergies" spelled "Alergies".
2. Check grammar on pluralisation, articles and possessives.
3. Replace placeholder data (lorem ipsum, identical KPI values, the same description pasted on every card) with realistic, varied content.
4. Check that helper text is specific to its field and not copy-pasted.
5. Check that numbers, units and periods are consistent (no "$" in one column and "USD" in the next).
6. Read the flow aloud. Every button label should make sense without its surrounding text.
