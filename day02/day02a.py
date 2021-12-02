#!/usr/bin/python

import time
from more_itertools import windowed
import tracemalloc

answer = 0
pos = { 'd': 0, 'h': 0 }

starttime = time.time()
tracemalloc.start()

with open('data_day02.txt') as data:
    for line in data:
        d,q = line.strip().split(" ")
        if(d=='forward'):
            pos['h'] = pos['h'] + int(q)
        elif(d=='down'):
            pos['d'] = pos['d'] + int(q)
        elif(d=='up'):
            pos['d'] = pos['d'] - int(q)
        #print(f"{m}\t=> h {pos['h']} - d {pos['d']} - a {pos['a']}")

answer = pos['h'] * pos['d']

endtime = time.time()

print("===========================")
print("AOC 2021 - day 2 - puzzle 1")
print(f"*** Answer : {answer}")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("===========================")