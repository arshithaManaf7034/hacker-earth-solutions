# Number of test cases
t = int(input())

for _ in range(t):
    # Read rows and columns
    r, c = map(int, input().split())

    # Read the grid
    grid = []
    for i in range(r):
        grid.append(input())

    max_border = 0

    # -------- Row-wise check --------
    for i in range(r):
        count = 0
        for j in range(c):
            if grid[i][j] == '#':
                count += 1
                if count > max_border:
                    max_border = count
            else:
                count = 0

    # -------- Column-wise check --------
    for j in range(c):
        count = 0
        for i in range(r):
            if grid[i][j] == '#':
                count += 1
                if count > max_border:
                    max_border = count
            else:
                count = 0

    # Print result for this test case
    print(max_border)
