with open("input", 'r') as f:
    crabs = f.readline().split(",")
    for c, i in enumerate(crabs):
        crabs[c] = int(i)

    shortest = 1000000
    shortest_pos = 0
    least_fuel = 10000000000
    for d in range(0, 1700):
        distance = 0
        for i in crabs:
            distance += abs(d - i)

        if distance < shortest:
            shortest = distance
            shortest_pos = d

    print("part 1:", least_fuel)
    print(shortest_pos)

with open("input", 'r') as f:
    crabs = f.readline().split(",")
    for c, i in enumerate(crabs):
        crabs[c] = int(i)

    least_fuel = 1000000000000
    for i in range (0, 1700):
        total_fuel = 0
        total_distance = 0
        for c in crabs:
            distance = abs(i-c)
            for x in range(0, distance+1):
                total_fuel += x

        if total_fuel < least_fuel:
            least_fuel = total_fuel
    
    print("part 2: ", least_fuel)

    