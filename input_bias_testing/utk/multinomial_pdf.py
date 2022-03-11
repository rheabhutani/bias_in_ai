import numpy as np 
from numpy import array, log, exp
import scipy.stats as stats
from scipy.stats.distributions import chi2

def GAMMA_LN(n):
    return stats.gammaln(n)

def log_factorial(x):
    return stats.gammaln(array(x)+1.0)

def PDF(P, G, n):
    ''' Arguments: 
    P -> The observed frequency distribution 
    G -> The global probability 
    N -> Number of samples (dataset size) 

    Returns: Assuming multinomial distribution, we compute the chi-squared p-value for goodness of fit
    '''

    P, G = array(P), array(G)
    result = stats.chisquare(f_obs=P, f_exp=n*G)
    arg = result[0]
    while arg > 10:
        arg = log(arg) 
    return 1-chi2.sf(arg, len(P))
