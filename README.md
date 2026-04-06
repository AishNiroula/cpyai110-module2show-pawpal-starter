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
# 🐾 PawPal+

PawPal+ is a Streamlit app that helps a busy pet owner plan and manage daily care tasks for their pets. The app uses a smart scheduling system to prioritize, sort, and organize tasks based on available time and priority level.

---

## 🚀 Features

- **Owner & Pet Setup** — Enter your name, pet info, and how much time you have available today
- **Task Management** — Add care tasks with a name, duration, priority, frequency, and start time
- **Smart Sorting** — Tasks are automatically sorted chronologically by start time
- **Priority Scheduling** — The scheduler fits tasks into your day starting with the highest priority ones
- **Conflict Detection** — Get warned if two tasks are scheduled at the same start time
- **Recurring Tasks** — Daily and weekly tasks auto-generate the next occurrence when marked complete
- **Filtering** — View tasks by completion status (all, pending, or completed)
- **Daily Plan** — Generate a clean daily schedule that fits within your available time

---

## 📸 Demo

<a href="/course_images/ai110/pawpal_screenshot.png" target="_blank"><img src='/course_images/ai110/pawpal_screenshot.png' title='PawPal App' width='' alt='PawPal App' class='center-block' /></a>

---

##  Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

##  Testing PawPal+

To run the test suite:
```bash
python -m pytest
```

### What the tests cover
- Task completion and status updates
- Recurring daily and weekly task generation
- Non-recurring task handling
- Chronological sorting by start time
- Conflict detection for duplicate time slots
- Edge cases: empty pet list, over-scheduling, exact time fit

### Confidence Level:(4/5)

---

PawPal+ includes several intelligent scheduling features:

- **Sorting by time**: Tasks are sorted by start time so the daily plan flows chronologically
- **Filtering**: Tasks can be filtered by pet name or completion status
- **Recurring tasks**: Completing a daily or weekly task auto-creates the next occurrence using Python's timedelta
- **Conflict detection**: The scheduler warns if two tasks share the same start time

---

## Project Structure

- `app.py` — Streamlit UI
- `pawpal_system.py` — Backend logic (Task, Pet, Owner, Scheduler)
- `main.py` — CLI demo script
- `tests/test_pawpal.py` — Automated test suite
- `uml_final.png` — Final UML class diagram
- `reflection.md` — Project reflection and design notes