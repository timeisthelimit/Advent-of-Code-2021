with open("input", 'r') as f:
    last = f.readline()
    count = 0
    while (line := f.readline()) != '': 
        if line > last:
            count += 1

        print(last, line, count)
        print()
        last = line
    print("part 1: ", count)

with open("input.in", 'r') as f:
    count = 0
    a = f.readline()
    b = f.readline()
    c = f.readline()

    lastsum = int(a)+int(b)+int(c)

    while (line := f.readline()) != '': 

        a = b
        b = c
        c = line

        if (int(a)+int(b)+int(c)) > lastsum:
            count+=1

        lastsum = int(a)+int(b)+int(c)
    print("part 2: ", count)

