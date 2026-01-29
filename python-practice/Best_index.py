import math

# Input
n = int(input())
arr = list(map(int, input().split()))

# Prefix sum
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

max_special_sum = float('-inf')

# For each index
for i in range(n):
    remaining = n - i

    # Find maximum k such that k*(k+1)//2 <= remaining
    k = int((math.sqrt(1 + 8 * remaining) - 1) // 2)

    length = k * (k + 1) // 2

    special_sum = prefix[i + length] - prefix[i]
    max_special_sum = max(max_special_sum, special_sum)

print(max_special_sum)
