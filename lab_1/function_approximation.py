import numpy as np
from function import function

def approximation(a0, ak, bk, n, x):
    y = a0/2
    for i in range(1, n+1):
        y += ak[i-1]*np.cos(i*np.pi*x/(np.pi - 0)) + bk[i-1]*np.sin(i*np.pi*x/(np.pi - 0))
    return y