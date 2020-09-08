from naive import naive
from greedy import greedy
from genetic import genetic
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
l = 0.45

for l in np.arange(0.25, 5.001, 0.20):
    # n = naive(data.get(l))
    g = greedy(data.get(l))
    ge = genetic(data.get(l))
    print(g)
    print(ge)

# print(data.get(2.85))
# Benchmark.run(lambda : genetic(data.get(4.85)))
# print(n)




