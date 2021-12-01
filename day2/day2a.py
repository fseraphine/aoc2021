#!/usr/bin/python

import time
from more_itertools import windowed
import tracemalloc

starttime = time.time()
tracemalloc.start()

with open('data_day1.txt') as fichier:
    i = sum(map(lambda x: int(x[0]<x[1]),windowed(map(sum, windowed(map(int,fichier),3)),2)))


endtime = time.time()

print("===========================")
print("AOC 2021 - day 2 - puzzle 1")
print(f"*** Answer : {i}")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("===========================")