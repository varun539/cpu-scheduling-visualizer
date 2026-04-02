💻 CPU Scheduling Visualizer

An interactive web application that simulates and visualizes Operating System CPU scheduling algorithms.
This project helps users understand how different scheduling strategies affect process execution, waiting time, and system performance.

📌 Project Overview

In an operating system, multiple processes compete for CPU time. Efficient scheduling is essential to optimize performance and ensure fairness.

This project allows users to:

Input process details
Select scheduling algorithms
Analyze performance metrics
Visualize execution using Gantt charts
⚙️ Algorithms Implemented
🔹 First Come First Serve (FCFS)

Executes processes in the order they arrive.

🔹 Shortest Job First (SJF)

Executes the process with the smallest burst time first.

🔹 Priority Scheduling

Executes processes based on priority (lower value = higher priority).

🔹 Round Robin

Allocates equal CPU time slices using a time quantum.

📊 Features

✔ Interactive Streamlit UI
✔ Real-time scheduling simulation
✔ Average Waiting Time & Turnaround Time
✔ Gantt Chart Visualization
✔ Modular and clean code structure

🛠️ Technologies Used
Python
Streamlit
Pandas
Matplotlib
📂 Project Structure
cpu-scheduling-visualizer


│
├── algorithms/


│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   └── round_robin.py
│


├── visualization/
│   └── gantt_chart.py
│


├── ui/
│   └── app.py
│


├── requirements.txt
└── README.md


🚀 How to Run Locally

Clone the repository:

git clone YOUR_REPO_LINK
cd cpu-scheduling-visualizer

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run ui/app.py
🌐 Deployment

The application can be deployed using Streamlit Cloud for online access.

🎯 Problem Statement Alignment

This project aligns with Smart India Hackathon Problem Statement SIH25091 – AI-Based Timetable Generation System.

Both systems involve efficient scheduling and optimal allocation of limited resources, making CPU scheduling concepts directly applicable to timetable generation and resource management.

👥 Team Members
Varun B
Azim Sadath
Kirthick
🎓 Academic Purpose

This project was developed as part of an Operating Systems course to demonstrate scheduling concepts through practical implementation and visualization.
