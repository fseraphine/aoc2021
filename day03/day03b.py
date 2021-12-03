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

with open('ex_day03.txt') as data:
    for line in data:
        diag.append(list(map(int,list(line.strip()))))

tdiag = transpose(diag)
w=len(diag[0])
l=len(diag)

idco = [x for x in range(l)]
idcc = [x for x in range(l)]


for i in range(w):
    nb=(len(idco))/2
    ones = sum([ tdiag[i][k] for k in idco])
    print(f"{i=} - {ones=} - {nb=}")
    if(ones>= nb):
        # we keep ones
        idco = [j for j in idco if(tdiag[i][j]==1)]
        idcc = [j for j in idcc if(tdiag[i][j]==0)]
        print(f"keeping 1 - {idco=}")
        print(f"keeping 0 - {idcc=}")
    elif(ones<nb):
        # we keep zeros
        idco = [j for j in idco if(tdiag[i][j]==0)]
        idcc = [j for j in idcc if(tdiag[i][j]==1)]
        print(f"keeping 0 - {idco=}")
        print(f"keeping 1 - {idcc=}")
    # else:
    #     # we keep prefered value
    #     idco = [j for j in idco if(tdiag[i][j]==1)]
    #     idcc = [j for j in idco if(tdiag[i][j]==0)]
    #     print(f"keeping 1 - {idco=}")
    #     print(f"keeping 0 - {idcc=}")
    if (len(idco)==1):
        print("idco:",idco[0],diag[idco[0]])
        o2=reduce(lambda x,y:(x<<1)|y,diag[idco[0]])
    if (len(idcc)==1):
        print("idcc:",idcc[0],diag[idcc[0]])
        co2=reduce(lambda x,y:(x<<1)|y,diag[idcc[0]])
    for k in idco:
        print("idco ","".join(str(e) for e in diag[k]))
    for k in idcc:
        print("idcc ","".join(str(e) for e in diag[k]))
    i +=1


answer = (o2,co2,o2*co2)

endtime = time.time()

print("===========================")
print("AOC 2021 - day 3 - puzzle 1")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
