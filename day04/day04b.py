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
    numero = None
    numbers = []
    checks = []
    gagnante = False

    def __init__(self,n,tab):
        self.numero = n
        self.numbers = tab
        self.checks = zeros([5,5])

    def coche(self,c):
        # on ne coche plus sur les cartes gagnantes
        if (not self.gagnante):
            for i in range(h):
                if(c in self.numbers[i]):
                    j=self.numbers[i].index(c)
                    self.checks[i][j]=1
    
    def win(self):
        if (self.gagnante):
            return True
        else:
            r = False
            for l in self.checks:
                if (sum(l) == len(l)):
                    r = True
        
            for l in transpose(self.checks):
                if (sum(l) == len(l)):
                    r = True
            self.gagnante = r
            return r
    
    def sumuncheck(self):
        s = 0
        for i in range(h):
            for j in range(w):
                if(self.checks[i][j]==0):
                    s = s + int(self.numbers[i][j])
        return s


    def __repr__(self):
        r = "Carte n°" + str(self.numero) + "\n"
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
finies = []


with open('data_day04.txt') as data:
    # lire les tirages
    tirage = data.readline().strip().split(',')

    # lire les cartes
    data.readline()
    t = []
    i=0
    for line in data.readlines():
        if (line.strip() == ""):
            cartes.append(Carte(i,t))
            i = i+1
            t = []
        else:
            l = line.strip().split()
            t.append(l)

v = None
ordre = []
for t in tirage:
    for c in cartes:
        #print("%d carte %d" % (int(t),c.numero))
        c.coche(t)
        if(c.numero not in ordre and c.win()):
            ordre.append(c.numero)
            v = t

     
s = cartes[ordre[-1]].sumuncheck()
answer = s*int(v)
print(ordre,ordre[-1])
print(cartes[ordre[-1]])
print(f"*** {s} * {v} = {answer}")

endtime = time.time()

print("===========================")
print("AOC 2021 - day 4 - puzzle 2")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
