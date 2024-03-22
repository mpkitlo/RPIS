import random
import matplotlib.pylab as plt
import numpy as np
import math

data = np.loadtxt("us_births_69_88.csv", delimiter=",", dtype = int, skiprows = 1)
births = data[:, 2]
sum_births = sum(births)
weights = [births[i] / sum_births for i in range(372)]
N = max(weights);

def rand_date():
    while True:
        randomDay = random.randrange(0,372)
        epsilon = random.uniform(0, 1)
        if(epsilon < weights[randomDay] / N):
            return randomDay


def f():
    s = set()
    ile = 0
    randomDay = 0
    while ile == len(s):
        randomDay = rand_date()
        ile += 1
        s.add(randomDay)
    return ile

x = range(1,1000000)
y = [f() for i in x]

plt.hist(y, range(80))
