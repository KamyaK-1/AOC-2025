def remove_rolls(grid):
    num_accessible_rolls = 0
    positions_to_remove = []
    for row in range(1, len(grid) - 1):
        for col in range(1, n - 1):
            if grid[row][col] == '@':
                neighbor_roll_count = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if grid[row + dr][col + dc] == '@':
                            neighbor_roll_count += 1
                neighbor_roll_count -= 1 # Exclude the roll itself
                if neighbor_roll_count < 4:
                    num_accessible_rolls += 1
                    positions_to_remove.append((row, col))
    
    for row, col in positions_to_remove:
        grid[row][col] = '.'
    
    return num_accessible_rolls

with open("input.txt", "r") as file:
    grid = file.readlines()
    grid = [["."] + list(line.strip()) + ["."] for line in grid]
    n = len(grid[0])
    grid.append(["."] * n)
    grid.insert(0, ["."] * n)

    print(remove_rolls(grid))