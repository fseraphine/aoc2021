#!/usr/bin/python

import time
import tracemalloc
import numpy as np


starttime = time.time()
tracemalloc.start()

answer = 0
f = []
with open('data_day06.txt') as data:
    f = list(map(int,data.readline().strip().split(',')))

timer=0

while timer <256:
    for i in range(len(f)):
        if (f[i]==0):
            f[i]=6
            f.append(8)
        else:
            f[i]=f[i]-1
    timer = timer +1
    #print(timer,f)

answer=len(f)

endtime = time.time()

print("===========================")
print("AOC 2021 - day 6 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
