with open("input.txt","r") as f:
    data = f.read().strip().split('\n')
    passwd = 0
    pos = 50
    for line in data:
        change = int(line[1:])
        if line[0] == 'R':
            pos = pos + change
            passwd += (pos // 100)
        else:
            if pos == 0:
                passwd += change // 100
                pos = pos - change
            else:    
                pos = pos - change
                passwd -= (pos - 1) // 100
        pos = pos % 100
    print(passwd)