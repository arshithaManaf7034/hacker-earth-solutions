n = int(input().strip())
arr = list(map(int, input().strip().split()))

if arr[-1] % 10 == 0:
    print("Yes")
else:
    print("No")
