#!/usr/bin/python

import time
import tracemalloc


starttime = time.time()
tracemalloc.start()

answer = 0
#sig = []
out = []
sizes = {1:2 , 4:4 , 7:3 , 8:7}

with open('data_day08.txt') as data:
    for l in data.readlines():
        (s, o) = l.strip().split("|")
        #sig.append(s.strip().split(" "))
        out = out + o.strip().split(" ")

for e in out:
    for v in sizes.values():
        if(len(e)==v):
            answer = answer + 1


endtime = time.time()

print("===========================")
print("AOC 2021 - day 8 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
