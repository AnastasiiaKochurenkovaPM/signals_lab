import numpy as np
import matplotlib.pyplot as plt
from function import function

def show_func():
    y = lambda x: (function(x))
    fig = plt.subplots()
    x = np.linspace(0, np.pi, 1000)
    plt.plot(x, y(x))
    plt.show()