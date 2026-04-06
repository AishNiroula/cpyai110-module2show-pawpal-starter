from pawpal_system import Task, Pet

def test_mark_complete():
    task = Task(name="Morning Walk", duration=30, priority="high", frequency="daily")
    assert task.completed == False
    task.mark_complete()
    assert task.completed == True

def test_add_task_increases_count():
    pet = Pet(name="Bella", species="Dog", age=3)
    assert len(pet.tasks) == 0
    task = Task(name="Feeding", duration=10, priority="high", frequency="daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1