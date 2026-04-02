def priority_scheduling(processes):

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

        wt = start - arrival
        tat = finish - arrival

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "priority": priority,
            "waiting_time": wt,
            "turnaround_time": tat
        })

        timeline.append((pid, start, finish))
        time = finish

    return results, timeline
