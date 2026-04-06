# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
There are four classes in my original UML design. The pet owner's name and available time in minutes are stored in the Owner class. The name, species, and age of the pet are stored in the Pet class. The name, priority level, and duration in minutes of a care job are stored in the job class. The Scheduler class is in charge of adding tasks, creating a daily schedule, and displaying that plan. It also maintains a list of tasks and the owner's available time.

**b. Design changes**
My design is yet to be changed since I am still at the early stages of planning. I will update this section as I implement the project.

Pet

Attributes: name, species, age
Methods: get_info()

Task

Attributes: name, duration, priority
Methods: get_details()

Scheduler

Attributes: tasks, available_time
Methods: add_task(task), generate_plan(), display_plan()

this is what copilot suggested 

"Summary Review of pawpal_system.py
Class Relationships:

Existing: Scheduler composes Task list; others are standalone.
Missing:
Owner should have pets: List[Pet] for ownership.
Task should reference a Pet (and possibly Owner) for assignment.
Scheduler should integrate with Owner (e.g., via constructor) to sync available_time and access pets.
Potential Logic Bottlenecks:

Scheduling may over-allocate time without validation.
Task.priority as string risks errors; use Enum.
No input validation in dataclasses (e.g., negative ages).
List-based storage could scale poorly for large task sets.
Methods are stubs; future implementations risk monolithic code.
Recommendations:

Add relationships for better cohesion.
Implement methods with constraints and helpers.
Use enums, validation, and tests to prevent issues."
---

## 2. Scheduling Logic and Tradeoffs
My scheduler considers two main constraints: available time and task priority. Available time limits how many tasks can fit into a single day — if the total duration of all tasks exceeds the owner's available time, lower priority tasks get dropped first. Priority determines the order tasks are scheduled, with high priority tasks always being scheduled before medium and low priority ones. I also added start time as a constraint for conflict detection, so two tasks cannot occupy the same time slot.
I decided that priority mattered most because a pet owner should always complete the most critical care tasks first, like feeding and medication, before optional ones like grooming or enrichment. Available time was the second most important constraint because no matter how high a task's priority is, it can only be scheduled if there is enough time in the day to complete it.

**b. Tradeoffs**
One tradeoff my scheduler makes is that conflict detection only checks for exact start time matches rather than checking if task durations overlap. For example, a 30-minute task at 08:00 and a 10-minute task at 08:20 would not be flagged even though they overlap. I kept this simpler approach because it is easier to understand and sufficient for a basic daily planner. Copilot suggested using a set instead of a dictionary for conflict detection, but I kept the dictionary version because it reports which specific tasks are conflicting by name, which is more useful to the user.

---

## 3. AI Collaboration

I used GitHub Copilot throughout this project in several ways. In the design phase I used Copilot Chat with #codebase to brainstorm my class structure and generate the initial UML diagram in Mermaid.js. During implementation I used Agent Mode to flesh out my class skeletons and Inline Chat to add docstrings. For testing I asked Copilot to suggest edge cases and generate test functions. The most helpful prompts were ones that referenced specific files using #file, because Copilot gave much more accurate suggestions when it could see my actual code.

**b. Judgment and verification**

One moment where I did not accept an AI suggestion as-is was during conflict detection. Copilot suggested using a set instead of a dictionary to track seen start times, which would have been simpler but would have lost the ability to report which specific tasks were conflicting by name. I kept the dictionary version because it gives the user more useful information. I verified this by running the app and confirming that the conflict warning correctly named both tasks.
---

## 4. Testing and Verification

**a. What you tested**

I tested ten behaviors in total. These included task completion status, adding tasks to a pet, chronological sorting by start time, daily and weekly recurring task generation, non-recurring task handling, time conflict detection, empty pet lists, over-scheduling, and exact time fits. These tests were important because they verified that the core scheduling logic works correctly before connecting it to the Streamlit UI. Without these tests I would not have been able to confidently say that the backend behaves as expected in both normal and edge case scenarios.

**b. Confidence**

- I am fairly confident the scheduler works correctly for typical use cases. All 10 tests pass and the app behaves as expected in the browser. I would give it a 4 out of 5. If I had more time I would test overlapping task durations where two tasks don't share an exact start time but their durations cause them to overlap, tasks with invalid priority values like "urgent", an owner with multiple pets where tasks compete for the same time slot, and what happens when available time is set to zero.
---

## 5. Reflection

I am most satisfied with how the scheduling logic came together. The scheduler correctly handles priority ordering, time constraints, recurring tasks, and conflict detection all in one clean method.h?

**b. What you would improve**

If I had another iteration I would improve the conflict detection to check for overlapping durations rather than just exact start time matches. I would also add a way for the user to mark tasks complete directly in the Streamlit UI.


**c. Key takeaway**

The most important thing I learned is that AI is a powerful tool but you still have to be the architect. Copilot could generate code quickly but it could not always tell whether a suggestion fit my specific design. I had to evaluate every suggestion, test it, and decide whether it made my system better or just more complex.
