from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import datetime, timedelta

# Tests cover: sorting, recurring tasks, conflict detection, edge cases

def test_mark_complete():
    """Task completion sets completed to True."""
    task = Task(name="Morning Walk", duration=30, priority="high", frequency="daily")
    assert task.completed == False
    task.mark_complete()
    assert task.completed == True

def test_add_task_increases_count():
    """Adding a task to a pet increases its task count."""
    pet = Pet(name="Bella", species="Dog", age=3)
    assert len(pet.tasks) == 0
    task = Task(name="Feeding", duration=10, priority="high", frequency="daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1

def test_sort_by_time():
    """Tasks are returned in chronological order by start time."""
    pet = Pet(name="Bella", species="Dog", age=3)
    pet.add_task(Task(name="Evening Walk", duration=30, priority="medium", frequency="daily", start_time="17:00"))
    pet.add_task(Task(name="Feeding", duration=10, priority="high", frequency="daily", start_time="08:00"))
    pet.add_task(Task(name="Playtime", duration=15, priority="medium", frequency="daily", start_time="10:00"))
    owner = Owner(name="Aishwarya", available_time=90, pets=[pet])
    scheduler = Scheduler(owner=owner)
    sorted_tasks = scheduler.sort_by_time()
    times = [t.start_time for t in sorted_tasks]
    assert times == sorted(times), "Tasks should be in chronological order"

def test_recurring_daily_task():
    """Completing a daily task creates a new task for the next day."""
    pet = Pet(name="Bella", species="Dog", age=3)
    task = Task(name="Feeding", duration=10, priority="high", frequency="daily")
    pet.add_task(task)
    pet.mark_task_complete("Feeding")
    assert len(pet.tasks) == 2, "A new task should be created for tomorrow"
    today = datetime.now().date()
    tomorrow = str(today + timedelta(days=1))
    assert pet.tasks[1].due_date == tomorrow, "New task should be due tomorrow"

def test_recurring_weekly_task():
    """Completing a weekly task creates a new task 7 days later."""
    pet = Pet(name="Bella", species="Dog", age=3)
    task = Task(name="Grooming", duration=20, priority="low", frequency="weekly")
    pet.add_task(task)
    pet.mark_task_complete("Grooming")
    assert len(pet.tasks) == 2
    today = datetime.now().date()
    next_week = str(today + timedelta(weeks=1))
    assert pet.tasks[1].due_date == next_week, "New task should be due next week"

def test_non_recurring_task():
    """Completing an 'as needed' task does not create a new task."""
    pet = Pet(name="Bella", species="Dog", age=3)
    task = Task(name="Vet Visit", duration=60, priority="high", frequency="as needed")
    pet.add_task(task)
    pet.mark_task_complete("Vet Visit")
    assert len(pet.tasks) == 1, "No new task should be created for non-recurring tasks"

def test_conflict_detection():
    """Two tasks at the same start time should trigger a conflict warning."""
    pet = Pet(name="Bella", species="Dog", age=3)
    pet.add_task(Task(name="Feeding", duration=10, priority="high", frequency="daily", start_time="08:00"))
    pet.add_task(Task(name="Morning Walk", duration=30, priority="medium", frequency="daily", start_time="08:00"))
    owner = Owner(name="Aishwarya", available_time=90, pets=[pet])
    scheduler = Scheduler(owner=owner)
    _, conflicts = scheduler.generate_plan()
    assert any("08:00" in c for c in conflicts), "Should detect conflict at 08:00"

def test_empty_pet_list():
    """Scheduler should return an empty plan when owner has no pets."""
    owner = Owner(name="Aishwarya", available_time=60, pets=[])
    scheduler = Scheduler(owner=owner)
    plan, conflicts = scheduler.generate_plan()
    assert plan == []
    assert conflicts == []

def test_over_scheduling():
    """Only tasks that fit within available time should be included."""
    pet = Pet(name="Bella", species="Dog", age=3)
    pet.add_task(Task(name="Walk", duration=50, priority="high", frequency="daily", start_time="08:00"))
    pet.add_task(Task(name="Feed", duration=50, priority="high", frequency="daily", start_time="09:00"))
    owner = Owner(name="Aishwarya", available_time=60, pets=[pet])
    scheduler = Scheduler(owner=owner)
    plan, conflicts = scheduler.generate_plan()
    assert len(plan) == 1, "Only one task should fit"
    assert len(conflicts) > 0, "Should report a conflict"

def test_exact_time_fit():
    """Tasks that exactly fill available time should all be included."""
    pet = Pet(name="Bella", species="Dog", age=3)
    pet.add_task(Task(name="Walk", duration=30, priority="high", frequency="daily", start_time="08:00"))
    pet.add_task(Task(name="Feed", duration=30, priority="high", frequency="daily", start_time="09:00"))
    owner = Owner(name="Aishwarya", available_time=60, pets=[pet])
    scheduler = Scheduler(owner=owner)
    plan, conflicts = scheduler.generate_plan()
    assert len(plan) == 2, "Both tasks should fit exactly"