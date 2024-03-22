import matplotlib.pyplot as plt
import random as rand
import numpy as np
import statistics as stat
N = 10_000

def f(k):
    if k == 0:
        return 0.5
    return 1 / (4 * abs(k) * (abs(k) + 1))

def sample():
    x = np.random.uniform(0, 1, N)
    randomized = np.random.randint(0,2,N)
    randomized2 = np.random.randint(0,2,N)

    k = np.floor(1 / x)

    k[randomized == 0] *= -1
    k[randomized2 == 0] = 0

    return k

sum = 0
x_average = []
x_median = []

x = sample()

for i in range(N):
    sum += x[i]
    x_average.append(sum / (i + 1))
    x_median.append(stat.median(x[0:i+1]))

plt.plot(x_average)
plt.plot(x_median)
plt.show()
