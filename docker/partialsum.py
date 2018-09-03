import time
import numpy as np
import numpy .linalg as nl
import random  
#import matplotlib.pyplot as plt
import sys
import os
print(os.environ['nmax'])
n_max=int(os.environ['nmax'])
# Iteration über sämtliche Argumente:
#for eachArg in sys.argv:   
#    print(eachArg)
#t1 = np.linspace(1,5,10)
#t2 = np.linspace(1,5,20)
#plt.plot(t1,t2)
#(t1, t1, ’r -- ’,t1, t1++2, (bs, t2,np.log(t2)**3), 'g^-')
#plt.show()

# # n = 15

# # A = np .random.rand ( 1, n )

# Aprime = A.transpose()
# print(A)

# i = 0
# while i < 10:
#    # uu= yield _do()
#     uu = random.randint(1,10)
#     print(uu)
#     time.sleep(1)
#     i=i+1

# #r = random.randint(1,10)  
# #rint(r)
#  X = np.random.rand(5,2)
#  print(X)
# #print("le produit est ",n)

# def fill_tab(tab,int):
#     for index in len(tab) : tab[index] = 0
# # print(tab)
# i=0
# su = 0
# N = 3
# while i < N:
#     su = su + 1./(i*i)
# 	print(su)
#     i=i+1


def partialsum(n_max) :
# summe des carre
    print(n_max)
    S=0
    sums=[]
    for i in range(1, n_max,1) :
        S+= 1/(i*i)
        sums.append(S)
    return(sums)

#n_max= 100 #int(sys.argv[1])
r= partialsum(n_max)

print(r)








