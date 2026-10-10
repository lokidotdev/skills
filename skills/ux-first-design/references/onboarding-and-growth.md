# Onboarding, Activation and Growth UX

Use this for signup and login, onboarding wizards, first-run and empty states, activation checklists, gamification, pricing, paywalls, trials and referrals. The aim is to get people to their first real outcome quickly, and to be honest about everything else.

## Contents
1. Signup and login
2. Onboarding questions
3. Setup and verification steps
4. Empty states and first run
5. Activation: checklists, templates, education
6. Motivation and gamification
7. Pricing, plans, trials and paywalls
8. Referrals and sharing
9. Celebrations and success moments

---

## 1. Signup and login
- **Keep the context** of why they're signing up. A contextual login modal that says "You're applying to Senior Lifecycle Manager · Hybrid · $85K–$110K" converts better than a generic wall, and the background stays dimmed but visible.
- **Put the trust panel beside the form**: a testimonial (avatar, quote, name, role) or a social-proof line ("Join 3,500+ brands…").
- **SSO first** when the audience has it ("Continue with Apple / Google / LinkedIn"), then a divider whose copy matches what follows, then the email form.
- The form itself:
  - labeled fields
  - a password show/hide eye
  - "Forgot password?" next to the Password label
  - "Keep me signed in"
  - CTA disabled only while the missing piece is obvious
  - legal microcopy with links under the CTA ("By continuing you agree to the Terms and Privacy Policy")
  - a "Sign up" / "Log in" switch link
- **Verification**: "We've sent a 6-digit code to hello@company.com" + OTP boxes + "Resend in 0:44" + "Change email".
- Keep **Help** reachable on auth screens (a "? Help" pill in a corner).
- **Invite landing**: who invited you, to what, why it's useful, and when it expires ("Sophia invited you to Kargul Studio… This invite expires in 7 days").

---

## 2. Onboarding questions
- **Ask only what changes the experience**, and say so: "We'll use this to personalize your experience." Drop or postpone everything else.
- **Name the steps** in a top stepper (Sign in · Permissions · Set-up · Learn) or use a progress bar. Say how long it takes ("Takes about 3 minutes", "Complete our 5-minute onboarding").
- **On mobile, one question per screen**: a big question title, option cards with an icon and label, and a sticky CTA.
- **Option design**:
  - single choice → radio cards with a description each ("Find a job: a skill-matched feed backed by live company signals")
  - multi choice → chips with "Select all that apply" and a count on the CTA ("3 selected")
  - always include **"None of the above" / "No preference" / "Other"**
- **Conditional reveal**: answering "Yes, I have a registration number" reveals the field. "No, I don't" stays a valid answer.
- **Reduce precision anxiety**: "Rough estimate", wheel pickers, ranges instead of exact numbers.
- **Reassuring answers inside the flow**: "Do I need experience? Every account starts at 0."
- **Skip for now** on every non-essential step, plus "You can change this later in Settings."
- **Reveal and explain recommendations**: "Based on your preferences, here are the agents we've selected for you", with a "Change" option on each item and a CTA that names the result ("Continue with this swarm").
- **Use the wait**: "Projecting your creator business…". A short, honest processing moment can build anticipation. Never fake a long delay.

---

## 3. Setup and verification steps
- **Set expectations on a timeline**: "Now: complete the 5-minute onboarding · Today: customize your strategy and go live · This week: watch the AI send texts and recover carts."
- **Explain permissions and privacy choices** with honest options ("Help improve Lemon: what we collect…" vs "Privacy mode"), and add "You can always change this later."
- **Learn by doing**: ask the user to try the core interaction in a realistic mock-up ("Hold Fn and try saying…" inside a Gmail or Slack mock), then verify it worked ("Does the button turn yellow while you press it? **No, change shortcut** / **Yes**"). That gives them a fix path immediately.
- **Connection or integration setup**: a card per method, each with a one-line explanation and its own action (Connection string · CLI · IDE extension · MCP server).
- **Prerequisites stated up front**, with copyable commands (copy buttons on every command).

---

## 4. Empty states and first run
An empty screen is the best onboarding surface you have. It has four parts:
1. **What this place is for**, framed as a benefit: "Streamline your outreach with workflows."
2. **How it works**, in one sentence: "Set up a workflow and new leads are added to your campaigns on a daily, weekly or monthly cadence."
3. **One primary action**: "Create workflow", "+ Add experience", "Upload image".
4. **An optional shortcut**: "Import from another platform", "Start with a template", "▶ How it works", sample data.

- Teach the input method in the empty state: "Speak or type to begin", "Press Fn to talk".
- Prefer an illustration or ghost preview (greyed-out sample charts or cards) over a big blank area.
- Zero numbers are honest. Pair them with the next action ("0 posts · Share your first post").

---

## 5. Activation: checklists, templates, education
- **A setup checklist** that persists in the sidebar or dashboard until it's done: "Let's set up your blog · 4/6 completed", "Workspace setup 2/4: complete these steps to get the most out of UniOps". Each step shows done ✓, in progress or todo, and a status line ("Frame.io is still missing a login").
- **Quick-create tiles** with purpose subtitles: "All boards: start a fresh project", "Shared: a ready-made project".
- **Templates** filtered by use case and by integration, with tabs (All / Yours / Your organization / For you). Each card shows its integration icons and a one-line purpose.
- **An education hub**: "Getting started", a video and article library with counts, "View tutorial" links inside builders, and "Watch the tutorial" in empty pages. Offer a human route as well ("Hire a professional", "Talk to an engineer").
- **Explainer cards** (▶ How it works) that can be dismissed and found again later.

---

## 6. Motivation and gamification
Gamification only works when it rewards progress toward the user's real goal.
- **Progress**: bars with milestone markers (7 / 14 / 30 days), "Day 8 of 14", "1 of 3 · 800 of 2,000 XP", progress rings with counts.
- **Streaks**: a week row with completed days filled, today highlighted and future days ghosted, plus stats ("Streak started Nov 15 · Record 11 days"). **Design the lost state** ("3-day streak lost", a greyed mascot) with an encouraging way back.
- **Tasks with rewards**: "Apply to 3 gigs · +20 XP", quests ("3-day streak · +5 points"), and onboarding tasks that pay out ("Add a contact · +5 points").
- **Tiers and badges**: Bronze / Silver / Gold with what's needed for the next one. Locked badges show 🔒 and the requirement; unlocked badges show the date.
- **Leaderboards**: the top 3 with medal colours, **the current user's row highlighted "(You)"** even when they're outside the top, and **one unit per board**. Don't mix XP and $.
- **A path view** for courses: connected nodes (✓ done, ▶ next, 🔒 locked) and tips ("Each lesson builds on the last").
- **Shareable achievements**: "Share your stats" with a preview card and theme choices.

---

## 7. Pricing, plans, trials and paywalls
- **Usage meters before limits**: "96 / 264 credits", "Seats used 16/50 · 25% of your Pro plan". Use warning colours as the limit gets close.
- **The upgrade card says what you gain**: "Pro gives you faster workflows and higher limits", and urgency only when it's true ("$750 credit · 7 days left").
- **Trial banners** show the honest countdown and what happens when it ends: "Your trial ends in 4 days. Upgrade to keep premium features."
- **Plan cards**:
  - the current plan is marked and disabled ("Current plan", "Renews May 26, 2026")
  - "Most popular" on one plan only
  - feature lists show only the difference ("Everything in Pro, plus…")
  - a Monthly/Yearly toggle with the saving ("Save 30%")
  - "Contact sales" for Enterprise
  - a full comparison table below
- **Paywall copy**: the value headline ("Unlock more premium AI features"), the plan, the CTA ("Start 7-day free trial"), and **the exact terms under the CTA** ("7-day free trial, then $900/year ($75/month). No commitment. Cancel anytime."). Also Restore purchase, Terms and Privacy.
- **Cancellation**: offer Pause and Downgrade next to Cancel. Never confirmshame. One honest "Are you sure?" with what they lose is enough.
- **Price on the action** for one-off purchases ("Renew $249.90", "Promoted · ends in 9 days").

---

## 8. Referrals and sharing
- The referral link in a field with **Copy link** and **Share** buttons, the reward stated plainly ("Earn 10% of all fees…", "Earn $50 for every friend you invite"), stats tiles (referred users, earned, available to claim, plus a **Claim** action) and a referrals table.
- The share sheet offers a preview and the common targets (Email, Copy link, Slack, Notion, Figma…).

---

## 9. Celebrations and success moments
- Celebrate **real** milestones: subscription started, first workflow live, a streak continued, a goal reached.
- The pattern: a modal or bottom sheet over a dimmed background, an illustration or confetti (respecting reduced motion), a **specific headline** ("Your agents are live", "3 days strong!"), one line about what's next ("Your plan renews on December 9, 2025"), and **one CTA** ("Go to dashboard", "Keep going").
- Never celebrate trivial actions. Over-celebration trains people to ignore it (see `apple-design` §13, Utility).
