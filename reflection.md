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

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
