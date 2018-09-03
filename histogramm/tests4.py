
import time
import numpy as np
import numpy .linalg as nl
import random  
import matplotlib.pyplot as plt
from scipy.stats import norm
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=8, usetex=False)

# mu, sigma = 0, 0.1 
# s = np.random.normal(mu, sigma, 10)
# plt.plot(s)
# plt.show()

# Define the distributions to be plotted
sigma_values = [0.5, 1.0, 2.0]
linestyles = ['-', '--', ':']
#colorcube =['black','red','yellow']
#number_N =[10,100,1000]
mu = 0
x = np.linspace(-10, 10, 1000)

# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for sigma, ls in zip(sigma_values, linestyles):
    # create a gaussian / normal distribution
    dist = norm(mu, sigma)

    plt.plot(x, dist.pdf(x), ls=ls, c='black',
             label=r'$\mu=%i,\ \sigma=%.1f$' % (mu, sigma))

plt.xlim(-5, 5)
plt.ylim(0, 0.85)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu,\sigma)$')
plt.title('Histogramme of Gaussian Distribution')
plt.legend()
plt.savefig("hauss4hist.png") 
plt.show()


# plt.plot([1, 2, 3], color='red', label='line one')
# plt.plot([4, 6, 8], color='blue', label='line two')
# plt.legend()
# plt.show()