
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib as mpl
import random # Pour tirer des notes au hasard
import scipy.optimize
from scipy.optimize import curve_fit
#from __future__ import division
import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as pyplot
import scipy as sp
import scipy.integrate


import %matplotlib inline

data=np.genfromtxt('data/histogramm.txt') 
print(data[:5])
dist = scipy.stats.norm(...)

mu, sigma = 0, 0.1
s1 = np.random.normal(mu, sigma, 10)
s2 = np.random.normal(mu, sigma, 100)
s3 = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s1, 30, density=True)
count, bins, ignored = plt.hist(s2, 30, density=True)
count, bins, ignored = plt.hist(s3, 30, density=True)

plt.plot(bins,1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.legend()
plt.title("histogramme Gaussian")
plt.savefig("GaussHist.png")
#plt.show()
# #################################################################################
X = np.linspace(-np.pi,np.pi,256)
 # Les fonctions de numpy peuvent s’appliquer séquentiellement à tous les
# éléments d’un tableau numpy:
C = np.cos(X)
S = np.sin(3*X)
# Maintenant, il faut demander l’affichage des courbes (superposées par défaut)
plt.plot(X,C,color='red', label='cos')
plt.plot(X,S,color='green', label='sin')
plt.plot(C,S,color='yellow', label='cossin')
plt.plot(4*C,S,color='b', label='sinlinea')
plt.savefig("cos_sin.png")
plt.legend()
# plt.clf()

#plt.show()
plt.axes(polar=True) # On se met en coordonnées polaires
plt.plot(X,C) # Les trois courbes précédentes
plt.plot(X,S) # du coup en polaires
plt.plot(C,S)
plt.savefig("cos_sin_polar.png") # Sauvegarde

#plt.clf() 

################################################################################

notes = [random.gauss(10,3) for k in range(130)]
with plt.xkcd(): 
    plt.hist(notes,bins=20,range=(0,20),cumulative=True,label="Mode cumulatif")
    plt.hist(notes,bins=20,range=(0,20),label="Notes des 3 PCSI")
    plt.title("histogramme Gaussian")
    #plt.legend(loc=’upper left’) # Les légendes
plt.savefig("hist.png") 
plt.show()
#plt.clf() 

# plt.hist(notes,bins=20,range=(0,20),label="Notes communes aux 3 PCSI")
# hist_data,bin_edges = np.histogram(notes,bins=20,range=(0,20))
# bin_centers = (bin_edges[:-1] + bin_edges[1:])/2
# def gauss(x, A, mu, sigma):
# 	return A*np.exp(-(x-mu)**2/(2.*sigma**2))


# depart = [30,8,6] # On définit un point de départ "plausible" pour [A,mu,sigma]
# # Et on fait l’ajustement
# coeff,var_matrix = sp.optimize.curve_fit(gauss,bin_centers,hist_data,p0=depart)
# A,mu,sigma = coeff # Récupération des paramètres
# hist_fit = gauss(bin_centers,A,mu,sigma) # La courbes résultantes

# # Son affichage par-dessus l’histogramme
# rmu,rsigma = round(mu,2),round(sigma,2)
# plt.plot(bin_centers,hist_fit,label="Gaussienne, mu={}, sigma={}".format(rmu,rsigma))
# plt.legend() # Choix automatique du placement de la légende
# plt.ylim(0,30) # Pour laisser de la place pour la légende
# #plt.savefig(’fit_result.png’)
# #plt.clf()
# plt.show()

##########################################################################################

# def func(x,a,b,c):
#    return a*numpy.exp(-b*x)-c


# yData = numpy.load('yData.npy')
# xData = numpy.load('xData.npy')

# trialX = numpy.linspace(xData[0],xData[-1],1000)

# # Fit a polynomial 
# fitted = numpy.polyfit(xData, yData, 10)[::-1]
# y = numpy.zeros(len(trailX))
# for i in range(len(fitted)):
#    y += fitted[i]*trialX**i

# # Fit an exponential
# popt, pcov = curve_fit(func, xData, yData)
# yEXP = func(trialX, *popt)

# pyplot.figure()
# pyplot.plot(xData, yData, label='Data', marker='o')
# pyplot.plot(trialX, yEXP, 'r-',ls='--', label="Exp Fit")
# pyplot.plot(trialX,   y, label = '10 Deg Poly')
# pyplot.legend()
# pyplot.show()

# # #######################################################


# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2*np.pi*t)
# plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
# plt.show()