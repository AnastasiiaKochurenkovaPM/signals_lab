import numpy as np
import matplotlib.pyplot as plt

def arithmetic_mean(values):
    return np.mean(values)

def harmonic_mean(values):
    return len(values) / np.sum(1 / values)

def geometric_mean(values):
    values = np.where(values <=0, np.nan, values)
    return np.nanprod(values) ** (1/np.sum(~np.isnan(values)))
   
def generate_test_sequence(N, A, n, phi, max_error_ratio):
    x = np.linspace(0, 1, N)  
    y_exact = A * np.sin(n * x + phi)  # Точні значення синусоїди без спотворень
    # Генеруємо випадкові відхилення
    max_error = max_error_ratio * A 
    errors = np.random.uniform(-max_error, max_error, N)  # Генеруємо випадкові значення похибок
    y_distorted = y_exact + errors
    return x, y_exact, y_distorted

# точне значення
def exact_value(x, A, n, phi):
    return A * np.sin(n * x + phi)

# обчислення похибок
def compare_values(approximate, exact):
    absolute_error = np.abs(approximate - exact)
    relative_errors = absolute_error / np.abs(exact)
    return absolute_error, relative_errors

def plot_result(x, y, y_exact):
    plt.plot(x, y, label='Зі спотворенням')
    plt.plot(x, y_exact, label='Точне значення')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Параметри синусоїди та генерації тестової послідовності
N = 1100 
A = 1  # Амплітуда синусоїди
n = 11 
phi = 0  # Зсув по фазі синусоїди
max_error_ratio = 0.05  # Максимальне відхилення (5% від амплітуди)

# Генеруємо тестову послідовність
x, y_exact, y_distorted = generate_test_sequence(N, A, n, phi, max_error_ratio)

arithmetic = arithmetic_mean(y_distorted)
harmonic = harmonic_mean(y_distorted)
geometric = geometric_mean(y_distorted)

print("\nСереднє арифметичне:", arithmetic)
print("Середнє гармонічне:", harmonic)
print("Середнє геометричне:", geometric)


# Обчислюємо точне значення
y_exact = exact_value(x, A, n, phi)
# Заміна нульових значень у y_exact на машинну точність
y_exact[np.abs(y_exact) < np.finfo(float).eps] = np.finfo(float).eps

# Обчислюємо абсолютні та відносні похибки
absolute_errors, relative_errors  = compare_values(y_distorted, y_exact)

# Знаходимо максимуми та мінімуми абсолютних та відносних похибок
max_absolute_error = np.max(absolute_errors)
min_absolute_error = np.min(absolute_errors)
max_relative_error = np.max(relative_errors)
min_relative_error = np.min(relative_errors)

print("\nМаксимум абсолютної похибки:", max_absolute_error)
print("Мінімум абсолютної похибки:", min_absolute_error)
# print("Максимум відносної похибки:", max_relative_error)
print("Мінімум відносної похибки:", min_relative_error)

# Виводимо графік функції
plot_result(x, y_distorted, y_exact)