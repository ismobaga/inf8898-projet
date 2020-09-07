from naive import naive
from greedy import greedy

entries =[
           [0, 3, 1, 4],
           [0, 2, 1, 1],
           [1, 4, 1, 3],
           [1, 3, 2, 4], 
           [2, 4, 3, 5],
           [2, 2, 2, 3]
]


# class Benchmark:
#     @staticmethod
#     def run(function):
#         timings = []
#         stdout = sys.stdout
#         for i in range(100):
#             sys.stdout = None
#             startTime = time.time()
#             function()
#             seconds = time.time() - startTime
#             sys.stdout = stdout
#             timings.append(seconds)
#             mean = statistics.mean(timings)
#             if i < 10 or i % 10 == 9:
#                 print("{} {:3.2f} {:3.2f}".format(
#                     1 + i, mean,
#                     statistics.stdev(timings, mean) if i > 1 else 0))

r = naive(entries)
g = greedy(entries)

print(r)
print(g)



