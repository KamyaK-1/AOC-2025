with open("input.txt","r") as f:
    data = f.read().strip().split('\n')
    passwd = 0
    curr = 50
    for line in data:
        change = int(line[1:])
        if line[0] == 'R':
            curr = curr + change
            passwd += (curr // 100)
        else:
            if curr == 0:
                passwd += change // 100
                curr = curr - change
            else:    
                curr = curr - change
                passwd -= (curr - 1) // 100
        curr = curr % 100
    print(passwd)