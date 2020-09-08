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
    fig.savefig(f'{filename}.{format}', format=format)
def plot(x, y, title=""):
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()

    fig.show()

    fig.savefig("test.png")
l = 0.45

lam = np.arange(0.25, 3.001, 0.20)
for m in (1, 4):
    greedyData = []
    geneticData = []
    naiveData = []
    for l in lam:
        if l < 0.40:
            n = naive(data.get(l))
            naiveData += [n]
        g = greedy(data.get(l, m))
        greedyData += [g]
        ge = genetic(data.get(l, m))
        geneticData += [ge]
        print(g)
        print(ge)
        # break

    naiveData =np.array(naiveData)
    greedyData =np.array(greedyData)
    geneticData =np.array(geneticData)
    fig, ax = plt.subplots()
    ax.plot(lam[:len(naiveData)], naiveData[:,0], label='Naive')
    ax.plot(lam[:len(greedyData)], greedyData[:,0], label='Glouton')
    ax.plot(lam[:len(geneticData)], geneticData[:,0], label="Génétique")
    ax.set(xlabel='La charge du système [requetes / time slot]', ylabel='énergie [J]',
        title="Consommation d'énergie vs La charge du système")
    legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
    save(fig, f'EvsL{m}', "png")

    # Delais
    fig, ax = plt.subplots()
    ax.plot(lam[:len(naiveData)], naiveData[:,1], label='Naive')
    ax.plot(lam[:len(greedyData)], greedyData[:,1], label='Glouton')
    ax.plot(lam[:len(geneticData)], geneticData[:,1], label="Génétique")
    ax.set(xlabel='Délai [ms]', ylabel='énergie [J]',
        title="Pénalité de retard vs La charge du système")
    legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')

    save(fig, f'DvsL{m}', "png")



    # input('press return to end')
# plt.savefig('energy_charge.eps', format='eps')
# print(data.get(2.85))
# Benchmark.run(lambda : genetic(data.get(4.85)))
# print(n)




