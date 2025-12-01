with open("input.txt","r") as f:
    data = f.read().strip().split('\n')
    passwd = 0
    pos = 50
    for line in data:
        change = int(line[1:])
        if line[0] == 'R':
            pos += change
        else:
            pos -= change
        pos = pos % 100
        passwd += (pos == 0)
    print(passwd)