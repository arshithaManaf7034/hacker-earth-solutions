import heapq

# Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Collect positives and negatives with indices
positives = []
negatives = []

for i in range(n):
    if arr[i] > 0:
        positives.append([i, arr[i]])
    elif arr[i] < 0:
        negatives.append([i, -arr[i]])  # store magnitude

# Min-heap for available positives (by index)
heap = []
p = 0
total_cost = 0

# Process negatives in increasing index order
for ni, need in negatives:

    # Add positives that are within right bound
    while p < len(positives) and positives[p][0] <= ni + k:
        heapq.heappush(heap, positives[p])
        p += 1

    # Remove positives that are too far left
    while heap and heap[0][0] < ni - k:
        idx, remaining = heapq.heappop(heap)
        total_cost += remaining

    # Try to cancel the negative
    while heap and need > 0:
        idx, available = heapq.heappop(heap)
        used = min(available, need)
        available -= used
        need -= used

        if available > 0:
            heapq.heappush(heap, [idx, available])

    # Remaining negative contributes to cost
    total_cost += need

# Add unused positives
while heap:
    idx, remaining = heapq.heappop(heap)
    total_cost += remaining

# Add positives that were never added to heap
while p < len(positives):
    total_cost += positives[p][1]
    p += 1

print(total_cost)
