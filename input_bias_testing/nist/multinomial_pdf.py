import numpy as np 
from numpy import array, log, exp
import scipy.stats as stats

def GAMMA_LN(n):
    return sc.gammaln(n)

def log_factorial(x):
    return sc.gammaln(array(x)+1.0)

def PDF(P, G, n):
    ''' Arguments: 
    P -> The observed frequency distribution 
    G -> The global probability 
    N -> Number of samples (dataset size) 

    Returns: Assuming multinomial distribution, we return the chi-squared p-value for goodness of fit
    '''

    P, G = array(P), array(G)
    result = stats.chisquare(f_obs=P, f_exp=n*G)
    return 1.0-result[1]
