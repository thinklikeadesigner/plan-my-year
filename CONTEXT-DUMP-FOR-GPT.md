# Context Dump for ChatGPT — Goal Planning Engine

**Last updated:** February 11, 2026
**Current status:** Phase 1: Week 2 (Feb 9-15)

This document contains everything ChatGPT needs to understand and assist with the goal planning system.

---

## MISSION STATEMENT

Land a platform engineering role at a top-tier tech company by June 2026. 100% referral-based applications. Network IS the application pipeline.

**Current role:** Employed 9-5 as a platform engineer
**Constraints:** Tue/Wed office (2hr commute via 2-house system), Mon/Thu/Fri WFH
**Study budget:** 10-15 hrs/week core, up to 23 hrs with flex

---

## THE SYSTEM ARCHITECTURE

This is a **cascading time-horizon planning system** that breaks down yearly goals into actionable daily tasks through 6 levels:

1. **Year** → Define success criteria
2. **Quarterly** → Major milestones
3. **Monthly** → Concrete targets
4. **Weekly** → Task breakdown
5. **Daily** → Schedule integration
6. **Hourly** → Time-blocked templates

**Key principle:** Human-in-the-loop checkpoints. Agent must STOP after each level for user approval before continuing deeper.

---

## CURRENT STATE (as of Feb 11, 2026)

### Progress Summary

| Metric | Status |
|--------|--------|
| **Structy DSA** | 28/114 problems done (103 remaining) |
| **Current sections** | DP: 16/22, Stack: 6/7, Graph II: 0/16 |
| **DDIA** | Ch 1-2 done (audiobook), Ch 5 in progress |
| **Weight** | Start: 156.5 → Current: 156.1 → Target: 146.5 lbs |
| **Networking** | 5 active contacts, Amazon referral in progress |
| **Phase** | Phase 1: Finish the Weapon (Feb 8-28) |

### Active Week: Feb 9-15

**OpenClaw AI hackathon:** Fri Feb 13 12pm → Sat Feb 14 6pm (eats ~8 hrs study)

**Weekly targets:**
- Structy: 25 problems (DP finish, Stack finish, Graph II start)
- DDIA: Ch 5 (Replication)
- Networking: OpenClaw hackathon + follow-ups within 48hrs
- Fitness: 4 sessions (skipping Sat due to hackathon)
- Weight: 156.1 → 155.4 lbs

---

## THE 3 GOALS

### Goal 1: Land Big Tech Platform Engineer Role

**Target companies (tiered):**
- **Tier 1 (Dream):** Google Cloud/Infra, Meta Infrastructure
- **Tier 2 (Strong):** Amazon AWS/Platform, Microsoft Azure/Platform
- **Tier 3 (Strategic):** Snap, TikTok, Cloudflare, Datadog, Figma, Elastic
- **Tier 4 (Practice):** LinkedIn, Stripe, Uber, Indeed, Oracle Cloud

**Compensation targets:** $240-335K total comp (Google L4: $255-335K, Meta E4: $240-310K, Amazon SDE II: $190-250K, Microsoft L62: $205-275K)

**The 5 blockers to address:**
1. Resume is a black hole → 100% referral-based applications
2. Never done a mock interview → 8-10 mocks before first real interview
3. Behavioral stories unstructured → 6 STAR stories, rehearsed at 2 min each
4. Side quest trap → "Does this move me closer to a FAANG offer in 90 days?"
5. Undersold on compensation → Never anchor to current salary

**Phase timeline:**
- **Phase 1 (Feb 8-28):** Finish Structy (103 remaining), DDIA Ch 5-7, 2-3 hackathons
- **Phase 2 (Mar 1-21):** 18 system design problems, DDIA Ch 8-9
- **Phase 3 (Mar 22-Apr 11):** 6 STAR stories, 8-10 mock interviews
- **Phase 4 (Apr 14-18):** All targets simultaneously, referral-attached
- **Phase 5 (Apr 21-May 30):** Interview gauntlet (Tier 4 first for practice)
- **Phase 6 (May/June):** Negotiation with competing offers

### Goal 2: Lose 10 lbs + Build Fitness Habit

**Target:** 156.5 → 146.5 lbs (0.7 lbs/week, ETA mid-May)
**Tool:** MacroFactor app

**Fitness schedule:**
- Boulder/Lift: Thu, Sat (gym 35min away)
- Walk/Run: Tue, Wed, Fri (local)
- Rest: Sun

### Goal 3: Network as Application Pipeline

**Active contacts:**
- **Isha (Amazon):** Met at Women's SWE meetup, gave value first (run club invite), coffee late Feb, referral ask Week 8-9
- **Olivia Petrie (Elastic):** Program Manager DevRel, invited to present at Elastic Austin meetup
- **Sophia Solomon (Elastic):** Developer Advocate, workshop talk angle, meeting Feb 12 11:30am
- **Daniel (EPFL):** AI/ML engineer, met at Founders Run Club, registered for OpenClaw hackathon together
- **Ryan Will (Meta):** Data scientist (not eng), met at AI camp meetup

**Weekly non-negotiables:**
- 1 networking touchpoint (message, coffee, event)
- 1 LinkedIn post or engagement session

---

## BEHAVIORAL STORY BANK (6 STAR Stories)

All stories should be rehearsed out loud and timed at ~2 minutes.

1. **Indexing Pipeline** — 20 min → 1 sec via incremental indexing (Technical challenge, Deliver results)
2. **Workday Integration** — API-driven sync of 700+ records (Simplify, Bias for action)
3. **Image Dedup Pipeline** — Hash-based dedup, 92% skip rate, zero errors (Optimize, Highest standards)
4. **IoT Form Redesign** — DAG-modeled field dependencies, zero invalid submissions (Customer obsession, Think big)
5. **AI-Assisted MVC Refactor** — 15 templates → single MVC under 3-week deadline (Bias for action, Learn and be curious)
6. **The Showing-Up Story** — Breakup text → showed up → met Amazon engineer (Earn trust, Have backbone, Resilience)

**Rehearsal schedule:** Starting Phase 3 (Mar 22+), rehearse 2 stories per week.

---

## SUSTAINABILITY GUARDRAILS

1. **One true rest day per week** — Sunday evening, no study, no guilt
2. **Weekly review ritual** — 15-30 min Sunday evening
3. **Core vs Flex hour distinction** — Core hours non-negotiable, Flex is bonus
4. **Permission to adjust** — If interviews heat up, skip a meetup; if energy tanks, eat at maintenance
5. **Side quest filter** — "Does this move me closer to a FAANG offer in 90 days?" If no, write it in Post-FAANG Ideas doc

---

## FILE STRUCTURE

### Planning Files
- `2026-goals.md` — Year overview (mission, targets, constraints, success metrics)
- `q1-feb-mar.md` — Quarterly breakdown (Phases 1-3)
- `feb-2026.md` — Monthly targets (Structy sections, DDIA chapters, hackathons)
- `week-feb-9-15.md` — Weekly plan with daily checkboxes and time blocks

### Tracking Files
- `tracker.csv` — Daily progress log (structy_done, weight, fitness, networking, notes)
- `contacts.md` — Networking contacts (status, last touch, next action)
- `applications.md` — Application pipeline (not active until Phase 4)
- `stories.md` — 6 behavioral stories in STAR format with rehearsal tracking

### Templates
- `templates/{day}.md` — Hourly templates per day type (WFH-mon.md, Office-tue.md, etc.)

---

## COMMANDS AVAILABLE

### Planning Commands

**`next week`** — Generate next week's planning file
- Reads tracker.csv for current progress
- Reads current week file for structure
- Reads monthly file for targets
- Calculates remaining work and distributes across weeks
- Generates week-{start}-{end}.md with daily breakdown
- Presents for approval before saving

**`calendar`** — Generate .ics files for current week
- Reads current week file
- Reads day templates for schedule details
- Generates .ics events (fitness, study core/flex, kickoff, review)
- Saves to calendar/week-{dates}.ics

### Tracking Commands

**`log`** — Parse pasted messages and update tracker.csv
- User pastes Telegram/notes messages with timestamps
- Claude parses entries and shows what it understood
- Updates tracker.csv with new rows after confirmation

**`story <name>`** — Display behavioral story for rehearsal
- Reads stories.md
- Finds story by name (partial match OK)
- Displays full STAR format
- Prompts to say it out loud and time it (~2 min)
- Updates "Rehearsed" section with today's date if confirmed

### Networking Commands

**`network add <name> <company> <context>`** — Add new contact
- Prompts for role, source, status, notes
- Adds row to "Active Contacts" table in contacts.md

**`network next`** — Show contacts who need follow-up
- Parses "Last Touch" and "Next Action" fields
- Flags urgent contacts (>7 days, pending actions)
- Displays sorted by urgency

**`network search <company>`** — Find contacts at specific company
- Filters by company name (case-insensitive, partial match)

### Application Commands (Phase 4+)

**`apply <company>`** — Log new application to applications.md
**`interview <company> <stage>`** — Log interview in pipeline
**`offer <company>`** — Log offer and display negotiation reminders
**`pipeline`** — Show current application status summary

---

## NEGOTIATION PRINCIPLES

From `claude.md` — these are non-negotiable:

1. **Never accept on the spot** — ask for time to review
2. **Never give a number first** — ask for their range
3. **Always negotiate** — even if it's good
4. **Use competing offers as leverage**
5. **Your current salary is irrelevant**

**Comp script:** "I'm targeting market rate for SWE II platform roles in Austin. I'm flexible on the structure — I care about total comp and the opportunity."

---

## VERSION CONTROL RULE

After making any changes to project files (goals, plans, tracker, etc.):
1. `git add .`
2. `git commit -m "update"`
3. `git push`

This ensures all progress is backed up and synced.

---

## HOW TO USE THIS WITH CHATGPT

### As a planning assistant:
"I'm in Phase 1, Week 2 of a 6-month goal to land a Big Tech platform engineer role. Here's my current state: [paste tracker.csv latest row]. Can you help me adjust this week's plan based on the OpenClaw hackathon eating 8 hours of study time?"

### As a progress analyzer:
"Here's my tracker.csv. Am I on track to finish Structy by Feb 28? If not, what adjustments should I make?"

### As a networking coach:
"Here's my contacts.md. Who should I follow up with this week? Draft a message for Isha (Amazon) asking for coffee late Feb."

### As a story coach:
"Here's my Indexing Pipeline story. Time me at 2 minutes and give feedback on clarity, structure, and impact."

### As a job search strategist:
"I'm entering Phase 4 in 63 days. Review my networking contacts and tell me which target companies I still need referrals for, and how to prioritize filling those gaps."

---

## KEY INSIGHTS FROM CLAUDE.md

This system is designed around **human-in-the-loop checkpoints**. The agent should:
- STOP after each time horizon for approval
- NEVER skip ahead without user confirmation
- Incorporate feedback before moving to next level
- Use Core vs Flex distinction to prevent burnout
- Flag overcommitment during feasibility checks
- Include one true rest day per week

**Checkpoint rule:** After presenting each breakdown, STOP and wait for "yes", feedback, or questions.

**Hackathon rule:** Build, ship, leave, move on. No multi-day follow-on building. Every hackathon is a networking event that happens to have code.

---

## EXAMPLE INTERACTION FLOW

**User:** "I just finished 6 more Structy problems today. Update tracker and tell me if I'm on pace for this week's goal of 25."

**Expected response:**
1. Read tracker.csv
2. Calculate current pace (28 done + 6 = 34 done, need 36 by Sunday)
3. Show remaining problems needed
4. Suggest distribution across remaining days
5. Update tracker.csv with new entry
6. Commit and push changes

---

## CONSTRAINTS TO RESPECT

- **Employed 9-5** — Study happens outside work hours
- **Tue/Wed: In-office** — 2hr commute via 2-house system, limited study time
- **Mon/Thu/Fri: WFH** — Best study days
- **Study budget:** 10-15 hrs/week core (non-negotiable), up to 23 hrs with flex (optional)
- **Fitness:** 5x/week non-negotiable (Boulder/Lift Thu/Sat, Walk/Run Tue/Wed/Fri, Rest Sun)
- **Weight loss:** 0.7 lbs/week via MacroFactor tracking

---

## SUCCESS METRICS BY PHASE

### End of February (Phase 1)
- [ ] Structy: 114/114 complete
- [ ] 30-day challenge complete
- [ ] DDIA: Ch 5-7 read with notes
- [ ] 2-3 hackathons attended, 4+ new contacts
- [ ] LinkedIn carousel posted
- [ ] Amazon engineer relationship progressing

### End of March (Phase 2-3)
- [ ] 18 system design problems completed
- [ ] DDIA Ch 8-9 read
- [ ] 6+ mock interviews completed
- [ ] All 6 behavioral stories rehearsed and timed
- [ ] Second LinkedIn carousel posted
- [ ] At least 2 referral contacts identified at target companies

### Mid-April (Phase 4)
- [ ] Applications submitted to all target companies
- [ ] At least 3 applications have referral attached
- [ ] First phone screen scheduled

### End of May (Phase 5-6)
- [ ] At least one offer in hand
- [ ] Negotiation strategy prepared
- [ ] Decision made

---

## RESUME BULLETS (Platform Engineering Frame)

- Designed incremental indexing pipeline reducing reindex time from 20 min → 1 sec
- Built API integration layer consuming REST APIs, synchronizing 700+ employee records
- Engineered image sync pipeline: 750+ records/run, 92% cache hit via hash-based dedup, zero errors
- Implemented cache invalidation and purging strategies across multi-tenant production
- Designed constraint-based form system modeling field dependencies as DAG, eliminating 100% invalid submissions

---

## TOOLS & RESOURCES

- **DSA:** Structy.net (primary), NeetCode 150 (Phase 2+), 30-day Instagram challenge
- **System Design:** Educative.io Grokking, Alex Xu Vol 1, System Design Primer, DDIA
- **Mocks:** Pramp (free), Interviewing.io (paid)
- **Networking:** Founders Run Club, ATX Divas Run Club, Austin tech meetups, hackathons
- **Tracking:** MacroFactor (weight), tracker.csv (progress), contacts.md (networking)

---

## BACKUP SCENARIOS

**If FAANG doesn't work by June:**
- **Option A:** Tier 3 companies as primary (Cloudflare, Datadog, Figma, Stripe, Uber)
- **Option B:** Austin startup play (Series B+, $140-170K+, 10x ownership)
- **Option C:** Re-prep Q3/Q4 with real interview experience

**If offer is lukewarm:** Take it if comp is right. Leave in 18-24 months. Logo and salary are the point.

**If entrepreneurship pull gets strong:** Deal with yourself — build after 18 months at big tech. Salary funds runway, logo gives credibility, network gives co-founders.

---

## END OF CONTEXT DUMP

This document contains everything needed to understand the system, current state, and how to assist with goal planning, progress tracking, and job search strategy.

**Use this to:**
- Generate next week's plan
- Analyze progress and suggest adjustments
- Draft networking messages
- Review and time behavioral stories
- Calculate feasibility of targets
- Identify gaps in referral coverage
- Keep the plan on track without burnout
