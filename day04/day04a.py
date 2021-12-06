#!/usr/bin/python

import time
import tracemalloc
from numpy import transpose
from numpy import zeros

starttime = time.time()
tracemalloc.start()

h=5
w=5

class Carte:
    numbers = []
    checks = []

    def __init__(self,tab):
        self.numbers = tab
        self.checks = zeros([5,5])

    def check(self,n):
        for i in range(h):
            if(n in self.numbers[i]):
                j=self.numbers[i].index(n)
                self.checks[i][j]=1
    
    def win(self):
        r = False
        for l in self.checks:
            if (sum(l) == len(l)):
                r = True
    
        for l in transpose(self.checks):
            if (sum(l) == len(l)):
                r = True
        return r
    
    def sumuncheck(self):
        s = 0
        for i in range(h):
            for j in range(w):
                if(self.checks[i][j]==0):
                    s = s + int(self.numbers[i][j])
        return s


    def __repr__(self):
        r = ""
        for i in range(h):
            ch = ""
            for j in range(w):
                if(self.checks[j][j]==1):
                    ch = ch +  self.numbers[i][j] + "* "
                else:
                    ch = ch + self.numbers[i][j] + "  "
            ch = ch + "\n"
            r = r + ch
        return r


answer = 0
i = 0
tirage,cartes = [],[]


with open('ex_day04.txt') as data:
    # lire les tirages
    tirage = data.readline().strip().split(',')

    # lire les cartes
    data.readline()
    t = []
    for line in data.readlines():
        if (line.strip() == ""):
            cartes.append(Carte(t))
            t = []
        else:
            l = line.strip().split()
            t.append(l)

for t in tirage:
    won = False
    for c in cartes:
        c.check(t)
        if(c.win()):
            won = True
            print(c)
            s = c.sumuncheck()
            answer = s*int(t)
            print(f"*** {s} * {t} = {answer}")
            break
    if(won):
        break


endtime = time.time()

print("===========================")
print("AOC 2021 - day 4 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
