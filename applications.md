# Application Pipeline

**Strategy:** 100% referral-based applications. Zero portal submissions without a warm intro.

**Phase 4 Target:** Apply to all target companies simultaneously (Apr 14-18) to generate competing offers.

---

## Application Status

| Company | Tier | Role | Referral Contact | Applied Date | Status | Interview Stage | Next Step | Notes |
|---------|------|------|------------------|--------------|--------|-----------------|-----------|-------|
| *No applications yet* | | | | | | | | Phase 1-3: Prep mode. No applications until Apr 14. |

---

## Target Companies (Phase 4)

### Tier 1 — Dream (Referral Required)
| Company | Target Team | Referral Contact | Contact Status | Apply Date | Notes |
|---------|-------------|------------------|----------------|------------|-------|
| Google | Cloud/Infra or Platform | TBD | Need to find | Apr 14-18 | Comp: $255-335K total |
| Meta | Infrastructure or Internal Tools | Ryan Will (possible) | Met Feb 4 | Apr 14-18 | Comp: $240-310K total |

### Tier 2 — Strong (Referral or Warm Recruiter)
| Company | Target Team | Referral Contact | Contact Status | Apply Date | Notes |
|---------|-------------|------------------|----------------|------------|-------|
| Amazon | AWS or Internal Platform | [Amazon engineer] | Warm (in progress) | Apr 14-18 | Coffee chat late Feb. Referral ask Week 8-9. Comp: $190-250K total |
| Microsoft | Azure, Copilot, or Platform | Daniel Lam, TTI student worker | commented congrats on his new position at microsoft | Apr 14-18 | Comp: $205-275K total |

### Tier 3 — Strategic (Easier Interviews, Good Comp)
| Company | Target Team | Referral Contact | Contact Status | Apply Date | Notes |
|---------|-------------|------------------|----------------|------------|-------|
| Snap | Infra/Platform | TBD | Need to find | Apr 14-18 | Competitive comp with Tier 1-2 |
| TikTok | Infra/Platform | Maybe james black, he owns a marketing agency and i think he said he used to work at tiktok | met at founders run club, we hung out all day at barton springs along with harry forsyth and richard tran | Apr 14-18 | Pays aggressively |
| Cloudflare | Platform | Ex's workplace | Awkward but possible | Apr 14-18 | Know culture. Genuine good infra work. |
| Datadog | Monitoring/Observability | TBD | Need to find | Apr 14-18 | Directly relevant to your work |


### Tier 4 — Practice + Backup
| Company | Target Team | Referral Contact | Contact Status | Apply Date | Notes |
|---------|-------------|------------------|----------------|------------|-------|
| LinkedIn | Platform | TBD | Need to find | Apr 14-18 | Microsoft subsidiary, separate process |
| Stripe | Platform Eng | TBD | Need to find | Apr 14-18 | Good practice interviews |
| Uber | Platform/Infra | TBD | Need to find | Apr 14-18 | Austin presence |
| Indeed | Platform | TBD | Need to find | Apr 14-18 | Austin HQ, lower bar, good practice |
| Oracle Cloud | Platform | TBD | Need to find | Apr 14-18 | Austin, hiring aggressively |

---

## Interview Pipeline

When applications move forward, track interview stages here:

| Company | Stage | Date | Interviewer(s) | Focus | Prep Notes | Result |
|---------|-------|------|----------------|-------|------------|--------|
| *No interviews yet* | | | | | | |

**Interview stages:**
1. Recruiter screen (30 min)
2. Technical phone screen (45-60 min, 1-2 LC mediums)
3. Onsite/Virtual onsite (4-5 rounds: coding, system design, behavioral)
4. Offer / Final decision

---

## Application Checklist (Phase 4)

For each company, before applying:

- [ ] Referral contact identified and asked
- [ ] Resume variant generated (use agentic-job-search if needed)
- [ ] Outreach message sent to referral contact
- [ ] Portal application submitted (AFTER referral is in)
- [ ] Application logged in tracker.csv
- [ ] Follow-up scheduled (if no response in 1 week)

---

## Offer Tracking

When offers come in, track them here to manage negotiation and deadlines:

| Company | Offer Date | Base Salary | Stock/Year | Bonus | Total Comp | Deadline | Status | Notes |
|---------|------------|-------------|------------|-------|------------|----------|--------|-------|
| *No offers yet* | | | | | | | | Target: May/June |

**Negotiation rules:**
1. Never give a number first: "I'm targeting market rate for SWE II platform roles. What's the range?"
2. Never accept on the spot: "I'm excited. Can I have until [date] to review?"
3. Always negotiate: "The base is strong. Is there flexibility on equity?"
4. Use competing offers: "I have an offer from [company] at [X]. Can we close the gap?"
5. Your current salary is irrelevant: "I'd rather focus on market rate for this role."

---

## Commands for Claude

Add these to `claude.md`:

### `apply <company>`
Logs a new application.

**Example:**
```
> apply google

Company: google
Role: Software Engineer III, Core
Referral contact: [prompt for name]
Applied date: 2026-04-14
Status: applied
```

### `interview <company> <stage>`
Logs an interview.

**Example:**
```
> interview google recruiter_screen

Date: [prompt]
Interviewer: [prompt]
Focus: [prompt]
Result: [moved_forward / rejected / pending]
```

### `offer <company>`
Logs an offer.

**Example:**
```
> offer amazon

Base: 145000
Stock/year: 80000
Bonus: 20000
Total comp: 245000
Deadline: [prompt for date]
```

### `pipeline`
Shows current application status across all companies.

**Example output:**
```
Application Pipeline Summary:

Applied (3):
- Google: Recruiter screen scheduled Feb 20
- Meta: Waiting for response (applied Feb 15)
- Amazon: Referral submitted, not yet applied

Need Referral (5):
- Microsoft: No contact identified
- Snap: No contact identified
...

Interviews (1):
- Google: Recruiter screen on Feb 20

Offers (0):
- None yet
```

---

## Strategy Notes

### Application Timing (Critical)
Apply to all targets simultaneously in ONE WEEK (Apr 14-18). This ensures:
- Competing timelines
- Leverage in negotiation
- You're not stuck waiting months for slow companies while fast ones expire

### Interview Order
1. **Tier 4 first** (Indeed, Oracle) — Practice reps, low stakes
2. **Tier 3 next** (Snap, TikTok, Datadog) — Real offers + more practice
3. **Tier 1-2 last** (Google, Meta, Amazon, Microsoft) — You're sharp from previous rounds

If you get an offer early, use it to accelerate everywhere else:
"I have an offer with a deadline of [date]. Can we expedite the process?"

### Rejection Plan
- **First rejection:** Sting for 24 hours. Debrief. Adjust.
- **Second rejection:** Sting for 12 hours. You're getting data.
- **Third rejection:** Barely a bruise. You know the game now.

You need ONE yes. Not five. Every rejection gets you closer.

---

## Weekly Tracking

Starting Phase 4, log in tracker.csv:
- Applications submitted this week
- Interviews completed this week
- Offers received this week
- Networking touchpoints that led to referrals

---

## Notes

**Do NOT apply before Phase 4** unless:
- You have a warm referral ready NOW
- The role is actually open and hiring
- You can dedicate < 2 hours total
- You're not sacrificing DSA/system design prep time

The prep is the priority. Applications come after you're sharp.

**Cold applications are a waste:** Your resume says "Texas A&M Transportation Institute." ATS will deprioritize you. Referrals bypass this. 100% referral-based strategy is non-negotiable.

**Track everything:** Every application, every interview, every rejection, every offer. This data feeds your strategy adjustments and helps you learn the game.
