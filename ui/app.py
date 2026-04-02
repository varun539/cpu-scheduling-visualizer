import sys
import os

# 🔥 Fix import path for Streamlit Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, project_root)

import streamlit as st
import pandas as pd

from algorithms.fcfs import fcfs_scheduling
from algorithms.sjf import sjf_scheduling
from algorithms.priority import priority_scheduling
from algorithms.round_robin import round_robin_scheduling
from visualization.gantt_chart import draw_gantt_chart


# ===== TITLE =====
st.title("💻 CPU Scheduling Visualizer")
st.markdown("Simulate CPU scheduling algorithms with performance metrics and Gantt chart")

st.divider()

# ===== INPUT =====
num_processes = st.number_input("Number of Processes", min_value=1, max_value=10, value=3)

processes = []

st.subheader("📝 Enter Process Details")

for i in range(num_processes):
    pid = f"P{i+1}"

    col1, col2 = st.columns(2)

    with col1:
        arrival = st.number_input(f"{pid} Arrival Time", min_value=0, key=f"a{i}")
    with col2:
        burst = st.number_input(f"{pid} Burst Time", min_value=1, key=f"b{i}")

    # Only show priority when needed
    if algorithm == "Priority":
        priority = st.number_input(f"{pid} Priority", min_value=1, key=f"p{i}")
    else:
        priority = 0  # default value

    processes.append({
        "pid": pid,
        "arrival": arrival,
        "burst": burst,
        "priority": priority
    })

st.divider()

# ===== ALGORITHM SELECT =====
algorithm = st.selectbox(
    "⚙️ Select Scheduling Algorithm",
    ["FCFS", "SJF", "Priority", "Round Robin"]
)

# ===== EXPLANATION =====
if algorithm == "FCFS":
    st.info("FCFS executes processes in the order they arrive.")

elif algorithm == "SJF":
    st.info("SJF selects the process with the smallest burst time.")

elif algorithm == "Priority":
    st.info("Priority scheduling executes higher priority processes first.")

elif algorithm == "Round Robin":
    st.info("Round Robin assigns fixed time slices to each process.")

# ===== TIME QUANTUM =====
time_quantum = 2
if algorithm == "Round Robin":
    time_quantum = st.number_input("Time Quantum", min_value=1, value=2)

st.divider()

# ===== RUN BUTTON =====
if st.button("▶️ Run Scheduling"):

    # Run selected algorithm
    if algorithm == "FCFS":
        results, timeline = fcfs_scheduling(processes)

    elif algorithm == "SJF":
        results, timeline = sjf_scheduling(processes)

    elif algorithm == "Priority":
        results, timeline = priority_scheduling(processes)

    elif algorithm == "Round Robin":
        results, timeline = round_robin_scheduling(processes, time_quantum)

    # ===== RESULTS TABLE =====
    st.subheader("📊 Results Table")

    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)

    # ===== METRICS =====
    avg_wait = df["waiting_time"].mean()
    avg_tat = df["turnaround_time"].mean()

    col1, col2 = st.columns(2)
    col1.metric("Average Waiting Time", round(avg_wait, 2))
    col2.metric("Average Turnaround Time", round(avg_tat, 2))

    st.divider()

    # ===== GANTT CHART =====
    st.subheader("📈 Gantt Chart Visualization")
    draw_gantt_chart(timeline, f"{algorithm} Scheduling")
