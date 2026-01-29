# Read input
n = int(input())
arr = list(map(int, input().split()))

MOD = 10**9 + 7

product = 1
for x in arr:
    product = (product * x) % MOD

print(product)
