import heapq

template = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Non-optimal way
cables = [*template]
cost_non_optimal = 0
result = None
for cable in cables:
    if result is None:
        result = cable
        continue
    result = result + cable
    cost_non_optimal += result
print("Non-optimal cost:", cost_non_optimal)

# Mid-optimal way
cables = [*template]
heapq.heapify(cables)
cost_optimal = 0
result = None
while cables:
    if result is None:
        result = heapq.heappop(cables)
    result = result + heapq.heappop(cables)
    cost_optimal += result
print("Mid-optimal cost:", cost_optimal)

# Most-optimal way 2
cables = [*template]
heapq.heapify(cables)
cost_optimal = 0
while len(cables) > 1:
    cable1 = heapq.heappop(cables)
    cable2 = heapq.heappop(cables)
    result = cable1 + cable2
    cost_optimal += result
    heapq.heappush(cables, result)
print("Most-optimal cost:", cost_optimal)
