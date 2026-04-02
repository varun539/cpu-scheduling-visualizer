def round_robin_scheduling(processes, time_quantum):
    from collections import deque

    # Sort by arrival
    processes = sorted(processes, key=lambda x: x["arrival"])

    n = len(processes)
    remaining = {p["pid"]: p["burst"] for p in processes}
    completion = {}

    timeline = []
    queue = deque()

    time = processes[0]["arrival"]
    i = 0

    # Add initial processes
    while i < n and processes[i]["arrival"] <= time:
        queue.append(processes[i])
        i += 1

    while queue:

        current = queue.popleft()
        pid = current["pid"]

        # Execute
        exec_time = min(time_quantum, remaining[pid])
        start = time
        time += exec_time
        remaining[pid] -= exec_time

        timeline.append((pid, start, time))

        # Add newly arrived processes FIRST
        while i < n and processes[i]["arrival"] <= time:
            queue.append(processes[i])
            i += 1

        # Then re-add current process if not finished
        if remaining[pid] > 0:
            queue.append(current)
        else:
            completion[pid] = time

        # If queue empty → jump to next arrival
        if not queue and i < n:
            time = processes[i]["arrival"]
            queue.append(processes[i])
            i += 1

    # Build results
    results = []

    for p in processes:
        pid = p["pid"]
        arrival = p["arrival"]
        burst = p["burst"]

        tat = completion[pid] - arrival
        wt = tat - burst

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "waiting_time": wt,
            "turnaround_time": tat
        })

    return results, timeline
