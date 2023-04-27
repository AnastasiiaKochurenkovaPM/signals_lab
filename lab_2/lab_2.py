import numpy as np
import random
import time
import matplotlib.pyplot as plt


def fourier_coefficient(x, k):
    N = len(x)
    omega = (2*np.pi)/N
    ak = np.sum(x*np.cos(omega*k*np.arange(N)))
    bk = np.sum(x*np.sin(omega*k*np.arange(N)))
    ck = ak - 1j * bk
    num_mult = 8*N+1
    num_add = 2*(N-1)
        
    return ck, num_mult, num_add

def DFT(x):
    N = len(x)
    c = np.zeros(N, dtype=np.complex128)
    total_mult = 0
    total_add = 0
    for k in range(N):
        c[k], num_mult, num_add = fourier_coefficient(x, k)
        total_mult += num_mult
        total_add += num_add
        print(str(k) + "-ий член ряду = "  + str(c[k]))
    print("\n\nКількість операцій множення та додавання: ", total_add+total_mult)
    print("\nКількість операцій множення: ", total_mult)
    print("\nКількість операцій додавання: ", total_add)

    return c


def generate_complex_vector(N, a, b):
    result = []
    for i in range(N-1):
        #генерація дійсної частини
        x = random.randint(a, b)
        #генерація уявної частини
        y = random.randint(a, b)
        #результат - комплексне число
        z = complex(x,y)
        result.append(z)
    return result

def generate_vector(N, a, b):
    result = []
    for i in range(N-1):
        x = random.randint(a, b)
        result.append(x)
    return result


def amplitudes_phases_spectrum(ck):
    N = len(ck)
    amp = np.zeros(N) # масив амплітуд
    phase = np.zeros(N) # масив фаз

    for i in range(N-1):
        amp[i] = np.sqrt(ck[i].real**2 + ck[i].imag**2) # обчислення амплітуди
        phase[i] = np.arctan2(ck[i].imag, ck[i].real) # обчислення фази

    # Візуалізація
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

    axs[0].stem(amp)
    axs[0].set_title('Графік спектру амплітуд')
    axs[0].set_xlabel('Частоти')
    axs[0].set_ylabel('Амплітуда')

    axs[1].stem(phase)
    axs[1].set_title('Графік спектру фаз')
    axs[1].set_xlabel('Частоти')
    axs[1].set_ylabel('Фази')

    plt.tight_layout()
    plt.show()

    return amp, phase

N = 21
# x = generate_complex_vector(N, -6, 6)
x = generate_vector(N, -10, 10)
print("\n\nВектор х:\n", x)
print("\n\nКоефіцієнти Фур'є Сk:")

start_time = time.time()
ck = DFT(x)
end_time = time.time()
    
print("\nЧас виконання програми:", end_time - start_time, "секунд\n\n")

amp, phase = amplitudes_phases_spectrum(ck)