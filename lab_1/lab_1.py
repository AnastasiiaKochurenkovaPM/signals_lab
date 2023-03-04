import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from function import function
from show_func import show_func
from fourier_coef import fourier
from function_approximation import approximation
from hurmonic import hurmonic

# first step: calculation function
show_func()

# second step: Fourier coefficients
li = 0
lf = np.pi

k = 3

# Fourier coeffficients for various functions
coeffs = fourier(li, lf, k, function)
print('\n\nКоефіцієнти Фур^є\n')
print('a0 = ' + str(coeffs[0]))
print('ak = ' + str(coeffs[1]))
print('bk = ' + str(coeffs[2]))
print('-------------------------------------------\n')

# third step: function approximation 
f = approximation(coeffs, k)
N = 3
f_N = round(f, N)
print('\nНаближення з точність до порядку ' + str(N) + ':')
print('f = ' + str(f_N) + '\n')

#fourth step: Graphs of harmonics and function a_k, b_k
hurmonic(li, lf, 10)

# fifth step: relative error
delta = abs(f - f_N)/abs(f)
print('\nВідносна похибка: ' + str(delta) + '\n')

# sixth step: write to file
file = open("fourier_file.txt", "w")
file.write("\nПорядок: " + str(N) + "\nКоефіцієнти Фур'є при k = " + str(k) + "\n" + "a_0 = " + str(coeffs[0]) + "\na_k = " + str(coeffs[1]) + "\na_k = " + str(coeffs[2]) + "\nПохибка наближення: " + str(delta))
file.close()

# file = open("fourier_file.txt", "r")
# print(file.read())