# Plan My Year

A Claude-powered goal planning system that breaks down yearly goals into actionable daily tasks with human-in-the-loop checkpoints.

## How It Works

1. Tell Claude your yearly goals
2. Claude breaks them down: **Year → Quarter → Month → Week → Day → Hour**
3. You approve/edit at each level before continuing
4. Claude generates markdown files and calendar exports

## Quick Start

```bash
cd plan-my-year
claude
```

Then tell Claude your goals, or use a command:

| Command | Description |
|---------|-------------|
| `next week` | Generate next week's plan from tracker progress |
| `calendar` | Generate .ics file for current week |
| `log` | Paste progress notes → update tracker.csv |

## File Structure

```
plan-my-year/
├── claude.md              # System prompt (planning engine)
├── README.md              # This file
├── tracker.csv            # Progress tracking
├── 2026-goals.md          # Year overview + quarterly breakdown
├── q1-feb-mar.md          # Q1 targets
├── feb-2026.md            # February monthly plan
├── week-feb-4-8.md        # Current week's daily plan
├── calendar/
│   └── week-feb-4-8.ics   # Calendar import file
└── templates/
    ├── monday.md
    ├── tuesday.md
    ├── wednesday.md
    ├── thursday.md
    ├── friday.md
    ├── saturday.md
    └── sunday.md
```

## Weekly Rhythm

| Day | Activity |
|-----|----------|
| **Sunday** | Weekly review → Update tracker.csv → Run `next week` → Run `calendar` → Import .ics |
| **Monday** | Weekly kickoff (10 min) → Commit to the week |
| **Tue-Sat** | Execute the plan |

## Logging Progress

Log to a private Telegram channel throughout the week:
```
10 structy done
sys design ch 2 finished
skipped gym, tired
weighed 155.2
```

On Sunday, copy messages and run `log` in Claude to update tracker.csv.

## Calendar Integration

After generating a week plan, run `calendar` to create an .ics file with:
- Wake up times
- Bedtime reminders (8hr sleep targets)
- Fitness blocks
- Study blocks (Core + Flex)
- Weekly kickoff & review

Import into Google Calendar by opening the .ics file or dragging it in.

## Customization

Edit `templates/` to adjust your daily schedules. Key variables:
- Wake/sleep times
- Work hours
- Commute patterns
- Gym days
- Core vs Flex study hours

## Philosophy

- **Human-in-the-loop**: Claude proposes, you approve
- **Core vs Flex hours**: Minimum commitment + optional stretch
- **Weekly review**: Adjust based on reality, not guilt
- **One rest day**: Sunday evening is protected
