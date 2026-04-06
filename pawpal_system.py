from dataclasses import dataclass, field
from typing import List, Tuple
from datetime import datetime, timedelta

@dataclass
class Task:
    name: str
    duration: int        # in minutes
    priority: str        # "high", "medium", "low"
    frequency: str       # "daily", "weekly", "as needed"
    start_time: str = "09:00"  # HH:MM format
    completed: bool = False

    def get_details(self):
        """Returns a formatted string with task details and completion status."""
        status = "Done" if self.completed else "Pending"
        return f"{self.name} | {self.start_time} | {self.duration} min | Priority: {self.priority} | {status}"

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Adds a task to the pet's task list."""
        self.tasks.append(task)

    def get_info(self):
        """Returns a summary string of the pet's basic info and task count."""
        return f"{self.name} ({self.species}, age {self.age}) — {len(self.tasks)} tasks"


@dataclass
class Owner:
    name: str
    available_time: int  # in minutes
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Adds a pet to the owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Returns a flat list of all tasks across all of the owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def get_info(self):
        """Returns a summary of the owner's name, available time, and pet count."""
        return f"Owner: {self.name} | Available time: {self.available_time} min | Pets: {len(self.pets)}"


@dataclass
class Scheduler:
    owner: Owner

    def get_all_tasks(self) -> List[Task]:
        """Retrieves all tasks from the owner's pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self) -> List[Task]:
        """Sorts tasks by start_time in HH:MM format."""
        return sorted(self.get_all_tasks(), key=lambda t: datetime.strptime(t.start_time, "%H:%M"))

    def filter_tasks_by_pet(self, pet_name: str) -> List[Task]:
        """Returns tasks for a specific pet by name."""
        return [task for pet in self.owner.pets if pet.name == pet_name for task in pet.tasks]

    def filter_tasks_by_status(self, completed: bool) -> List[Task]:
        """Returns tasks filtered by completion status."""
        return [task for task in self.get_all_tasks() if task.completed == completed]

    def expand_recurring_tasks(self, days_ahead: int = 7) -> List[Task]:
        """Generates instances of recurring tasks for the next days_ahead days."""
        expanded = []
        today = datetime.now().date()
        for task in self.get_all_tasks():
            if task.frequency == "daily":
                for i in range(days_ahead):
                    due_date = today + timedelta(days=i)
                    expanded.append(Task(
                        name=f"{task.name} ({due_date})",
                        duration=task.duration,
                        priority=task.priority,
                        frequency=task.frequency,
                        start_time=task.start_time
                    ))
            elif task.frequency == "weekly":
                for i in range(0, days_ahead, 7):
                    due_date = today + timedelta(days=i)
                    expanded.append(Task(
                        name=f"{task.name} ({due_date})",
                        duration=task.duration,
                        priority=task.priority,
                        frequency=task.frequency,
                        start_time=task.start_time
                    ))
        return expanded

    def generate_plan(self) -> Tuple[List[Task], List[str]]:
        """Sorts tasks by priority and returns those that fit within available time, with conflict warnings."""
        priority_order = {"high": 1, "medium": 2, "low": 3}
        all_tasks = self.get_all_tasks()
        sorted_tasks = sorted(all_tasks, key=lambda t: (priority_order.get(t.priority, 4), t.duration))

        plan = []
        time_used = 0
        conflicts = []

        high_priority_time = sum(t.duration for t in all_tasks if t.priority == "high")
        if high_priority_time > self.owner.available_time:
            conflicts.append(f"High-priority tasks need {high_priority_time} min but only {self.owner.available_time} min available.")

        for task in sorted_tasks:
            if time_used + task.duration <= self.owner.available_time:
                plan.append(task)
                time_used += task.duration
            else:
                conflicts.append(f"'{task.name}' ({task.duration} min) could not fit — {time_used} min already used.")

        return plan, conflicts

    def display_plan(self):
        """Prints the generated daily plan and any conflicts to the terminal."""
        plan, conflicts = self.generate_plan()

        if conflicts:
            print("\nConflicts detected:")
            for c in conflicts:
                print(f"  ⚠️  {c}")

        if not plan:
            print("No tasks fit within the available time.")
            return

        print(f"\nDaily Plan for {self.owner.name}:")
        print(f"Available time: {self.owner.available_time} minutes\n")
        for i, task in enumerate(plan, 1):
            print(f"{i}. {task.get_details()}")