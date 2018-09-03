import time
import numpy as np
import numpy.linalg as nl
import random  
import matplotlib.pyplot as plt

def sortInt(n_max) :
# summe des carre
    
    listInt=[]
    for i in range(1, n_max) :
        s = random.randint(1,10)
       	listInt.append(s)
    return(listInt)
    

intRand= sortInt(5) 
print(intRand)


def tri_ins(t):
    permut = 0
    for k in range(1,len(t)):
        temp=t[k]
        j=k
        while j>0 and temp<t[j-1]:
            permut=permut+1
            t[j]=t[j-1]
            j-=1
            t[j]=temp
            print(t)
        permut= permut + 2*len(t)
    return t,permut


x,e=tri_ins(intRand)


