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

print("=== Marking Tasks Complete ===")
dog.mark_task_complete("Feeding")
dog.mark_task_complete("Grooming")

print("\n=== Bella's Tasks After Completion ===")
for t in dog.tasks:
    print(f"  {t.name} | Due: {t.due_date} | {'Done' if t.completed else 'Pending'}")

print("\n=== Daily Plan ===")
scheduler.display_plan()