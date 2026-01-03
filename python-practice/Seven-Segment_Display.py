sticks = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

t = int(input())

for _ in range(t):
    n = input().strip()
    total = 0

    for d in n:
        total += sticks[d]

    if total % 2 == 0:
        print("1" * (total // 2))
    else:
        print("7" + "1" * ((total - 3) // 2))
