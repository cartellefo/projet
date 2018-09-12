import numpy as np 
import math
import random 
#import sys

#for eachArg in sys.argv:   
    #print(eachArg)






def generate_randlist(N,min_int,max_int):
	listint =[]
	for i in range(N):
		listint.append(random.randint(min_int,max_int))
	return(listint)

	

#N= int(sys.argv[1])
#min_int = int(sys.argv[2])
#max_int = int(sys.argv[3])



#matrix operations
#tableau = np.zeros((2,3), dtype ="i") cf dataFrame pandas




#tableau = np.random.randint(1,10)






#def arrysort(tableau):
tab1 =[]
tab2 =[]
tableau = generate_randlist(100,1,50)
print("my tab ist \n", tableau)

for i in range(len(tableau)):
	if tableau[i] % 2 == 0:
		tab1.append(tableau[i])
	else:
		tab2.append(tableau[i])


print("arry of pair \n ",tab1, " \n arry of impair \n",tab2)
print("the inverse of pai array ist \n ", reversed(tab1))


#print(" the sort array of impair Arry ist \n", tab2.sort())



#arry2 = generate_number(50,1,100)
#print(reversed(arry2))
#print(arry2.sort())
#print(arry3)
#print(arry1)






# print(arry1.max())
# print(arry1.min())
# arry1.argmin()
# arry1.argmax()
# np.all(arry1 = 5)
# np.any(aryy1 !=5)


# matrix 

#data = np.loadtxt('data/populations.txt')
