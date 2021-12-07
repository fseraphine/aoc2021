#!/usr/bin/python

import time
import tracemalloc


starttime = time.time()
tracemalloc.start()

answer = 0
p = []
with open('data_day07.txt') as data:
    p = list(map(int,data.readline().strip().split(',')))

answer = len(p)+10000000000000000
for i in range(len(p)):
    acc = 0
    for e in p:
        s = abs(i-e)
        acc = acc + s*(s+1)/2
    answer = min(answer,acc)

endtime = time.time()

print("===========================")
print("AOC 2021 - day 7 - puzzle 2")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
