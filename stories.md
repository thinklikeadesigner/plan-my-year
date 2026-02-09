# Behavioral Stories — STAR Format

Each story should be rehearsed out loud and timed at ~2 minutes. Track rehearsal dates in tracker.csv.

---

## Story 1: Indexing Pipeline

**Situation:**
Staff data was being fully reindexed on every request, creating 20-minute delays and blocking users from accessing updated information.

**Task:**
Design and implement incremental indexing to eliminate redundant work and move execution out of the request path.

**Action:**
- Analyzed the existing indexing workflow to identify bottlenecks
- Designed change detection mechanism to track which records actually changed
- Moved indexing execution out of the user request path into a background job
- Eliminated redundant computation by processing only delta changes
- Implemented zero-downtime migration strategy

**Result:**
Reindex time dropped from ~20 minutes to ~1 second. Zero downtime during migration. Users got immediate access to updated data. System became maintainable and scalable.

**Maps to:** Technical challenge, Deliver results, Dive deep

**Rehearsed:**
- [ ] Date: ___________

---

## Story 2: Workday Integration

**Situation:**
Employee data was scattered across Workday and proprietary systems with no single source of truth. Manual reconciliation was error-prone and time-consuming.

**Task:**
Build an integration layer to aggregate and synchronize 700+ employee records automatically.

**Action:**
- Designed API-driven sync layer consuming multiple REST APIs
- Built conflict resolution logic for data inconsistencies
- Implemented scheduled batch jobs for automated synchronization
- Added monitoring and alerting for sync failures
- Collaborated with stakeholders to define data ownership rules

**Result:**
Unified employee data across systems. Eliminated manual reconciliation work. 700+ records synchronized automatically with robust error handling.

**Maps to:** Simplify, Invent and simplify, Bias for action

**Rehearsed:**
- [ ] Date: ___________

---

## Story 3: Image Dedup Pipeline

**Situation:**
Image sync pipeline was re-downloading all assets on every run, wasting bandwidth, time, and server resources.

**Task:**
Build smart synchronization that skips unchanged assets while maintaining correctness and privacy requirements.

**Action:**
- Implemented hash-based deduplication to detect unchanged assets
- Designed privacy-aware caching strategy
- Built evaluation framework to process 750+ records per run
- Added comprehensive error handling and validation
- Monitored performance metrics to verify improvements

**Result:**
~92% of assets skipped via deduplication (cache hit rate). Zero errors across all production runs. Massive performance improvement. Privacy requirements maintained.

**Maps to:** Optimize, Insist on highest standards

**Rehearsed:**
- [ ] Date: ___________

---

## Story 4: IoT Form Redesign

**Situation:**
48-field IoT device intake form was generating invalid submissions. Researchers were entering inconsistent data based on complex field dependencies, causing downstream data quality issues.

**Task:**
Redesign form to make invalid states impossible while maintaining flexibility for different device types.

**Action:**
- Modeled field dependencies as a directed acyclic graph (DAG)
- Built reactive validation logic using control plane pattern
- Implemented progressive disclosure (show/hide fields based on selections)
- Collaborated with researchers to understand real-world usage patterns
- Designed constraint-based architecture that encoded business rules in code

**Result:**
Zero invalid submissions after deployment. Faster data collection. Researchers could move through form confidently. Data quality improved dramatically.

**Maps to:** Customer obsession, Think big, System design thinking

**Rehearsed:**
- [ ] Date: ___________

---

## Story 5: AI-Assisted MVC Refactor

**Situation:**
Procedural code was scattered across 15 templates. Any bug fix or feature change required hunting through all 15 files. Maintenance was becoming unsustainable. Deadline was 3 weeks.

**Task:**
Consolidate to single MVC architecture under tight deadline pressure.

**Action:**
- Used AI tooling (Claude/GPT) to accelerate code analysis and refactoring
- Made architectural decisions on MVC structure and separation of concerns
- Validated AI-generated output against requirements
- Iterated on design to ensure maintainability
- Tested thoroughly to prevent regressions

**Result:**
Shipped on time with single source of truth. Future feature velocity increased dramatically. Bug fixes now touch one place instead of 15. Demonstrated ability to leverage new tools under pressure.

**Maps to:** Bias for action, Learn and be curious, Innovation

**Rehearsed:**
- [ ] Date: ___________

---

## Story 6: The Showing-Up Story

**Situation:**
Received a breakup text right before a critical networking event (Women's Software Engineers meetup). Had to decide whether to go or stay home.

**Task:**
Show up despite emotional difficulty and make the event productive.

**Action:**
- Reframed emotionally: "This is data, not personal attack"
- Took care of basics: showered, got dressed, drove to event
- Showed up authentically but professionally
- Engaged genuinely in conversations despite internal state
- Gave value first (invited Amazon engineer to run club before any ask)

**Result:**
Met Amazon engineer who became a warm referral contact. Made multiple genuine connections that turned into job search leads. Proved to myself I could separate emotions from execution. Built confidence in resilience under pressure.

**Maps to:** Earn trust, Have backbone, Resilience, Grit

**Use carefully:** This is powerful but personal. Best for "tell me about a time you overcame adversity" or "describe a difficult situation." Don't lead with this. Save for behavioral rounds where vulnerability is appropriate.

**Rehearsed:**
- [ ] Date: ___________

---

## Rehearsal Instructions

### How to Practice
1. Set a timer for 2 minutes
2. Say the story OUT LOUD (not in your head)
3. Hit the key points: Situation, Task, Action, Result
4. Stop when timer goes off
5. Note what you forgot or where you rambled
6. Mark the date in tracker.csv when done

### Weekly Goal
Starting Phase 3 (Mar 22+): Rehearse 2 stories per week.

### Mock Interview Practice
Use these stories in your behavioral mock interviews. Get feedback on:
- Clarity and structure
- Did you ramble?
- Did you forget key details?
- Was the impact clear?
- Did you sound rehearsed or natural?
