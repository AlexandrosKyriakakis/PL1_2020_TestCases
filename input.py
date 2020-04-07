import random as rd
import numpy as np
closeToLimmitN = np.arange(10**8,10**9,1)
closeToLimmitK = np.arange(10**5,2*10**5,1)
closeToKN = np.arange(10**5,2*10**5 - 2,1)
closeToNK = [x+rd.choice([-2,-1,0,1,2]) for x in closeToKN]
verysmallN = np.arange(0,100,1)
verysmallK = np.arange(0,100,1)
for t_i in range(30):
    if (t_i < 10):
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputPowersOf2EDGE/powers2inputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            curr1 = rd.choice(closeToLimmitN)
            curr = rd.choice(closeToLimmitK)
            print(curr1,curr, file=file)
        file.close()        
    elif (t_i < 20):
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputPowersOf2EDGE/powers2inputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            curr1 = rd.choice(closeToKN)
            curr = rd.choice(closeToNK)
            print(curr1,curr, file=file)
        file.close()        
    else :
        file = open("/Users/alexanders_mac/Desktop/Profiteus/NTUA/Programming Languages 1/PL1_2020/TestCases/InputPowersOf2EDGE/powers2inputEDGE{}.txt".format(t_i), mode = 'w+')
        print(10,file = file)
        for j in range(10):
            curr1 = rd.choice(verysmallN)
            curr = rd.choice(verysmallK)
            print(curr1,curr, file=file)
        file.close()        

