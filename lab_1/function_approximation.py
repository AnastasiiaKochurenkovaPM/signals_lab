import numpy as np

def approximation(a0, ak, bk, n, x):
    for i in range(n):
        f = a0/2.0 + np.sum(ak[i+1]*np.cos(i*x) + bk[i]*np.sin(i*x))
    return f