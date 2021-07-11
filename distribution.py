'''
Probability distribtion
Gaosheng Liu 
10/07/2021
1. Exponential
2. Poission
3. Uniform
4. Geometric

'''

# Import packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# For exponential
'''
    Plots the exponential distribution function for a given x range
    If mu and sigma are not provided, standard exponential is plotted
    If cdf=True cumulative distribution is plotted
    Passes any keyword arguments to matplotlib plot function
'''
def plot_exponential(x_range, mu=0, sigma=1, cdf=Flase, **Kwargs):
    x = x_range
    if cdf:
        y = ss.expon.cdf(x, mu, sigma) ''' x reprents the range od x; mu represents the
                                           the starting of x; sigma represent the 1/lamada.
                                       '''
    else:
        y = ss.expon.pdf(x, mu, sigma)
    plt.plot(x, y, **kwargs)

x = np.linspace(0, 5, 5000)

plot_exponential(x, 0, 1, color='red', lw=2, ls='-', alpha=0.5, label='pdf')
plot_exponential(x, 0, 1, cdf=True, color='blue', lw=2, ls='-', alpha=0.5, label='cdf')
plt.legend