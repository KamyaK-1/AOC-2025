with open("input.txt",'r') as f:
    lines = f.read().strip().split('\n\n')
    blocks = []
    for block in lines[:-1]:
        parts = block.split('\n')
        grid = parts[1:]
        blocks.append(grid)

    answer = 0
    puzzles = lines[-1].split('\n')
    for puzzle in puzzles:
        rows = int(puzzle.split('x')[0])
        cols = int(puzzle.split('x')[1].split(':')[0])
        presents = list(map(int,puzzle.split(':')[1].strip().split(' ')))
        area = rows * cols
        required_area = sum(presents[i] * sum(blocks[i][j].count('#') for j in range(3)) for i in range(len(presents)))
        answer += 1 if required_area <= area else 0
    
    # No reason for this to be the correct answer though it is
    print(answer)