def solve (N, A):
    #def solve(N, A):
    total = sum(A)

    # Condition 1: total sum must be divisible by (N - 1)
    if total % (N - 1) != 0:
        return -1

    x = total // (N - 1)

    # Condition 2: no element can be greater than x
    if max(A) > x:
        return -1

    return x

    pass
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = solve(N, A)
    print (out_)
