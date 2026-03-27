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
from algorithms.fcfs import fcfs_scheduling
from algorithms.sjf import sjf_scheduling
from algorithms.priority import priority_scheduling
from algorithms.round_robin import round_robin_scheduling

algorithm = st.selectbox(
    "Select Scheduling Algorithm",
    ["FCFS", "SJF", "Priority", "Round Robin"]
)

time_quantum = 2
if algorithm == "Round Robin":
    time_quantum = st.number_input("Time Quantum", min_value=1, value=2)

if st.button("Run Scheduling"):

    if algorithm == "FCFS":
        results, timeline = fcfs_scheduling(processes)

    elif algorithm == "SJF":
        results, timeline = sjf_scheduling(processes)

    elif algorithm == "Priority":
        results, timeline = priority_scheduling(processes)

    elif algorithm == "Round Robin":
        results, timeline = round_robin_scheduling(processes, time_quantum)

    st.write(results)
    import pandas as pd
from visualization.gantt_chart import draw_gantt_chart

    df = pd.DataFrame(results)
    st.dataframe(df)

    avg_wait = df["waiting_time"].mean()
    avg_tat = df["turnaround_time"].mean()

    st.metric("Average Waiting Time", round(avg_wait, 2))
    st.metric("Average Turnaround Time", round(avg_tat, 2))

    draw_gantt_chart(timeline, algorithm)
