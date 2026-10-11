# Data Display: Numbers, KPIs, Charts, Tables, Dashboards

In the reference set, the most common gap between a good data screen and a great one wasn't the visuals. It was context. A number with no comparison forces the user to do the analysis themselves. The great screens add that context in a few characters (a delta chip, "vs last month", "/ 100%", an ⓘ, a one-word verdict), not in sentences. The weaker ones put a description under every card and chart, which makes the dashboard noisy and knocks the values out of line.

## Contents
1. The number sentence
2. Metric polarity and delta colour
3. Comparisons, targets and benchmarks
4. Verdicts and thresholds
5. Freshness and data lag
6. KPI cards
7. Charts
8. Tables
9. Dashboards
10. Number and date formatting
11. Money and finance specifics

---

## 1. The number sentence

| Part | Purpose | Example |
|---|---|---|
| Label (+ⓘ definition) | What it is | "Engaged views ⓘ" |
| Value + unit | How much | `3,028` views, `1m 31s`, `$842.36`, `0.11 / 0.5 GB` |
| Baseline | Compared with what | "vs last month", "1,384 last period", "Prev close: 6195" |
| Delta | Change, with sign and arrow | `▲ 3.5%`, `↓0.3d slower`, `+8pp` |
| Colour | Good or bad, *by polarity* | green, red, or grey for neutral |
| Target or limit | Distance to a goal | "82% of max target", "7,530 / 10,000 steps" |
| Verdict | What it means | "Optimal", "Fair", "Needs improvement", "Positive dominated" |
| Freshness | How current it is | "Updated 11:30 AM", "Last sync 2m ago" |

This table is a menu, not a checklist. **The default KPI is label + value + delta + baseline.** Add the other parts only when the user acts on them:
- a target or limit when there is one (quotas, goals, budgets)
- a verdict when non-experts need meaning, as one word or a short chip ("Optimal", "Stable", "Top 8% in skincare")
- freshness once per page or per data source, not on every card
- a definition behind ⓘ, not as a line of text under the label

**Translate into human value** when you can: "Automation saved you a total of 93.2 hours last month" says more than "Automated tasks: 1,204". One such sentence per screen is plenty.

---

## 2. Metric polarity and delta colour

Colour shows **whether the change is good**, not which way it moved. In the reference set, higher bounce rate was shown green and lower return rate red. Both are wrong.

```ts
type Polarity = 'up-is-good' | 'down-is-good' | 'neutral';

function deltaTone(delta: number, polarity: Polarity, epsilon = 0.0005) {
  if (polarity === 'neutral' || Math.abs(delta) < epsilon) return 'neutral'; // grey: "same as last period"
  const good = polarity === 'up-is-good' ? delta > 0 : delta < 0;
  return good ? 'positive' : 'negative';
}
// The arrow always shows direction; colour shows meaning.
// Bounce rate +4% → ▲ 4% in red.  Returns −3% → ▼ 3% in green.
```

- Down-is-good examples: bounce rate, churn, cost, latency, error rate, returns, overdue tasks, time to close, CPU consumption, worst trade.
- Neutral examples: headcount, total sessions in an A/B test, anything whose goodness depends on context. Show these in grey.
- Use **pp** (percentage points) for changes in a percentage: conversion 16.2% → 18.7% is **+2.5pp**, not +15%.
- When nothing changed, say "same as last period" in grey. Don't show "+0.00%".

---

## 3. Comparisons, targets and benchmarks

- **Period over period**: put the comparison in the date control ("Last 7 days compared to the previous period", "Compare to: Mar 18–Mar 24").
- **Show the previous absolute value** when stakes are high: "6,293 · 1,384 last period". A percentage alone hides scale.
- **Side by side** for intuition: "Today $243.65 | Yesterday $208.19".
- **Target or limit**: progress bars toward "Max target". For quotas, show both used and remaining: "$2,150 used · $850 remaining · 72%".
- **Benchmarks**: "40% above industry average", "Top 5% performer", "Median 0% · 40th percentile" against a peer group the user can see and edit ("ARR < $100K · B2C").
- **Distributions over means** when the spread matters: "Average 7.4 years · P25 1.1 · Median 1.6 · P75 2.4".
- **Baselines in charts**: dashed average lines ("Avg. view 392"), "Prev close" lines, and a ghost line for the previous period.

---

## 4. Verdicts and thresholds

Non-experts need meaning, and experts like confirmation.
- Pair a score with a word and a colour: "7.94 / 10 · ✓ Strong positive", "82% High readiness", "Endurance fitness 38 · Fair".
- **State the thresholds** that produced the verdict: "Poor < 50 · Needs improvement 50–90 · Good > 90"; "Less than 75% had a great experience."
- Explain composite scores: list their components ("Social media 9.99 · KOL 6.28 · News 7.38") or show "Learn more".
- Shade target zones on charts (a "Good" band) so users read state without reading numbers.

---

## 5. Freshness and data lag

- Show freshness once for each live or synced source, usually in the page header or the card group's header: "Last update: just now", "Updated Monday, Oct 21, 11:30 AM", "Last sync 2m ago". Repeat it per card only when cards update independently.
- Disclose delays and gaps honestly: "Metrics may be delayed by an hour and aren't updated for inactive projects." · "Updates take up to 1 hour."
- Give auto-refresh a visible interval and controls ("Refresh · 30 seconds ▾", pause and resume streaming).
- Make missing data an explicit, actionable state ("Overnight data missing ›"), never an unexplained dip to zero.

---

## 6. KPI cards

```
┌──────────────────────────────────────┐
│ [icon] Label ⓘ                    ↗ │  ← drill-in
│ 12,450  leads                        │  ← tabular, large, unit muted
│ ▲ 6.4%  from last week   ▂▃▅▃▆▇     │  ← delta chip + baseline + sparkline
└──────────────────────────────────────┘
```
- Use 3–5 per row, ordered by importance, with the same anatomy on every card so labels, values and deltas line up across the row.
- **No description sentence under the label.** A KPI card has at most three text levels: label, value, and one line of delta or comparison. Put definitions behind ⓘ.
- Give it room: 20–24px padding, and 8–12px between the label and the value.
- A card can carry a composition sub-row: "With promotion 62% · Without 38%", "Desktop 8,900 · Mobile 3,550".
- A clickable card shows ↗ or a hover state. When the cards *select* a chart's metric, highlight the selected card.
- **Never ship duplicate placeholder values** (three cards all reading "3,926"). It reads as broken.
- The empty KPI states are "—" with a reason, "0 · from 0 (last 4 weeks)", and "Not enough data yet".

---

## 7. Charts

### Choosing the chart
| Question | Chart |
|---|---|
| How did it change over time? | Line or area (≤5 series); bars for discrete periods |
| How do categories compare? | Horizontal bars, sorted, with value labels |
| What makes up the whole? | Segmented (stacked) bar, or a stacked column over time. Pie or donut only for 2–4 parts with a centre label |
| How is it distributed? | Histogram, P25/median/P75, box plot |
| How close to the goal? | Progress bar or ring with "x / target" |
| When or where does it happen? | Heatmap by hour × day, or a map with a ranked list beside it |
| Many metrics at once | Small multiples with shared axes |

### Chart rules
- **Titles**: a plain noun title is fine for most charts ("Sales trend", "Traffic analytics"). Give an insight or question title to the one chart the page is about ("We've generated 3,920 leads today", "Task completion within SLA, last 30 days"). Add a subtitle only when the measure is ambiguous (units, P95 vs P50), never one that restates the title ("Project timeline: monitor milestone progress over time").
- Put the legend near the data, or label lines directly. Keep each series' colour the same across the whole app.
- Tooltips show the date, every series' value, and the difference ("On Running 2.37K · New Balance 1.89K · Difference 10.2%").
- **Annotate what needs explaining**, usually one or two marks: the highest and lowest points, an event on a spike or dip ("Email blast"), a "today" line, hatching for future or incomplete periods, a ghost line for the previous period.
- Bars start at zero. Keep gridlines faint and use ≤6 axis ticks with abbreviated values ($10k).
- Highlight the current or selected bar in full colour and leave the others as tints.
- Use tints of one hue for related series (new vs returning). Distinct hues are for unrelated categories.
- **Close with a recommendation** only when there's a concrete action: "Consistently high utilization may require scaling executor capacity. Learn more."
- Show the controls people use on that chart (usually the period). Put expand, export and share in a "…" menu instead of a row of buttons on every card.

---

## 8. Tables

| Element | Rule |
|---|---|
| Header | Small uppercase or muted labels; **type icons** (date, person, link, tag) for scannable schemas; sortable columns show ⇅ and the active direction; sticky on scroll |
| Selection | Leading checkbox; header checkbox shows the indeterminate state; selected rows tinted; a **floating bulk-action bar** ("4 rows selected · Change status · Download · Delete") |
| Numbers | Right-aligned, tabular figures, consistent decimals, units in the header |
| Status | Tinted chip with dot or icon + word; editable inline when the user owns it |
| People and companies | Avatar or logo + name; "+2" overflow for multiple values |
| Empty cell | Explicit ("No contact", "—", "Not set") in muted text, never blank |
| Long text | Truncate with an ellipsis + tooltip; a 2-line clamp for descriptions |
| Row actions | Appear on hover (desktop) or under "…"; the destructive one goes last |
| Row click | Opens a **side detail panel** (keeps list context) or the detail page; deep-linkable |
| Completeness | A column that prompts action ("Receipt: Missing / Attached") |
| Footer | "Showing 1–25 of 212,212", pagination or infinite scroll, "Total record: 10" |
| Toolbar | Search · filter pills · sort · group by · view toggle · column settings · export |
| Density | 32–40px rows for work tools; zebra striping only for very wide numeric tables |

Mobile: turn rows into cards that keep the 2–3 columns the user scans for, and push the rest into the detail view.

---

## 9. Dashboards

**Order of a good dashboard:**
1. **Greeting + summary sentence** ("Good morning, Joe. 2 tasks due today", "Here's how your SMS program is performing").
2. **What needs attention**: a queue with counts and actions ("Confirm pending payouts · 19", "Needs attention 3 · 2 high, 1 medium").
3. **KPIs**, with context (§1).
4. **Trends**: charts with insight titles.
5. **Breakdowns**: by segment, channel or category.
6. **Lists and activity**: recent items, an activity feed, top performers.
7. **Setup progress** while onboarding isn't finished ("Workspace setup 2/4").

- The header carries scope (product, location, team), date range + compare, and granularity (daily / weekly / monthly), plus Share, Export and Customize ("Set as default", "+ Add card").
- Keep the words few: a greeting or summary line, label + value + delta on the KPIs, plain chart titles, and at most one insight sentence. Separate the sections listed above with 40–64px of space rather than extra headings and descriptions.
- Primary jobs go in quick actions ("Send an invoice", "Draft a proposal", "+ Create flow").
- An empty dashboard shows sample or ghost charts with "Connect a data source", not a grid of zeros.

---

## 10. Number and date formatting

- Use thousands separators. Abbreviate large values (`1.2K`, `$4.8M`) and show the full value on hover. Keep decimals consistent within a column.
- Use `font-variant-numeric: tabular-nums` for every number that sits in a column or changes live. Mono is a good choice for IDs, hashes and code.
- Format durations as `1h 10m`, `2m 26s` and `0.06 ms`, choosing units for the magnitude.
- Use relative time for recent items ("12m", "2h ago", "yesterday") and absolute time beyond about a week, with the full timestamp on hover.
- Show the timezone whenever the time matters to more than one person ("10:55 UTC", "New York (UTC−5)").
- Shorten IDs with an ellipsis, add a copy button, and use a mono font: `ta-01KJ7…3R ⧉`.

---

## 11. Money and finance specifics

- Mask account and card numbers ("•••• 1937"). Offer a show/hide-balance eye. Never mask the amounts the user needs to act on.
- Separate **available** from **total** or pending ("$6.92 · $1.89 available"). Show in/out flows as a pair ("IN $230.00 · OUT $1,740.00").
- Installments and due dates: "1 of 4 installments · Due on the 18th · Pay now".
- Limits: "Today's limit $614.93 / $43,093.00 · Set card limits →". Offer a proactive guardrail ("Set a monthly limit. We'll notify you if you go over.").
- Every money-moving flow ends with a review (amount, fee, ETA, method, total), and then a receipt-style confirmation.
- Investment and trading surfaces show market state ("Closed"), last updated time, and P&L coloured by polarity. Clearly separate demo from live.
