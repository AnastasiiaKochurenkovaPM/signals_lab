import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from function import function
from show_func import show_func
from function_approximation import approximation
from hurmonic import hurmonic

# обчислення функції
#show_func()

# межі
li = 0
lf = np.pi
n = 30

# коефіцієнти фур'є
l = (lf - li)/2
a0 = 1/l*integrate.quad(lambda x: function(x), li, lf)[0]
ak = np.zeros((n + 1))
bk = np.zeros((n))
   
for i in range(n + 1):
    if i == 0:
        ak[i] = a0
    else:
        ak[i] = 1/l*integrate.quad(lambda x: function(x)*np.cos((i*x)), li, lf)[0]
        bk[i - 1] = 1/l* integrate.quad(lambda x: function(x)*np.sin((i*x)), li, lf)[0]
       
print('\n\nКоефіцієнти Фур^є\n')
print("a0 = {:.4f}\n".format(ak[0]))

for i in range(n): 
   print("a{} = {:.4f},    b{} = {:.4f}".format(i + 1, ak[i + 1], i + 1, bk[i])) 
print('-------------------------------------------\n')

#будує графік оригінальної функції та графіки наближення
def plot_approximation(ak, bk, n):
    x = np.arange(-np.pi, np.pi, 0.001)
    y = function(x)
    s = np.zeros_like(x)

    plt.figure(figsize=(15, 10))
    plt.plot(x, y, label='Original function')
    for i in range(n):
        s += ak[i] * np.cos(i * x) + bk[i] * np.sin(i * x)
        plt.plot(x, s, label=f'N={i+1}')
    plt.legend()
    plt.show()

#plot_approximation(ak, bk, n)    

y=0.0152
x = np.arange(-np.pi, np.pi, 0.3)
fourier = approximation(a0, ak, ak, n, y)
f_N = round(fourier, 10)
print('Наближене значення функції в точці x =' + str(y))
print('fn = ' + str(f_N) + '\n')
#графіки гармонік
#hurmonic(ak, bk, n)

#відносна похибка
delta = abs(function(x)-f_N)/abs(function(x))
print('Відносна похибка: ' + str(delta) + '\n')

#запис у файл
file = open("fourier_file.txt", "w")
file.write("\nПорядок: " + str(n) + "\nКоефіцієнти Фур'є:\n")
file.write("a0 = {:.4f}\n".format(ak[0]))
for i in range(n):
    file.write("a{} = {:.4f},    b{} = {:.4f}\n".format(i + 1, ak[i + 1], i + 1, bk[i]))
file.write("\nПохибка наближення: " + str(delta))    
file.close()