import heapq

cables = [4, 3, 2, 1]

# Non-optimal way
cost_non_optimal = 0
result = None
for cable in cables:
    if result is None:
        result = cable
        continue
    result = result + cable
    cost_non_optimal += result

print("Non-optimal cost:", cost_non_optimal)

# Optimal way
heapq.heapify(cables)
cost_optimal = 0
result = None
while cables:
    if result is None:
        result = heapq.heappop(cables)
    result = result + heapq.heappop(cables)
    cost_optimal += result

print("Optimal cost:", cost_optimal)
