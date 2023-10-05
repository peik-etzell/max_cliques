from math import log2
import numpy as np
import matplotlib.pyplot as plt

fig, clique_axis = plt.subplots(1)
time_axis = clique_axis.twinx()

data = np.genfromtxt(fname='out.tsv', delimiter='\t')
data = np.sort(data, axis=0)
x, y_real, time = zip(*data)


def plot_real_data():
    clique_axis.plot(x, y_real, '.', label='Real data')
    fig.legend()


def plot_theoretical():
    k_v = np.vectorize(lambda x: int(
        2 * log2(x) - 2*log2(log2(x))))
    y_theory = k_v(x)
    clique_axis.plot(x, y_theory, label='2log(n) - 2loglog(n)')
    fig.legend()


def plot_time():
    time_axis.plot(x, time, label='Time taken')
    fig.legend()


plot_real_data()
plot_theoretical()
plot_time()

clique_axis.set_xlabel('Number of vertices')
clique_axis.set_ylabel('Size of maximum clique')
time_axis.set_ylabel('Time taken (s)')

plt.savefig('plot.png')
plt.show()
