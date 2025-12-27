t = int(input())  # number of test cases

for _ in range(t):
    G, P = map(int, input().split())
    n = int(input())

    problem1 = 0
    problem2 = 0

    for _ in range(n):
        a, b = map(int, input().split())
        problem1 += a
        problem2 += b

    cost_option1 = problem1 * G + problem2 * P
    cost_option2 = problem1 * P + problem2 * G

    print(min(cost_option1, cost_option2))
