with open("input.txt",'r') as f:
    data = f.readlines()
    nums = data[:-1]
    ops = data[-1].strip().split()
    num_ops = len(ops)

    total_sum_operations = 0
    num_cols = max(len(row) for row in nums)

    col = 0
    for op in range(num_ops):
        operator = None
        result = None
        if ops[op] == '+':
            result = 0
            operator = lambda x, y: x + y
        elif ops[op] == '*':
            result = 1
            operator = lambda x, y: x * y
        else:
            assert False, "Invalid Operation"

        while col < num_cols and (s := "".join(["" if col >= len(row) else row[col] for row in nums]).strip()) != "":
            col += 1
            result = operator(result, int(s))
            
        total_sum_operations += result
        col += 1

    print(total_sum_operations)