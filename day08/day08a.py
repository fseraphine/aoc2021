#!/usr/bin/python

import time
import tracemalloc


starttime = time.time()
tracemalloc.start()

answer = 0
sig = []
out = []
sizes = {1:2 , 4:4 , 7:3 , 8:7}
times = {}
with open('data_day08.txt') as data:
    for l in data.readlines():
        (s, o) = l.strip().split("|")
        sig.append(s.strip().split(" "))
        out.append(o.strip().split(" "))

for elem in out:
    for e in elem:
        for k,v in sizes.items():
            if(len(e)==v):
                times[k] = times.get(k,0) + 1
print(times)
answer = sum(times.values())

endtime = time.time()

print("===========================")
print("AOC 2021 - day 8 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
