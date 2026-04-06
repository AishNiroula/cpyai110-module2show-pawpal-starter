from pawpal_system import Owner, Pet, Task, Scheduler

dog = Pet(name="Bella", species="Dog", age=3)
cat = Pet(name="Mochi", species="Cat", age=2)

dog.add_task(Task(name="Evening Walk", duration=30, priority="medium", frequency="daily", start_time="17:00"))
dog.add_task(Task(name="Feeding", duration=10, priority="high", frequency="daily", start_time="08:00"))
dog.add_task(Task(name="Grooming", duration=20, priority="low", frequency="weekly", start_time="11:00"))

cat.add_task(Task(name="Playtime", duration=15, priority="medium", frequency="daily", start_time="10:00"))
cat.add_task(Task(name="Litter Box Cleaning", duration=10, priority="high", frequency="daily", start_time="09:00"))

owner = Owner(name="Aishwarya", available_time=90, pets=[dog, cat])
scheduler = Scheduler(owner=owner)

print("=== Sorted by Time ===")
for t in scheduler.sort_by_time():
    print(f"  {t.start_time} - {t.name}")

print("\n=== Bella's Tasks ===")
for t in scheduler.filter_tasks_by_pet("Bella"):
    print(f"  {t.name}")

print("\n=== Pending Tasks ===")
for t in scheduler.filter_tasks_by_status(completed=False):
    print(f"  {t.name}")

print("\n=== Recurring Tasks (next 7 days) ===")
for t in scheduler.expand_recurring_tasks():
    print(f"  {t.name}")

print("\n=== Daily Plan ===")
scheduler.display_plan()