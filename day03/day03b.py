#!/usr/bin/python

import time
import tracemalloc
from numpy import transpose
from functools import reduce


starttime = time.time()
tracemalloc.start()

answer = 0
diag = []
emptystr=""

with open('data_day03.txt') as data:
    for line in data:
        diag.append(list(map(int,list(line.strip()))))

tdiag = transpose(diag)
w=len(diag[0])
l=len(diag)

idco = idcc = [x for x in range(l)]


for i in range(w):
    # compute the sum of ones (1) in the current bit column for o2
    ones = sum([ tdiag[i][k] for k in idco ])
    # and compare this sum to the nb of remaining lines valid for o2
    if(ones>= len(idco)/2):
        # we keep ones of o2 (idco) (idcc)
        idco = [j for j in idco if(tdiag[i][j]==1)]
    else:
        # we keep zeros of o2 (idco) (idcc)
        idco = [j for j in idco if(tdiag[i][j]==0)]
    
    # compute the total of ones (1) in the current bit column for co2
    ones = sum([ tdiag[i][k] for k in idcc ])
    # and compare this sum to the nb of remaining lines valid for co2
    if(ones>= len(idcc)/2):
        # we keep zeros for co2 (idcc)
        idcc = [j for j in idcc if(tdiag[i][j]==0)]
    else:
        # we keep ones for co2 (idcc)
        idcc = [j for j in idcc if(tdiag[i][j]==1)]
    
    # if there's only one value left, we compute the decimal value
    if (len(idco)==1):
        o2=reduce(lambda x,y:(x<<1)|y,diag[idco[0]])
    if (len(idcc)==1):
        co2=reduce(lambda x,y:(x<<1)|y,diag[idcc[0]])
    i +=1


answer = (o2,co2,o2*co2)

endtime = time.time()

print("===========================")
print("AOC 2021 - day 3 - puzzle 2")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
