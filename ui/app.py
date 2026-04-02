import sys
import os

# 🔥 Ensure project root is added (robust for Streamlit Cloud)
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


# ===== HEADER =====
st.title("💻 CPU Scheduling Visualizer")
st.markdown("Interactive simulation of Operating System scheduling algorithms")

st.divider()

# ===== INPUT =====
num_processes = st.number_input("Number of Processes", 1, 10, 3)

processes = []

st.subheader("📝 Enter Process Details")

for i in range(num_processes):
    pid = f"P{i+1}"

    col1, col2, col3 = st.columns(3)

    with col1:
        arrival = st.number_input(f"{pid} Arrival", min_value=0, key=f"a{i}")
    with col2:
        burst = st.number_input(f"{pid} Burst", min_value=1, key=f"b{i}")
    with col3:
        priority = st.number_input(f"{pid} Priority", min_value=1, key=f"p{i}")

    processes.append({
        "pid": pid,
        "arrival": arrival,
        "burst": burst,
        "priority": priority
    })

st.divider()

# ===== ALGORITHM =====
algorithm = st.selectbox(
    "⚙️ Select Algorithm",
    ["FCFS", "SJF", "Priority", "Round Robin"]
)

# ===== EXPLANATION =====
if algorithm == "FCFS":
    st.info("FCFS executes processes in order of arrival.")

elif algorithm == "SJF":
    st.info("SJF executes the shortest job first.")

elif algorithm == "Priority":
    st.info("Priority scheduling executes highest priority first.")

elif algorithm == "Round Robin":
    st.info("Round Robin gives equal CPU time to all processes.")

time_quantum = 2
if algorithm == "Round Robin":
    time_quantum = st.number_input("Time Quantum", min_value=1, value=2)

st.divider()

# ===== RUN =====
if st.button("▶️ Run Scheduling"):

    if algorithm == "FCFS":
        results, timeline = fcfs_scheduling(processes)

    elif algorithm == "SJF":
        results, timeline = sjf_scheduling(processes)

    elif algorithm == "Priority":
        results, timeline = priority_scheduling(processes)

    elif algorithm == "Round Robin":
        results, timeline = round_robin_scheduling(processes, time_quantum)

    # ===== RESULTS =====
    df = pd.DataFrame(results)
    st.dataframe(df, use_container_width=True)

    avg_wait = df["waiting_time"].mean()
    avg_tat = df["turnaround_time"].mean()

    col1, col2 = st.columns(2)
    col1.metric("Avg Waiting Time", round(avg_wait, 2))
    col2.metric("Avg Turnaround Time", round(avg_tat, 2))

    st.divider()

    # ===== GANTT CHART =====
    st.subheader("📈 Gantt Chart")
    draw_gantt_chart(timeline, f"{algorithm} Scheduling")
