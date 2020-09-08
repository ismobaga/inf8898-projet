from naive import naive
from greedy import greedy
from genetic import genetic
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('qt5agg')
import data

import statistics
import sys
import time
import numpy as np

entries =[
           [0, 3, 1, 4],
           [0, 2, 1, 1],
           [1, 4, 1, 3],
           [1, 3, 2, 4], 
           [2, 4, 3, 5],
           [2, 2, 2, 3]
]


class Benchmark:
    @staticmethod
    def run(function):
        timings = [] 
        print("hells")
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(
                    1 + i, mean,
                    statistics.stdev(timings, mean) if i > 1 else 0))


def save(fig, filename, format):
    fig.savefig(f'{filename}.eps', format=format)
def plot(x, y, title=""):
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()

    fig.show()

    fig.savefig("test.png")
l = 0.45

lam = np.arange(0.25, 5.001, 0.20)
greedyData = []
geneticData = []

m = 1
for l in np.arange(0.25, 5.001, 0.20):
    # n = naive(data.get(l))
    g = greedy(data.get(l, m))
    greedyData += [g]
    ge = genetic(data.get(l, m))
    geneticData += [ge]
    print(g)
    print(ge)

greedyData =np.array(greedyData)
geneticData =np.array(geneticData)
fig, ax = plt.subplots()
# ax.plot(x, y)
ax.plot(lam, greedyData[:,0])
ax.plot(lam, geneticData[:,0])

save(fig, 'EvsL1', "eps")
# plt.savefig('energy_charge.eps', format='eps')
# print(data.get(2.85))
# Benchmark.run(lambda : genetic(data.get(4.85)))
# print(n)




