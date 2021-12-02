#!/usr/bin/python

import time
from more_itertools import windowed
import tracemalloc

starttime = time.perf_counter()
tracemalloc.start()

with open('data_day1.txt') as fichier:
    i = sum(map(lambda x: int(x[0]<x[1]),windowed(map(sum, windowed(map(int,fichier),3)),2)))

endtime = time.perf_counter()

print("===========================")
print("AOC 2021 - day 1 - puzzle 2")
print(f"*** Answer : {i}")
print(f"Temps d'exécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("===========================")