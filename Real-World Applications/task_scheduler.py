# Real-world use: Heap / Priority Queue → Server task scheduler

import heapq

tasks = []

heapq.heappush(tasks, (-2, "Send email"))
heapq.heappush(tasks, (-5, "Generate report"))
heapq.heappush(tasks, (-10, "Process payment"))
heapq.heappush(tasks, (-20, "Emergency task"))

priority, task = heapq.heappop(tasks)       # Here Python's heapq is a min-heap, so for a real scheduler we'd usually store priorities as negative numbers

print(task)  # Process payment