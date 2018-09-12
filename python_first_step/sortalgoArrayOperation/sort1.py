import time
import numpy as np
import numpy .linalg as nl
import random  
import matplotlib.pyplot as plt

def f(t):   
    return np.exp(-t) * np.cos(2*np.pi*t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.figure("superposed figures"")
#plt.title("superposed figures")
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.subplot(223)
plt.plot(t2, np.sin(2*np.pi*t2), 'b-')
plt.show()
