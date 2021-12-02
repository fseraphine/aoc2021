#!/usr/bin/python

import time
import tracemalloc

starttime = time.time()
tracemalloc.start()

answer = 0
pos = { 'd': 0, 'h': 0, 'a': 0}

with open('data_day02.txt') as data:
    for line in data:
        m,q = line.strip().split(" ")
        if(m=='forward'):
            pos['h'] = pos['h'] + int(q)
            pos['d'] = pos['d'] + int(q) * pos['a']
        elif(m=='down'):
            pos['a'] = pos['a'] + int(q)
        elif(m=='up'):
            pos['a'] = pos['a'] - int(q)
        #print(f"{m}\t=> h {pos['h']} - d {pos['d']} - a {pos['a']}")

answer = pos['h'] * pos['d']

endtime = time.time()

print("===========================")
print("AOC 2021 - day 2 - puzzle 1")
print(f"*** Answer : {answer}")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("===========================")