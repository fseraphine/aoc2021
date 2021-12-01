#!/usr/bin/python

import time
from more_itertools import windowed

starttime = time.time()

depths =[]

i=0
for a,b in windowed(map(sum, windowed(open('data_day1.txt'),3)),2):
    if a < b :
        i = i+1
print(i)


print("AOC 2021 - day 1 - puzzle 2")
print("inc:",i)
print("Temps d'éxécution:",time.time()-starttime)