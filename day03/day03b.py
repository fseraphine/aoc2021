#!/usr/bin/python

import time
import tracemalloc
from numpy import transpose
from functools import reduce

starttime = time.time()
tracemalloc.start()

answer = 0
tab = []
g,e=0,0
with open('data_day03.txt') as data:
    for line in data:
        tab.append(list(map(int,list(line.strip()))))

for l in transpose(tab):
    print(sum(l),len(l))
    if(sum(l)>len(l)/2):
        g = (g<<1)|1
        e = (e<<1)|0
    else:
        g = (g<<1)|0
        e = (e<<1)|1

print(g,e)

answer = g * e

endtime = time.time()

print("===========================")
print("AOC 2021 - day 3 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
