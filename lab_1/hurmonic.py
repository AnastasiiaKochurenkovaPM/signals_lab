import numpy as np
import matplotlib.pyplot as plt

def hurmonic(ak, bk, n):
    #a_k
    plt.title("Графік гармоніки ak")
    plt.stem(range(n+1), ak, markerfmt="o")
    plt.show()
    
    #b_k
    plt.title("Графік гармоніки bk")
    plt.stem(range(n), bk)
    plt.show()