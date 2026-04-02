def round_robin_scheduling(processes, time_quantum):
    from collections import deque

    processes = [p.copy() for p in processes]
    processes.sort(key=lambda x: x["arrival"])

    n = len(processes)
    time = 0
    i = 0

    queue = deque()

    remaining_time = {p["pid"]: p["burst"] for p in processes}
    completion_time = {}

    timeline = []

    # Start from first arrival
    time = processes[0]["arrival"]
    queue.append(processes[0])
    i = 1

    while queue:

        current = queue.popleft()

        pid = current["pid"]
        arrival = current["arrival"]

        # Execute
        exec_time = min(time_quantum, remaining_time[pid])
        start_time = time
        time += exec_time
        remaining_time[pid] -= exec_time

        timeline.append((pid, start_time, time))

        # 🔥 IMPORTANT: First re-add current if not finished
        if remaining_time[pid] > 0:
            queue.append(current)
        else:
            completion_time[pid] = time

        # 🔥 THEN add newly arrived processes
        while i < n and processes[i]["arrival"] <= time:
            queue.append(processes[i])
            i += 1

        # If queue empty, jump to next arrival
        if not queue and i < n:
            time = processes[i]["arrival"]
            queue.append(processes[i])
            i += 1

    # Results
    results = []

    for p in processes:
        pid = p["pid"]
        arrival = p["arrival"]
        burst = p["burst"]

        tat = completion_time[pid] - arrival
        wt = tat - burst

        results.append({
            "pid": pid,
            "arrival": arrival,
            "burst": burst,
            "waiting_time": wt,
            "turnaround_time": tat
        })

    return results, timeline
