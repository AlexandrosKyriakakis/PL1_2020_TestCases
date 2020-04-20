import random as rd
import numpy as np
All = np.arange(3,1000001,1)

def createEdges (Start, N, file):
    AllNodes = np.arange(N)
    unUsed =  AllNodes[:]
    unUsed = sorted(unUsed, key=lambda k: rd.random())
    used = []
    used.append(unUsed.pop())
    while (unUsed != []):
        poped = unUsed.pop()
        used.append(poped)
        print (Start + rd.choice(used) + 1, Start + poped + 1, file = file)
    print (Start + rd.choice(used) + 1,Start + rd.choice(used) + 1, file = file)

def createNoEdges (Start, N, file):
    AllNodes = np.arange(N)

    unUsed =  AllNodes[:]
    unUsed = sorted(unUsed, key=lambda k: rd.random())
    used = []
    used.append(unUsed.pop())
    while (unUsed != []):
        poped = unUsed.pop()
        used.append(poped)
        print (Start + rd.choice(used) + 1, Start + poped + 1, file = file)

def create2Edges (Start, N, file):
    AllNodes = np.arange(N)

    unUsed =  AllNodes[:]
    unUsed = sorted(unUsed, key=lambda k: rd.random())
    used = []
    used.append(unUsed.pop())
    while (unUsed != []):
        poped = unUsed.pop()
        used.append(poped)
        print (Start + rd.choice(used) + 1, Start + poped + 1, file = file)
    print (Start + rd.choice(used) + 1,Start + rd.choice(used) + 1, file = file)
    print (Start + rd.choice(used) + 1,Start + rd.choice(used) + 1, file = file)

def createCycle (N, file):
    cycle = [(i,i+1) for i in np.arange(N-1)]
    cycle = sorted(cycle, key=lambda k: rd.random())
    print(1,N, file=file)
    for x,y in cycle:
        print (x+1, y+1, file=file)

def totalRandom (N, file):
    AllNodes = np.arange(N)
    for i in range(N):
        print (rd.choice(AllNodes) + 1,rd.choice(AllNodes) + 1, file = file)

"""
for t_i in range(10):
    file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputCoronaEDGE/coronainputEDGE{}.txt".format(t_i), mode = 'w+')
    print(10,file = file)
    for j in range(10):
        N = rd.choice(All)
        print(N,N, file = file)
        createEdges(N,file)
    file.close()  
"""
# cycles
for t_i in range(10):
    if (t_i < 2):
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputCoronaEDGE/coronainputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            N = rd.choice(All)
            print(N,N, file = file)
            createCycle(N,file)
        file.close()  
    # 2 δεντρα με ένα κυκλο το καθενα     
    elif (t_i < 4):
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputCoronaEDGE/coronainputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            N = rd.choice(All)
            print(N,N, file = file)
            start = rd.choice(np.arange(3,N-4,1))
            createEdges(0,start,file)
            createEdges(start, N - start ,file)
        file.close()  
    elif (t_i < 6):
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputCoronaEDGE/coronainputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            N = rd.choice(All)
            start = rd.choice(np.arange(3,N-4,1))
            print(N,N, file = file)
            create2Edges(0,start,file)
            createNoEdges(start, N - start ,file)
        file.close()  
    elif (t_i < 8):
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputCoronaEDGE/coronainputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            N = rd.choice(All)
            start = rd.choice(np.arange(3,N-4,1))
            print(N,N, file = file)
            create2Edges(0,N-1,file)
    else :
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputCoronaEDGE/coronainputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            N = rd.choice(All)
            print(N,N, file = file)
            totalRandom(N,file)
        file.close()   
"""
# Κυκλος Ν κόμβων
# 2 δεντρα με ενα κυκλο το καθενα
# 2 δεντρα με 2 κυκλους στο ένα δεντρο
# 2 δεντρα με 2 κυκλους στο ένα δεντρο που τεμνοντε με μια ακμη
# Μονηρης κομβος με 2 κυκλους στο δεντρο
#  1-2 ραντομ 
"""