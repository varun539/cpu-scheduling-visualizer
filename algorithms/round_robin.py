def round_robin_scheduling(processes, time_quantum):
    """
    Round Robin Scheduling Algorithm
    """

    from collections import deque

    # Copy processes to avoid modifying original
    processes = [p.copy() for p in processes]

    # Sort by arrival time
    processes.sort(key=lambda x: x["arrival"])

    queue = deque()
    time = 0
    i = 0

    n = len(processes)

    remaining_time = {p["pid"]: p["burst"] for p in processes}
    completion_time = {}

    timeline = []

    # Add first processes to queue
    while i < n and processes[i]["arrival"] <= time:
        queue.append(processes[i])
        i += 1

    if not queue:
        time = processes[0]["arrival"]
        queue.append(processes[0])
        i = 1

    while queue:

        current = queue.popleft()

        pid = current["pid"]
        arrival = current["arrival"]

        exec_time = min(time_quantum, remaining_time[pid])

        start_time = time
        time += exec_time
        remaining_time[pid] -= exec_time

        timeline.append((pid, start_time, time))

        # Add newly arrived processes
        while i < n and processes[i]["arrival"] <= time:
            queue.append(processes[i])
            i += 1

        # If process not finished, push back to queue
        if remaining_time[pid] > 0:
            queue.append(current)
        else:
            completion_time[pid] = time

    # Calculate results
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
