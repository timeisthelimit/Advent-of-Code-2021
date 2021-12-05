def count_eps_gam(arr):
    epsilon = [0,0,0,0, 0,0,0,0, 0,0,0,0]
    gamma = [0,0,0,0, 0,0,0,0, 0,0,0,0]

    for line in arr:
        for count, n in enumerate(line):
            if n == '1':
                epsilon[count] += 1
                gamma[count] -= 1
            elif n == '0':
                epsilon[count] -= 1
                gamma[count] += 1

    for c, n in enumerate(epsilon):
        if n >= 0:
            epsilon[c] = 1
        else:
            epsilon[c] = 0

    for c, n in enumerate(gamma):
        if n > 0:
            gamma[c] = 1
        else:
            gamma[c] = 0

    return epsilon, gamma

with open("input", 'r') as f:
    epsilon = [0,0,0,0, 0,0,0,0, 0,0,0,0]
    gamma = [0,0,0,0, 0,0,0,0, 0,0,0,0]

    for line in f:
        for count, n in enumerate(line):
            if n == '1':
                epsilon[count] += 1
                gamma[count] -= 1
            elif n == '0':
                epsilon[count] -= 1
                gamma[count] += 1

    for c, n in enumerate(epsilon):
        if n > 0:
            epsilon[c] = 1
        else:
            epsilon[c] = 0

    for c, n in enumerate(gamma):
        if n > 0:
            gamma[c] = 1
        else:
            gamma[c] = 0

    epsi_dec = 0
    gamm_dec = 0

    for i in range(0, len(epsilon)):
        epsi_dec += (epsilon[i]*(2**(len(epsilon)-i-1)))

    for i in range(0, len(gamma)):
        gamm_dec += (gamma[i]*(2**(len(gamma)-i-1)))

    print("part 1: ", epsi_dec*gamm_dec)

with open("input", 'r') as f:

    inp = []
    for line in f:
        inp.append(line)

    oxygen = inp.copy()

    pos = 0
    while len(oxygen) > 1:
        eps, _ = count_eps_gam(oxygen)
        deletion_queue = []
        for c, i in enumerate(oxygen):
            if int(i[pos]) != eps[pos]:
                deletion_queue.append(c)
        
        for i in range(len(deletion_queue)-1, -1, -1):
            del oxygen[deletion_queue[i]]
        pos+=1

    co2 = inp.copy()

    pos = 0
    while len(co2) > 1:
        _, gam = count_eps_gam(co2)
        deletion_queue = []
        for c, i in enumerate(co2):
            if int(i[pos]) != gam[pos]:
                deletion_queue.append(c)
        
        for i in range(len(deletion_queue)-1, -1, -1):
            del co2[deletion_queue[i]]
        pos+=1
    
    oxygen = int(oxygen[0], 2)
    co2 = int(co2[0],2)

    print("part 2: ", oxygen*co2)

exit(0)
