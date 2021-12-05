import pprint

pp = pprint.PrettyPrinter()

with open("input", 'r') as f:
    coords = []
    test = []
    largest_x = 0
    largest_y = 0
    for line in f:
        split = line.split()
        
        coords.append(((x1 := int(split[0].split(",")[0]), y1 := int(split[0].split(",")[1])),
                        (x2 := int(split[2].split(",")[0]), y2 := int(split[2].split(",")[1]))))
        
        if x1 > largest_x: largest_x = x1
        if x2 > largest_x: largest_x = x2

        if y1 > largest_y: largest_y = y1
        if y2 > largest_y: largest_y = y2
        
    largest_x += 1
    largest_y += 1
    
    #pp.pprint(coords)
    #print(largest_x, largest_y)
        
    
    #init board
    board = []
    for i in range(0, largest_y):
        row = []
        board.append(row)
        for i in range(0, largest_x):
            row.append(0)

    #pp.pprint(board)

    #draw lines
    for coord in coords:
        #print("drawing: ", coord)
        c1, c2 = coord
        #print("drawing: ", c1, c2)
        x1, y1 = c1
        x2, y2 = c2
        #print("drawing: ", x1, y1, x2, y2)
        if x1 == x2:
            #print("x1 == x2")
            for y in range((y1 if y1<y2 else y2), (y2 if y1<y2 else y1)+1):
                #print("drawing: x1:", x1, "y", y)
                board[y][x1] += 1
        elif y1 == y2:
            #print("y1 == y2")
            #print("x1: ",x1," x2: ", x2)
            for x in range((x1 if x1<x2 else x2), (x2 if x1<x2 else x1)+1):
                #print("drawing: x:", x, "y1", y1)
                board[y1][x] += 1
        else:
            pass
            #print("unexpected input data: ", coord)
        #pp.pprint(board)
        #print()

    #count danger
    danger_count = 0
    for col in board:
        for cell in col:
            if cell > 1:
                danger_count+=1

    print("part1: ",danger_count)

with open("input", 'r') as f:
    coords = []
    test = []
    largest_x = 0
    largest_y = 0
    for line in f:
        split = line.split()
        
        coords.append(((x1 := int(split[0].split(",")[0]), y1 := int(split[0].split(",")[1])),
                        (x2 := int(split[2].split(",")[0]), y2 := int(split[2].split(",")[1]))))
        
        if x1 > largest_x: largest_x = x1
        if x2 > largest_x: largest_x = x2

        if y1 > largest_y: largest_y = y1
        if y2 > largest_y: largest_y = y2
        
    largest_x += 1
    largest_y += 1
    
    #pp.pprint(coords)
    #print(largest_x, largest_y)
        
    
    #init board
    board = []
    for i in range(0, largest_y):
        row = []
        board.append(row)
        for i in range(0, largest_x):
            row.append(0)

    #pp.pprint(board)

    #draw lines
    for coord in coords:
        #print("drawing: ", coord)
        c1, c2 = coord
        #print("drawing: ", c1, c2)
        x1, y1 = c1
        x2, y2 = c2
        #print("drawing: ", x1, y1, x2, y2)
        if x1 == x2:
            #print("x1 == x2")
            for y in range((y1 if y1<y2 else y2), (y2 if y1<y2 else y1)+1):
                #print("drawing: x1:", x1, "y", y)
                board[y][x1] += 1
        elif y1 == y2:
            #print("y1 == y2")
            #print("x1: ",x1," x2: ", x2)
            for x in range((x1 if x1<x2 else x2), (x2 if x1<x2 else x1)+1):
                #print("drawing: x:", x, "y1", y1)
                board[y1][x] += 1
        else:
            if y1 > y2:
                temp = x1
                x1 = x2
                x2 = temp

            if x1 > x2:
                xinc = -1
            else:
                xinc = +1
                
            for c, y in enumerate(range((y1 if y1<y2 else y2), (y2 if y1<y2 else y1)+1)):
                board[y][x1] += 1
                x1 += xinc
            #print("unexpected input data: ", coord)
        #pp.pprint(board)
        #print()

    #count danger
    danger_count = 0
    for col in board:
        for cell in col:
            if cell > 1:
                danger_count+=1

    print("part2: ",danger_count)