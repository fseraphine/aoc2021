#!/usr/bin/python

import time
import tracemalloc


starttime = time.time()
tracemalloc.start()

answer = 0
p = []
with open('data_day07.txt') as data:
    p = list(map(int,data.readline().strip().split(',')))

answer = len(p)+1000000
for i in range(len(p)):
    acc = 0
    for e in p:
        acc = acc + abs(i-e)
    answer = min(answer,acc)

endtime = time.time()

print("===========================")
print("AOC 2021 - day 7 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
