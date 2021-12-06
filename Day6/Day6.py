with open("input", 'r') as f:
    fish = []
    for line in f:
        fish = line.split(",")
        
    for i in range(0, len(fish)):
        fish[i] = int(fish[i])

    for i in range(0, 80):
        for i, f in enumerate(fish):
            if fish[i] == 0:
                fish[i] = 7
                fish.append(9)
            fish[i] -= 1

    print("part 1: ",len(fish))

with open("input", 'r') as f:
    fish = []
    for line in f:
        fish = line.split(",")
        
    for i in range(0, len(fish)):
        fish[i] = int(fish[i])

    mega_fish = []
    for i in range(0,10):
        mega_fish.append(0)
    
    for i in fish:
        mega_fish[i] += 1

    for i in range(0, 256):
        mega_fish[7] += mega_fish[0]
        mega_fish[9] = mega_fish[0]

        mega_fish[0] = mega_fish[1]
        
        mega_fish[1] = mega_fish[2]
        mega_fish[2] = mega_fish[3]
        mega_fish[3] = mega_fish[4]
        mega_fish[4] = mega_fish[5]
        mega_fish[5] = mega_fish[6]
        mega_fish[6] = mega_fish[7]
        mega_fish[7] = mega_fish[8]
        mega_fish[8] = mega_fish[9]

    total_number = 0
    for i in mega_fish:
        total_number += i
    
    print("part 2: ", total_number-mega_fish[9])
    