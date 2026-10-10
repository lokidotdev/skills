# The Reference Set

This skill was distilled from 358 product-design shots: 38 primary images plus 282 more from the same thread. They're mostly the portfolio work of a product designer (Marcel Kargul / kargul.studio) and cover modern SaaS, AI and mobile products. The source images are not published in this repo (they are third-party work). In the author's local checkout they live at:

- `_local/ux-first-design-research/images/` (the 38 primary shots, `NN_<id>.png|jpg`)
- `_local/ux-first-design-research/thread_images/` (all 320 thread shots, `NNN_<id>.png|jpg`; includes the 38)

You don't need the images to use the skill. Every rule has been written out in the reference files. Use the images only to look at a pattern visually.

## What the set covers
- **Desktop SaaS**: CRMs and record tables, sales, marketing and SEO analytics, finance dashboards, recruiting/ATS, support inboxes, LLM-ops and dev tools (deployments, logs, DB monitoring, API testing), security scanners, workflow and agent builders, docs and help-center analytics, HR (time off, scheduling), healthcare, smart home, maps and logistics.
- **AI products**: chat assistants, agent consoles, AI search, voice dictation, text-to-speech studios, AI insights in hiring, AI-generated reports and code.
- **Mobile**: fintech (wallets, cards, savings goals, investing, crypto), health and fitness, habits and gamified learning, creator tools, podcast/music players, calendar and tasks, video editing, ride-hailing and delivery tracking, community and chat.
- **Flows**: signup and login, OTP, onboarding wizards, permissions, setup checklists, pricing and paywalls, checkout and withdrawals, review & send, celebrations.

## Exemplars by pattern
Paths are relative to the folders above. A `t` prefix means `thread_images/`.

| Pattern | Look at |
|---|---|
| App shell, nav grouped by job | `images/10` (Main / Create / Enhance), `images/14` (Build / Data / Monitor), `images/11` (counts + saved "Slipping deals" view), `images/08` (human help + account card), `t299` (Money / Workflows / Receivables / Admin) |
| Calm task app (greeting, grouping by time, inline add, detail panel, inbox) | `images/35`–`38` |
| Kanban with drag state | `images/01` |
| Tables (type-icon headers, strength chips, explicit empty values) | `images/12`, `images/11`, `images/25` |
| Bulk action bar, inline status editing | `t123` |
| Filters: readable pills, facets, logic explained | `images/11`, `images/21`, `t228`, `t255` |
| KPIs with context and verdicts | `images/16`, `images/33`, `t034`, `t043`, `t180`, `t198`, `t221`, `t262` |
| Charts: annotations, baselines, compare | `images/30`, `t115`, `t240`, `t242`, `t279`, `t298` |
| Data freshness and lag disclosure | `t047`, `t180`, `t186`, `t235` |
| Settings rows and "when it applies" copy | `images/19`, `t033`, `t068`, `t160` |
| Forms with sections, helper text, security note | `t099`, `t141`, `t295` |
| Modals (good footer layout, AI-detected fields) | `images/03` |
| Contextual login with reassurance | `images/29` |
| Signup with testimonial panel | `images/13`, `t219` |
| Onboarding: one question per screen, escape options | `t044`, `t050`, `t075`, `t192`, `t237` |
| Onboarding: learn by doing + verify | `t058`, `t095` |
| Expectations timeline | `t220` |
| Setup checklist with statuses | `t048`, `t064`, `t221` |
| Empty states with a single CTA | `t052`, `t213`, `t251`, `t282` |
| Workflow / agent builders (typed nodes, sentences, branches) | `images/14`, `images/24`, `t102`, `t127`, `t157`, `t176`, `t231` |
| AI transparency (changelog, next steps, why, warnings) | `images/24`, `images/21`, `t056`, `t105`, `t146`, `t084` |
| AI entry composer with suggestions | `t057`, `t163`, `t280`, `t282`, `t292` |
| Review before commit (money, sending, data shared) | `t038`, `t109`, `t238`, `images/22` |
| Destructive confirmation naming consequences | `t156` |
| Safety defaults and modes (test mode, stop if replies, paused until, live vs demo) | `images/22`, `images/32`, `t089`, `t289`, `t296` |
| Inbox and notifications in context | `images/38`, `t154`, `t204`, `t241` |
| Chat (unread pill, voice notes, reply quotes) | `images/05`, `images/09`, `t081` |
| Mobile home with labeled actions | `images/34`, `t185`, `t244`, `t307` |
| Speed dial and contextual popover | `images/23` |
| Player with elapsed and remaining time | `images/06` |
| Gamification (streak, loss state, leaderboard "You") | `images/15`, `t209`, `t277`, `t301` |
| Course path with locked and progress states | `images/26`, `t224`, `t309` |
| Pricing, trial and paywall honesty | `t059`, `t108`, `t257` |
| Tracking timeline and live ETA | `t270`, `t274`, `t175` |

## Flaws observed (kept as teaching examples)
- Delta colours inverted: `images/16` (bounce rate ▲ green), `images/20` (returns ▼ red).
- Placeholder-as-label, no show-password, re-enter password: `images/13`.
- Icon-only tab bar: `images/06`. Icon-only footer actions: `images/03`. Icon-only revoke: `images/19`.
- Duplicate labels ("Provider" ×2) and typo "firts": `images/17`.
- Copy contradicting layout ("OR SIGN IN WITH EMAIL" above the social buttons) and a grammar error: `images/29`.
- Identical KPI values (placeholder data) and the typo "periode": `images/32`.
- Low-contrast titles on dark cards and repeated descriptions: `images/04`.
- Mixed units in one leaderboard: `images/15`.
- Typos "Taks" (`images/24`), "Is you skin" / "No at all" (`images/18`), "Alergies" (`t304`).
