# Read input
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_steps = -1

# Try all possible final values
for target in range(min(a) + 1):
    steps = 0
    possible = True

    for i in range(n):
        if a[i] < target:
            possible = False
            break

        diff = a[i] - target

        if b[i] == 0:
            if diff != 0:
                possible = False
                break
        else:
            if diff % b[i] != 0:
                possible = False
                break
            steps += diff // b[i]

    if possible:
        if min_steps == -1 or steps < min_steps:
            min_steps = steps

print(min_steps)
