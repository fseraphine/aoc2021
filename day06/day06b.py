#!/usr/bin/python

import time
import tracemalloc
import numpy as np


starttime = time.time()
tracemalloc.start()

class Fishtank:
    old = {}

    def __init__(self,t):
        for e in t:
            self.old[e] = self.old.get(e,0) + 1

    def __repr__(self):
        return str(self.old)

    def pop(self):
        return sum(self.old.values())
    
    def itere(self,n):
        new = {}
        for i in range(n):
            new.clear()
            for k,v in self.old.items():
                if (k==0):
                    new[8]=v + new.get(8,0)
                    new[6]=v + new.get(6,0)
                else:
                    new[k-1]=v + new.get(k-1,0)
            self.old.clear()
            self.old = new.copy()


answer = 0
f = []
with open('data_day06.txt') as data:
    f = list(map(int,data.readline().strip().split(',')))


fishes = Fishtank(f)
fishes.itere(256)
answer=fishes.pop()

endtime = time.time()

print("===========================")
print("AOC 2021 - day 6 - puzzle 2")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
