from dataclasses import dataclass, field
from typing import List

@dataclass
class Owner:
    name: str
    available_time: int  # in minutes

    def get_info(self):
        pass

@dataclass
class Pet:
    name: str
    species: str
    age: int

    def get_info(self):
        pass

class Task:
    name: str
    duration: int  # in minutes
    priority: str  # "high", "medium", "low"

    def get_details(self):
        pass

@dataclass
class Scheduler:
    tasks: List[Task] = field(default_factory=list)
    available_time: int = 0

    def add_task(self, task: Task):
        pass

    def generate_plan(self):
        pass

    def display_plan(self):
        pass