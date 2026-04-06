from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    name: str
    duration: int
    priority: str
    frequency: str
    completed: bool = False

    def get_details(self):
        """Returns a formatted string with task details and completion status."""
        status = "Done" if self.completed else "Pending"
        return f"{self.name} | {self.duration} min | Priority: {self.priority} | {status}"

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
    available_time: int
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

    def generate_plan(self) -> List[Task]:
        """Sorts tasks by priority and returns those that fit within available time."""
        priority_order = {"high": 1, "medium": 2, "low": 3}
        all_tasks = self.get_all_tasks()
        sorted_tasks = sorted(all_tasks, key=lambda t: priority_order.get(t.priority, 4))

        plan = []
        time_used = 0
        for task in sorted_tasks:
            if time_used + task.duration <= self.owner.available_time:
                plan.append(task)
                time_used += task.duration

        return plan

    def display_plan(self):
        """Prints the generated daily plan to the terminal."""
        plan = self.generate_plan()
        if not plan:
            print("No tasks fit within the available time.")
            return
        print(f"\nDaily Plan for {self.owner.name}:")
        print(f"Available time: {self.owner.available_time} minutes\n")
        for i, task in enumerate(plan, 1):
            print(f"{i}. {task.get_details()}")