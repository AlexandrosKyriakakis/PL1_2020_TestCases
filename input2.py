import random as rd
import numpy as np
All = np.arange(0,1000001,1)

def createEdges (N, file):
    AllNodes = np.arange(N)

    unUsed =  AllNodes[:]
    unUsed = sorted(unUsed, key=lambda k: rd.random())
    used = []
    used.append(unUsed.pop())
    while (unUsed != []):
        poped = unUsed.pop()
        print (rd.choice(used) + 1, poped + 1, file = file)
        used.append(poped)
    print (rd.choice(used) + 1, rd.choice(used) + 1, file = file)

for t_i in range(10):
    file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputCoronaEDGE/coronainputEDGE{}.txt".format(t_i), mode = 'w+')
    print(10,file = file)
    for j in range(10):
        N = rd.choice(All)
        print(N,N, file = file)
        createEdges(N,file)
    file.close()  