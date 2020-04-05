import random as rd
import numpy as np
a = np.arange(0,10**9,1)
b = np.arange(0,2*10**5,1)
for t_i in range(20):
    file = open("/Users/alexanders_mac/MyProjects/C++_Projects/Programming_Languages_1_2020/Series1/TestCases/InputPowersOf2/powers2input{}.txt".format(t_i), mode = 'w+')
    print(10,file = file)
    for j in range(10):
        curr1 = rd.choice(a)
        curr = rd.choice(b)
        print(curr1,curr, file=file)
    file.close()        
   
