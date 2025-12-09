import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(10**4)

def calculate_area(x1, x2, y1, y2):
    for row in range(min(x1, x2), max(x1, x2) + 1):
        for col in range(min(y1, y2), max(y1, y2) + 1):
            if grid[row][col] == '.':
                return 0
    length = abs(invMpX[x2] - invMpX[x1]) + 1
    width = abs(invMpY[y2] - invMpY[y1]) + 1
    return length * width

def dfs(i, j):
    if i < 0 or i > M1 or j < 0 or j > M2:
        return
    if grid[i][j] != '0':
        return
    grid[i][j] = '.'
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

x = []
y = []

with open("input.txt") as f:
    lines = f.readlines()
    points = [tuple(map(int, line.strip().split(","))) for line in lines]
    for point in points:
        x.append(point[0])
        y.append(point[1])

uniqueX = sorted(list(set(x)))
uniqueY = sorted(list(set(y)))

mpX = dict()
mpY = dict()
invMpX = dict()
invMpY = dict()
for i, val in enumerate(uniqueX):
    mpX[val] = i
    invMpX[i] = val
for i, val in enumerate(uniqueY):
    mpY[val] = i
    invMpY[i] = val

x = [mpX[val] for val in x]
y = [mpY[val] for val in y]
numPoints = len(x)

plt.plot(x, y, 'r-')
plt.savefig("shape.png")

M1 = max(x)
M2 = max(y)

grid = [['0' for _ in range(M2 + 1)] for _ in range(M1 + 1)]
for i in range(numPoints):
    for j in range(numPoints):
        if x[i] == x[j]:
            for col in range(min(y[i], y[j]), max(y[i], y[j]) + 1):
                grid[x[i]][col] = '#'
        if y[i] == y[j]:
            for row in range(min(x[i], x[j]), max(x[i], x[j]) + 1):
                grid[row][y[i]] = '#'


dfs(0,0)
dfs(0,M2)
dfs(M1,0)
dfs(M1,M2)

largest_area = 0

for i in range(numPoints):
    for j in range(i + 1, numPoints):
        x1, y1 = x[i], y[i]
        x2, y2 = x[j], y[j]
        area = calculate_area(x1, x2, y1, y2)
        largest_area = max(largest_area, area)

print(largest_area)

