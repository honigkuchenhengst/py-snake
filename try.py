import heapq

list = [3, 4, 6, 2, 5, 1]
queue = []
for i in range(len(list)):
    heapq.heappush(queue, list[i])

#for thing in range(len(queue)):
print(heapq.heappop(queue))


