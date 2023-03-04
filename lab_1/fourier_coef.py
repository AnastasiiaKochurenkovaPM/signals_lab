import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

from function import function

def fourier(li, lf, n, f):
    l = (lf-li)/2
    
    a0=1/l*integrate.quad(lambda x: f(x), li, lf)[0]
    A = np.zeros((n))
    B = np.zeros((n))
     
    for i in range(1,n+1):
        A[i-1]=1/l*integrate.quad(lambda x: f(x)*np.cos((i*x)), li, lf)[0]
        #A[i-1]=2/lf*integrate.quad(lambda x: f(x)*np.cos((i*x)), li, lf)[0]
    for i in range(1,n+1):    
        B[i-1]=1/l* integrate.quad(lambda x: f(x)*np.sin((i*x)), li, lf)[0]
        #B[i-1]=2/lf* integrate.quad(lambda x: f(x)*np.sin((i*x)), li, lf)[0]
 
    return [a0, A, B]