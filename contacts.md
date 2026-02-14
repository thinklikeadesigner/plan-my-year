# Networking Contacts

Your network IS your application pipeline. Every person here is a potential referral, coffee chat, or warm intro to your target companies.

**Goal:** Track relationships, follow-ups, and next actions. Make networking systematic, not random.

---

## Active Contacts

| Name | Company | Role | Source | Status | Last Touch | Next Action | Notes |
|------|---------|------|--------|--------|------------|-------------|-------|
| Olivia Petrie | Elastic | Program Manager, DevRel | Elastic Austin meetup (Feb 3) | Active | Feb 12 call | Send talk outline by end of week | Invited to present at Elastic Austin meetup on search architecture. Workshop talk with Sophia went great. |
| Sophia Solomon | Elastic | Developer Advocate, Austin | Intro from Olivia (Feb 5) | Active | Feb 12 call | Send talk outline, follow up within 24hrs | Workshop call Feb 12 - connected over shared biochem → tech background. Talk about AI, life, career pivots. Great rapport. |
| Holt | Google | Developer Advocate | AI meetup (Feb) | Warm | Commented on course post | Second interaction by mid-March | Bridge node into Google. Gave A2A talk. Potential intro to platform engineer. Referral ask in April through intro request, not direct ask. |
| Isha | Amazon | SWE | Women's SWE meetup (Feb 6) | Warm | Feb 7 run club invite | Coffee late Feb, referral ask Week 8-9 | Gave value first with run club invite. Build relationship before ask. |
| Daniel | EPFL | AI/ML Engineer | Hackathon invite | Met Feb 7 | Feb 9 | Stay visible at run club | Registered for OpenClaw AI hackathon together  |
| Ryan Will | Meta | Data Scientist | AI camp meetup (Feb 4) | Met | Feb 4 | LinkedIn, stay in touch | Met at AI camp: Claude SDK + A2A protocol talks |
| Sophie | Recruiting | Recruiter | Previous contact | Ghosted | Resume submission | One polite follow-up, then move on | Went dark after resume. Not worth chasing. |
| Ion | Gamersplug | Founder | Moltathon Austin hackathon (Feb 14) | Met | Feb 14 | Follow up within 48hrs | Met at Moltathon hackathon |
| Josh | Skippy | Founder | Moltathon Austin hackathon (Feb 14) | Met | Feb 14 | Get contact info at Day 2, try Skippy beta | Local Mac-native AI assistant. Got beta .dmg airdropped. Not on LinkedIn. Hackathon continues Feb 15. |
| Jack Moffatt | Linkt AI | Co-founder & CTO | Moltathon Austin hackathon (Feb 14) | Met | Feb 14 | Follow up within 48hrs | |
| [Angel investor guy] | Natural Stacks | Angel Investor / Founder | Moltathon Austin hackathon (Feb 14) | Met | Feb 14 | Follow up if relevant | Writes sci-fi, owns Natural Stacks supplement company |

---

## Target Company Contacts (To Be Found)

These are referral contacts you need to identify for Phase 4 (Application Blitz, Apr 14-18).

| Company | Target Contact | Source | Status | Notes |
|---------|----------------|--------|--------|-------|
| Google | Holt (DevRel) | AI meetup (Feb) | In progress | Tier 1 - Dream. Bridge node. Target: second interaction mid-March, referral ask April via intro request to platform engineer. |
| Meta | Ryan Will? | AI camp meetup | Possible | Data scientist, not engineering. May not be strong referral. |
| Amazon | Isha | Women's SWE meetup | In progress | walk hike with whatsapp group possible. Referral ask Week 8-9. |
| Microsoft | Daniel Lam | Student Worker at TTI got return offer at microsoft | congratulated in linkedin comment section | Tier 2 - Strong |
| Snap | TBD | Need to find | Not started | Tier 3 - Strategic |
| TikTok | maybe james black | founders run club | went to barton springs on saturday feb 7 | Tier 3 - Strategic |
| Cloudflare | Ex's workplace | Personal | Possible | Know culture from dating someone there. Genuine fit. May be awkward to reach out. |
| Datadog | TBD | Need to find | Not started | Tier 3 - Strategic. Monitoring/observability = relevant to your work. |
| Elastic | Olivia Petrie, Sophia Solomon | Elastic Austin meetup | Active | Tier 3 - Strategic. Presenting at meetup Feb/Mar. Strong relationship via talk collaboration. |

---

## Run Club Network

Track people you meet at **Founders Run Club** and **ATX Divas Run Club**. These are consistent touchpoints.

| Name | Run Club | Met Date | Company | Notes |
|------|----------|----------|---------|-------|
| Daniel | Founders | Feb 7 | Mitre | AI/ML engineer |
| [Add more as you meet them] | | | | |

---

## Commands for Claude

Add these to `claude.md` to make contact management easy:

### `network add <name> <company> <context>`
Adds a new contact to the table.

**Example:**
```
> network add "Jane Doe" "Google" "Met at Founders Run Club Feb 7"
```

### `network next`
Shows who needs follow-up based on "Next Action" column and last touch date.

**Example output:**
```
Contacts to follow up with:

1. [Amazon engineer] - Last touch: Feb 7 (3 days ago)
   Next action: Coffee late Feb, referral ask Week 8-9

2. Armel Talla - Last touch: Feb 14 (1 day ago)
   Next action: Follow up within 48hrs (URGENT)

3. Figma production engineer - Last touch: Never
   Next action: SEND THE DRAFTED MESSAGE THIS WEEK
```

### `network search <company>`
Filters contacts by company.

**Example:**
```
> network search amazon

Found 1 contact at Amazon:
- [Amazon engineer]: Women's SWE meetup, status: Warm
  Next: Coffee late Feb, referral ask Week 8-9
```

---

## Networking Strategy

### Phase 1 (Feb 8-28): Build Relationships
- Attend 2-3 hackathons/meetups per month
- Give value first (run club invites, genuine conversations, not "hire me")
- Add every meaningful contact to this file within 24 hours
- Follow up within 48 hours after meeting someone

### Phase 2-3 (Mar 1 - Apr 11): Deepen Connections
- Coffee chats with warm contacts
- Identify referral contacts at target companies
- Stay visible at run clubs and events
- LinkedIn engagement with engineers at target companies

### Phase 4 (Apr 14-18): Activate Network
- Referral asks for all target companies
- "I'm starting to look at platform/infra roles. If you think it might be a fit, I'd love to learn about the referral process."
- Use contacts.md to track who you've asked, who said yes, who's pending

---

## Weekly Non-Negotiable

**1 networking touchpoint per week:**
- Coffee chat
- Meetup/hackathon
- LinkedIn message to new contact
- Follow-up message to existing contact

Log it in tracker.csv under `networking_touchpoints`.

---

## Notes

- **Status definitions:**
  - **Cold:** Never met, no context
  - **Met:** Single interaction, no follow-up
  - **Warm:** Multiple interactions or gave value first
  - **Active:** In conversation, working toward referral
  - **Referral:** They've submitted your resume

- **The 48-hour rule:** Follow up within 48 hours of meeting someone. LinkedIn connection + "great meeting you" message. Strike while memory is fresh.

- **Give value first:** Invite to run club, share a resource, make an intro. Don't lead with "I need a job." Build the relationship, then make the ask.

- **Quality over quantity:** 5 warm contacts at target companies > 50 cold LinkedIn connections.
