#!/usr/bin/python

import time
from more_itertools import windowed
import tracemalloc

starttime = time.time()
tracemalloc.start()

depths =[]
variations = []
i=1

fichier = open('data_day1.txt')
for l in fichier:
	depths.append(int(l))

sums = []
while i < len(depths)-1:
    sums.append(sum(depths[i-1:i+2:1]))
    i=i+1
#print(sums)

i=1
while i < len(sums):
    if (sums[i]>sums[i-1]):
        variations.append("i")
    else: 
        variations.append("d")
    i=i+1
#print(variations)
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

endtime = time.time()

print("AOC 2021 - day 1 - puzzle 2")
print("*** inc",variations.count("i"),"dec",variations.count("d"))
print("Temps d'éxécution:",endtime-starttime)