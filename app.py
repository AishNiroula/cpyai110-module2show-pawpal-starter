import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = None
if "scheduler" not in st.session_state:
    st.session_state.scheduler = None

st.title("🐾 PawPal+")
st.markdown("Welcome to PawPal+! Set up your profile, add tasks, and generate a daily care plan.")

st.divider()

st.subheader("1. Owner & Pet Info")
owner_name = st.text_input("Owner name", value="Aishwarya")
pet_name = st.text_input("Pet name", value="Bella")
species = st.selectbox("Species", ["dog", "cat", "other"])
available_time = st.number_input("Your available time today (minutes)", min_value=10, max_value=480, value=90)

if st.button("Set Up Owner & Pet"):
    pet = Pet(name=pet_name, species=species, age=0)
    owner = Owner(name=owner_name, available_time=int(available_time), pets=[pet])
    st.session_state.owner = owner
    st.session_state.scheduler = Scheduler(owner=owner)
    st.success(f"Profile created for {owner_name} with pet {pet_name}!")

st.divider()

st.subheader("2. Add Tasks")

if st.session_state.owner is None:
    st.info("Please set up your owner and pet profile first.")
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        task_name = st.text_input("Task name", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    frequency = st.selectbox("Frequency", ["daily", "weekly", "as needed"])

    if st.button("Add Task"):
        task = Task(name=task_name, duration=int(duration), priority=priority, frequency=frequency)
        st.session_state.owner.pets[0].add_task(task)
        st.success(f"Task '{task_name}' added!")

    all_tasks = st.session_state.owner.get_all_tasks()
    if all_tasks:
        st.write("Current tasks:")
        st.table([{"Task": t.name, "Duration": t.duration, "Priority": t.priority, "Status": "Done" if t.completed else "Pending"} for t in all_tasks])
    else:
        st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("3. Generate Daily Schedule")

if st.session_state.scheduler is None:
    st.info("Please set up your profile first.")
else:
    if st.button("Generate Schedule"):
        plan = st.session_state.scheduler.generate_plan()
        if not plan:
            st.warning("No tasks fit within your available time.")
        else:
            st.success(f"Here is {st.session_state.owner.name}'s plan for today!")
            for i, task in enumerate(plan, 1):
                st.markdown(f"**{i}. {task.name}** — {task.duration} min | Priority: {task.priority}")