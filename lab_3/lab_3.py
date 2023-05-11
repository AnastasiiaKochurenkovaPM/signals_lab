import numpy as np
import time
import matplotlib.pyplot as plt

# функція для обчислення швидкого перетворення Фур'є
def fft(x):
    n = len(x)
    if n == 1:
        return x
    else:
        # доповнення вхідного сигналу нулями до степеня 2
        m = 2**int(np.ceil(np.log2(n)))
        x_padded = np.pad(x, (0, m-n), 'constant')
        
        even = fft(x_padded[::2])
        odd = fft(x_padded[1::2])
        w = np.exp(-2j * np.pi * np.arange(m) / m)
        
        return np.concatenate([even + w[:int(m/2)] * odd, even + w[int(m/2):] * odd])

# генерація випадкового сигнала довжиною N
N = 210
x = np.random.rand(N)

# обчислення ШПФ
t1 = time.time()
Ck = fft(x)
t2 = time.time()

for i, val in enumerate(Ck):
    print(f"C_{i}: {val}")

# час обчислення
print(f"\nЧас виконання: {t2-t1} секунд")

# кількість операцій
num_plus = N
num_mult = 4*N
num_operations = num_mult + num_plus

print(f"\nКількість операцій додавання: {num_plus}")
print(f"Кількість операцій множення: {num_mult}")
print(f"Загальна кількість операцій: {num_operations}")

# обчислення спектру амплітуд і фаз та побудова графіків
amplitude = np.abs(Ck)
phase = np.angle(Ck)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].stem(amplitude)
axs[0].set_title('Графік спектру амплітуд')
axs[0].set_xlabel('Частоти')
axs[0].set_ylabel('Амплітуда')
axs[1].stem(phase)
axs[1].set_title('Графік спектру фаз')
axs[1].set_xlabel('Частоти')
axs[1].set_ylabel('Фази')
plt.tight_layout()
plt.show()