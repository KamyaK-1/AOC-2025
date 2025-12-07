with open("input.txt","r") as f:
    grid = [line.strip() for line in f.readlines()]
    cols_covered = set([grid[0].index("S")])
    splits = 0
    for row in range(1, len(grid)):
        new_cols_covered = set()
        for col in cols_covered:
            if grid[row][col] == '^':
                new_cols_covered.add(col - 1)
                new_cols_covered.add(col + 1)
                splits += 1
            else:
                new_cols_covered.add(col)
        cols_covered = new_cols_covered
    print(splits)
    