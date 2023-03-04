import numpy as np

def approximation(coeffs, k):
    f = coeffs[0]/2.0 + np.sum(coeffs[1] + coeffs[2])
    return f