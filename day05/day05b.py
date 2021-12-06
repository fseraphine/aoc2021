#!/usr/bin/python

import time
import tracemalloc
import re
import numpy as np
from functools import reduce

starttime = time.time()
tracemalloc.start()

class Carte:

    def __init__(self,n,m):
        t = []
        for i in range(n):
            l = []
            for j in range(m):
                l.append(0)
            t.append(l)
        self.t = t
        self.n=n
        self.m=m
    
    def __repr__(self):
        s = "* Carte\n"
        for l in self.t:
            for e in l:
                s = s + " " + str(e)
            s = s + "\n"
        return s

    def mark(self,e):
        (x0,y0,x1,y1)=e
        dx = np.sign(x1-x0)
        dy = np.sign(y1-y0)
        while x0 != x1+dx or y0 != y1+dy:
            self.t[x0][y0] += 1
            x0 += dx
            y0 += dy
        
    def res(self):
        r = 0
        for l in self.t:
            r = r + reduce(lambda x,y: x+1 if y>=2 else x, l)
        return r

pattern = re.compile("(\d+),(\d+) -> (\d+),(\d+)")

answer = 0
tab = []
maxh = maxw = 0
with open('data_day05.txt') as data:
    for line in data:
        if (m := pattern.match(line)):
             t = list(map(int,m.groups()))
             tab.append(t)
             maxh = max(maxh,t[0],t[2])
             maxw = max(maxw,t[1],t[2])

c = Carte(maxh+1,maxw+1)
for e in tab:
    c.mark(e)
answer = c.res()

endtime = time.time()

print("===========================")
print("AOC 2021 - day 5 - puzzle 2")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
