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
        total_presents = sum(presents)
        area = rows * cols
        required_area = sum(presents[i] * sum(blocks[i][j].count('#') for j in range(3)) for i in range(len(presents)))
        if required_area > area:
            continue

        presents_filled_easily = (rows // 3) * (cols // 3)

        if presents_filled_easily >= total_presents:
            answer += 1
            continue    

        assert False, "Backtracking would be needed"
    
    print(answer)