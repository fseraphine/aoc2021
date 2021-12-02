#!/usr/bin/python

import time
from more_itertools import windowed
import tracemalloc

answer = 0
pos = { 'd': 0, 'h': 0 }

starttime = time.time()
tracemalloc.start()

moves = []
for line in open('data_day02.txt'):
    move = line.strip().split(" ")
    m = (move[0],int(move[1]))

for m in moves:
    if(m[0]=='forward'):
        pos['h'] = pos['h'] + m[1]
    elif(m[0]=='down'):
        pos['d'] = pos['d'] + m[1]
    elif(m[0]=='up'):
        pos['d'] = pos['d'] - m[1]
    #print(f"{m}\t=> h {pos['h']} - d {pos['d']} - a {pos['a']}")

answer = pos['h'] * pos['d']

endtime = time.time()

print("===========================")
print("AOC 2021 - day 2 - puzzle 1")
print(f"*** Answer : {answer}")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
print("===========================")