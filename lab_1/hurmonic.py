import numpy as np
import matplotlib.pyplot as plt
from function import function
from fourier_coef import fourier

def hurmonic(li, lf, n):
    coef = fourier(li, lf, n, function)

    # x=np.linspace(np.pi,2000)
    # y = [0 for _ in x] 
    # for n in range(0, n):
    #     y += n*np.sin(n*np.pi*x)
    # plt.plot(x,y)
    # plt.grid()
    # plt.show()


    #a_k
    x = np.array(["a_1", "a_2", "a_3", "a_4", "a_5", "a_6", "a_7", "a_8", "a_9", "a_10"])
    plt.bar("a_0", coef[0], width = 0.1)
    plt.bar(x, coef[1], width = 0.1)
    plt.show()
    
    #b_k
    x = np.array(["b_1", "b_2", "b_3", "b_4", "b_5", "b_6", "b_7", "b_8", "b_9", "b_10"])
    plt.bar(x, coef[2], width = 0.1)
    plt.show()