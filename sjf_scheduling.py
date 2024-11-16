class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))

    time = 0
    completed_processes = []

    while processes:
        ready_queue = [p for p in processes if p.arrival_time <= time]

        if ready_queue:
            ready_queue.sort(key=lambda x: x.burst_time)
            current_process = ready_queue[0]
            processes.remove(current_process)

            time += current_process.burst_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time

            completed_processes.append(current_process)
        else:
            time += 1

    return completed_processes


n = int(input("Enter the number of processes: "))
processes = []

for i in range(n):
    print(f"\nProcess {i + 1}:")
    name =input("Enter process name: ")
    arrival_time = int(input("Enter arrival time: "))
    burst_time = int(input("Enter burst time: "))
    processes.append(Process(name, arrival_time, burst_time))

completed_processes = sjf_scheduling(processes)

print("\nProcess\t\tAT\tBT\tCT\tTT\tWT")
for p in completed_processes:
    print(f"{p.name}\t\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t{p.turnaround_time}\t{p.waiting_time}")

avg_tt = sum(p.turnaround_time for p in completed_processes) / len(completed_processes)
avg_wt = sum(p.waiting_time for p in completed_processes) / len(completed_processes)
print(f"\nAverage Turnaround Time (ATT): {avg_tt}")
print(f"Average Waiting Time (AWT): {avg_wt}")
