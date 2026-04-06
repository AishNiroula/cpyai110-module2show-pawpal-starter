# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
## Smarter Scheduling

PawPal+ includes several intelligent scheduling features:

- **Sorting by time**: Tasks are sorted by their start time (HH:MM) so the daily plan flows chronologically.
- **Filtering**: Tasks can be filtered by pet name or completion status to give targeted views of the schedule.
- **Recurring tasks**: When a daily or weekly task is marked complete, a new instance is automatically created for the next occurrence using Python's timedelta.
- **Conflict detection**: The scheduler warns the user if two tasks are scheduled at the same start time, preventing accidental overlaps.

## Testing PawPal+

To run the test suite, use the following command in your terminal:
```bash
python -m pytest
```

### What the tests cover
- Task completion: verifies that marking a task complete updates its status
- Recurring tasks: confirms that daily and weekly tasks auto-generate the next occurrence
- Non-recurring tasks: ensures "as needed" tasks do not create new instances on completion
- Sorting: verifies tasks are returned in chronological order by start time
- Conflict detection: checks that two tasks at the same time trigger a warning
- Edge cases: empty pet list, over-scheduling, and exact time fit

### Confidence Level: (4/5)
The core scheduling behaviors are well tested and all 10 tests pass. I would give it a full 5 stars with more time to test overlapping durations and invalid input handling.