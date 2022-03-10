import numpy as np 
from numpy import array, log, exp

def GAMMA_LN(n):
    c = array([76.18009172947146, -86.50532032941677, \
         24.01409824083091, -1.231739572450155, \
         0.001208650973866179, -0.5395239384953 * 0.00001])
    x = n 
    y = n
    tm = x + 5.5
    tm -= (x + 0.5) * log(tm)
    se = 1.0000000000000190015
    for j in range(6):
        y += 1.0
        se += c[j] / y
    return -tm + log(2.5066282746310005 * se / x)

def log_factorial(x):
    return GAMMA_LN(array(x)+1)

def PDF(P, G, n):
    P, G = array(P), array(G)
    result = log_factorial(n) - sum(log_factorial(P)) + sum(P * log(G))
    return exp(result)

