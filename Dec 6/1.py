from functools import reduce
with open("input.txt",'r') as f:
    inp = []
    for line in f.readlines():
        inp.append(line.strip().split())
    problems = list(map(list, zip(*inp)))
    total_sum_operations = 0
    
    for problem in problems:
        if problem[-1] == '+':
            total_sum_operations += reduce(lambda x,y : x + y, map(int,problem[:-1]))
        else:
            total_sum_operations += reduce(lambda x,y : x * y, map(int,problem[:-1]))

    print(total_sum_operations)