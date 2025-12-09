with open("input.txt") as f:
    lines = f.readlines()
    
    points = [tuple(map(int, line.strip().split(","))) for line in lines]
    points.sort()
    
    xCoords = set(x for x, y in points)

    largest_area = 0
    
    minY = dict()
    maxY = dict()
    
    for x, y in points:
        if x not in minY:
            minY[x] = y
            maxY[x] = y
        else:
            minY[x] = min(minY[x], y)
            maxY[x] = max(maxY[x], y)

    for x1 in xCoords:
        for x2 in xCoords:
            length = abs(x2 - x1) + 1
            width1 = abs(maxY[x2] - minY[x1]) + 1
            width2 = abs(minY[x2] - maxY[x1]) + 1
            largest_area = max(largest_area, length * width1)
            largest_area = max(largest_area, length * width2)

    print(largest_area)