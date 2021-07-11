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
import scipy.stats as ss
from scipy.stats import poisson
from scipy.stats import uniform
from scipy.stats import geom
from scipy.stats import expon
import sys

#Define the public variables
x_continous = np.arange(0, 10)
x_exponential = np.arange(0, 10)
x_discrete = np.arange(0, 100, 1)
geom_probability = 0.5
expon_alpha = 0.5
# For exponential
'''
    Plots the exponential distribution function for a given x range
    If mu and sigma are not provided, standard exponential is plotted
    If cdf=True cumulative distribution is plotted
    Passes any keyword arguments to matplotlib plot function (Continous)
'''
def plot_exponential(): 
    # The first method
    # mu=0, sigma=1, cdf=False, **kwargs
    '''
    if cdf:
        # x reprents the range od x; mu represents the
         #   the starting of x; sigma represent the 1/lamada.
        
        y = ss.expon.cdf(x_continous, mu, sigma) 
    else:
        y = ss.expon.pdf(x_continous, mu, sigma)
    plt.plot(x_continous, y, **kwargs)
    '''
    # the second method
    y = expon.pdf(x_exponential, 0, 1)
    z = expon.cdf(x_exponential, 0, 1)
    plt.plot(x_exponential, y, label='pdf', color='red')
    plt.plot(x_exponential, z, label='cdf', color='blue')
    plt.legend(title='Exponential')
    plt.show()

'''
For uniform distribution (Continous)
'''
def plot_uniform():
    y = uniform.pdf(x_continous, 0, 100)
    z = uniform.cdf(x_continous, 0, 100)
    plt.plot(x_continous, y, label='pdf', color='red')
    plt.plot(x_continous, z, label='cdf', color='blue')
    plt.legend(title='Uniform')
    plt.show()

'''
For poisson distribution (discrete)
'''
def plot_poisson():
    # First figure
    y = poisson.pmf(x_discrete, mu=40, loc=10)
    z = poisson.cdf(x_discrete, mu=40, loc=10)
    plt.plot(x_discrete, y, label='pdf', color='red')
    plt.plot(x_discrete, z, label='cdf', color='blue')
    plt.legend(title="Poisson")
    plt.show()

'''
For geometric distribution (discrete)
'''
def plot_geometric():
    y = geom.pmf(x_discrete, geom_probability)
    z = geom.cdf(x_discrete, geom_probability)
    plt.plot(x_discrete, y, label='pdf', color='red')
    plt.plot(x_discrete, z, label='cdf', color='blue')
    plt.legend(title='Geometric')
    plt.show()


def main(distributioType):
    if distributioType == 'Exponential':
        #plot_exponential(0, 1, color='red', lw=2, ls='-', alpha=0.5, label='pdf')
        #plot_exponential(0, 1, cdf=True, color='blue', lw=2, ls='-', alpha=0.5, label='cdf')
        #plt.legend()
        #plt.show()
        plot_exponential()
    elif distributioType == 'Poisson':
        plot_poisson()
    elif distributioType == 'Uniform':
        plot_uniform()
    else:
        plot_geometric()


if __name__ == "__main__":
    parameter = input("Please selection the distribution:")
    main(parameter)