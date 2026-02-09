# Changelog

## 2026-02-09 — Extended for Ultra Plan

### Files Added
1. **stories.md** — 6 behavioral stories in STAR format
   - Indexing Pipeline (20 min → 1 sec)
   - Workday Integration (700+ records)
   - Image Dedup Pipeline (92% cache hit)
   - IoT Form Redesign (zero invalid submissions)
   - AI-Assisted MVC Refactor (15 templates → 1)
   - The Showing-Up Story (resilience)

2. **contacts.md** — Networking contact CRM
   - Active Contacts table
   - Target Company Contacts (for Phase 4 referrals)
   - Run Club Network tracking
   - 48-hour follow-up rule

3. **applications.md** — Application pipeline tracker
   - Application Status table
   - Target Companies by tier (1-4)
   - Interview Pipeline tracking
   - Offer Tracking + negotiation rules

### Commands Added
- `story <name>` — Display story for rehearsal, mark as practiced
- `network add <name> <company> <context>` — Add new contact
- `network next` — Show contacts who need follow-up
- `network search <company>` — Find contacts at specific company
- `apply <company>` — Log application (Phase 4+)
- `interview <company> <stage>` — Log interview
- `offer <company>` — Log offer
- `pipeline` — Show application status summary

### Why These Changes
The Ultra Plan requires:
- Behavioral prep (Phase 3): 6 STAR stories rehearsed
- Networking as application pipeline: Track every contact systematically
- Referral-based applications (Phase 4): No cold applications, need CRM
- Competing offers strategy: Track applications/interviews/offers to manage timelines

These additions turn `plan-my-year` into a complete FAANG job search system.

---

## Usage Notes

### Phase 1-2 (Now - Mar 21)
- **Focus:** DSA + System Design prep
- **Use:** Weekly planning, progress tracking, fitness/weight tracking
- **Network commands:** Track meetup contacts, log coffee chats
- **Do NOT use:** Application commands (you're not ready yet)

### Phase 3 (Mar 22 - Apr 11)
- **Focus:** Behavioral prep + Mock interviews
- **Use:** `story <name>` command to rehearse 2 stories/week
- **Network:** Deepen connections, identify referral contacts
- **Prepare:** Applications.md ready for Phase 4

### Phase 4 (Apr 14-18)
- **Focus:** Application blitz
- **Use:** `apply`, `network next`, `pipeline` commands
- **Goal:** Apply to 10-15 companies simultaneously with referrals
- **Strategy:** Generate competing offers for leverage

### Phase 5+ (Apr 21 - June)
- **Focus:** Interview gauntlet + offers
- **Use:** `interview`, `offer`, `pipeline` commands
- **Track:** Interview prep, offer deadlines, negotiation leverage

---

## What NOT to Build

Do NOT add:
- ❌ Automation (auto-send messages, auto-apply)
- ❌ AI agents (you have enough tools)
- ❌ Complex integrations (LinkedIn API, etc.)
- ❌ New features before Phase 4

The system is complete. Execute the plan.

---

## Related Workflows

**agentic-job-search** (archived until Phase 4):
- Generates ATS-optimized resume variants
- Creates outreach messages (recruiter, hiring manager, referral)
- Useful for cold/semi-warm applications
- DO NOT iterate on this tool now

**Current focus:**
- Structy: 11/114 done, 103 remaining
- This week target: 25 problems (Week 2: Feb 9-15)
- OpenClaw hackathon: Feb 13-14 (relationships > winning)

Get back to the weapon. The tools are ready.
