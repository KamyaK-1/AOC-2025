with open("input.txt","r") as f:
    grid = [line.strip() for line in f.readlines()]

    dp = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    dp[0][grid[0].index("S")] = 1

    for row in range(1, len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '^':
                dp[row][col - 1] += dp[row - 1][col]
                dp[row][col + 1] += dp[row - 1][col]
            else:
                dp[row][col] += dp[row - 1][col]

    print(sum(dp[-1]))