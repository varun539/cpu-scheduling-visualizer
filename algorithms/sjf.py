def sjf_scheduling(processes):
    """
    Non-preemptive Shortest Job First Scheduling
    """

    processes = sorted(processes, key=lambda x: (x["arrival"], x["burst"]))

    current_time = 0
    completed = []
    timeline = []
    remaining = processes.copy()

    while remaining:

        available = [p for p in remaining if p["arrival"] <= current_time]

        if not available:
            current_time += 1
            continue

        shortest = min(available, key=lambda x: x["burst"])
        remaining.remove(shortest)

        pid = shortest["pid"]
        arrival = shortest["arrival"]
        burst = shortest["burst"]

        start_time = current_time
        finish_time = start_time + burst

        waiting_time = start_time - arrival
        turnaround_time = finish_time - arrival

        completed.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })

        timeline.append((pid, start_time, finish_time))

        current_time = finish_time

    return completed, timeline
