def priority_scheduling(processes):
    """
    Non-preemptive Priority Scheduling
    Lower number = higher priority
    """

    processes = sorted(processes, key=lambda x: (x["arrival"], x["priority"]))

    current_time = 0
    completed = []
    timeline = []

    for process in processes:

        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]
        priority = process["priority"]

        if current_time < arrival:
            current_time = arrival

        start_time = current_time
        finish_time = start_time + burst

        waiting_time = start_time - arrival
        turnaround_time = finish_time - arrival

        completed.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": priority,
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })

        timeline.append((pid, start_time, finish_time))

        current_time = finish_time

    return completed, timeline
