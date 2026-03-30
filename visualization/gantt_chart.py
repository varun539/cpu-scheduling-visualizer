
import matplotlib.pyplot as plt
import streamlit as st


def draw_gantt_chart(timeline, title="Gantt Chart"):

    fig, ax = plt.subplots()

    for pid, start, finish in timeline:
        ax.barh(pid, finish - start, left=start)

    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title(title)

    ax.grid(True, linestyle="--", alpha=0.5)

    st.pyplot(fig)
    plt.close(fig)
