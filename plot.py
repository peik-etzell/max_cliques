import numpy as np
import matplotlib.pyplot as plt
import math

CSVFILE = './out.csv'


data = np.genfromtxt(CSVFILE, delimiter=';')
x, y = zip(*data)
plt.plot(x, y, label='Real data')
plt.legend()


def k_theoretical(n: float):
    return 2 * math.log2(n)


k_v = np.vectorize(k_theoretical)
x_prime = np.linspace(3, max(x), 10000)
y_prime = k_v(x_prime)
plt.plot(x_prime, y_prime, label='Theoretical')
plt.legend()

plt.show()
