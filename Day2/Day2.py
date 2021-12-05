with open("input", 'r') as f:
    h = 0
    v = 0
    while (line := f.readline()) != '':
        if line[0] == 'f':
            h += int(line.split()[1])
        elif line[0] == 'd':
            v += int(line.split()[1])
        elif line[0] == 'u':
            v -= int(line.split()[1])

    print (h*v)

with open("input", 'r') as f:
    h = 0
    v = 0

    aim = 0
    
    while (line := f.readline()) != '':
        if line[0] == 'f':
            h += int(line.split()[1])
            v += int(line.split()[1])*aim
        elif line[0] == 'd':
            aim += int(line.split()[1])
        elif line[0] == 'u':
            aim -= int(line.split()[1])

    print ("part 2: ", h*v)