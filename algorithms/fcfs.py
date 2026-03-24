def fcfs_scheduling(processes):
    """
    First Come First Serve Scheduling Algorithm
    """

    processes = sorted(processes, key=lambda x: x["arrival"])

    current_time = 0
    results = []
    timeline = []

    for process in processes:

        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]

        if current_time < arrival:
            current_time = arrival

        start_time = current_time
        finish_time = start_time + burst

        waiting_time = start_time - arrival
        turnaround_time = finish_time - arrival

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })

        timeline.append((pid, start_time, finish_time))

        current_time = finish_time

    return results, timeline
