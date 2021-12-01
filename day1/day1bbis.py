#!/usr/bin/python

import time
from more_itertools import windowed

starttime = time.time()

i = sum(map(lambda x: int(x[0]<x[1]),windowed(map(sum, windowed(map(int,open('data_day1.txt')),3)),2)))

endtime = time.time()

print("AOC 2021 - day 1 - puzzle 2")
print("AOC 2021 - day 1 - puzzle 2")
print("inc:",i)
print("Temps d'éxécution:",endtime-starttime)