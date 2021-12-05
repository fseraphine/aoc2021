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
        if (e[0] == e[2]):
            # ligne verticale
            # on calcule la valeur du step pour la boucle
            if (e[1]>e[3]):
                s = -1
            else:
                s = 1
            for i in range(e[1],e[3]+s,s):
                self.t[i][e[0]] += 1
        elif (e[1] == e[3]):
            # ligne horizontale
            if (e[0]>e[2]):
                s = -1
            else:
                s = 1
            for i in range(e[0],e[2]+s,s):
                self.t[e[1]][i] += 1
        elif (e[1] >= e[3]) and (e[0] == e[2])
        
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
print("AOC 2021 - day 5 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
