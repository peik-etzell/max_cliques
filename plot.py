import math
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(fname='out.tsv', delimiter='\t')
data = np.sort(data, axis=0)
x, y = zip(*data)
plt.plot(x, y, label='Real data')
plt.legend()


def k_theoretical(n: float):
    return 2 * math.log2(n)


k_v = np.vectorize(k_theoretical)
x_prime = np.linspace(2, max(x), 10000)
y_prime = k_v(x_prime)
plt.plot(x_prime, y_prime, label='Theoretical')
plt.legend()

plt.xlabel('Number of vertices')
plt.ylabel('Size of maximum clique')

plt.savefig('plot.png')
plt.show()
