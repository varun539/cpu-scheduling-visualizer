def priority_scheduling(processes):
    """
    Non-preemptive Priority Scheduling
    Lower number = higher priority
    """

    processes = sorted(processes, key=lambda x: (x["arrival"], x["priority"]))

    time = 0
    results = []
    timeline = []

    for p in processes:
        pid = p["pid"]
        arrival = p["arrival"]
        burst = p["burst"]
        priority = p["priority"]

        if time < arrival:
            time = arrival

        start = time
        finish = start + burst

        waiting_time = start - arrival
        turnaround_time = finish - arrival

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": priority,
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })

        timeline.append((pid, start, finish))
        time = finish

    return results, timeline
