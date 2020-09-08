from naive import naive
from greedy import greedy
from genetic import genetic
import data

import statistics
import sys
import time

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

n = naive(entries)
g = greedy(entries)
ge = genetic(entries)

# print(data.get(2.85))
Benchmark.run(lambda : naive(data.get(2.85)))
print(n)
print(g)
print(ge)



