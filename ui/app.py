import streamlit as st

st.title("💻 CPU Scheduling Visualizer")

st.markdown("Interactive simulation of CPU scheduling algorithms")

num_processes = st.number_input("Number of Processes", min_value=1, max_value=10, value=3)

st.subheader("Enter Process Details")

processes = []

for i in range(num_processes):
    pid = f"P{i+1}"
    arrival = st.number_input(f"{pid} Arrival Time", min_value=0, key=f"a{i}")
    burst = st.number_input(f"{pid} Burst Time", min_value=1, key=f"b{i}")
    priority = st.number_input(f"{pid} Priority", min_value=1, key=f"p{i}")

    processes.append({
        "pid": pid,
        "arrival": arrival,
        "burst": burst,
        "priority": priority
    })
