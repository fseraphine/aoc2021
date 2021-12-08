#!/usr/bin/python

import time
import tracemalloc
import numpy as np


starttime = time.time()
tracemalloc.start()

answer = 0
sigs = []
outs = []
pattern = { 1:"cf", 2:"acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6: "abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg" }

# with open('ex_day08.txt') as data:
#     for line in data.readlines():
#         (s, o) = line.strip().split("|")
#         sigs.append(np.array(s.strip().split(" ")))
#         outs.append(o.strip().split(" "))


mytest = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |cdfeb fcadb cdfeb cdbaf"
(s, o) = mytest.strip().split("|")
sigs.append(np.array(s.strip().split(" ")))
outs.append(o.strip().split(" "))

e = sigs[0]

cond = np.char.str_len(e) == len(pattern[1])
r1 = np.extract(cond,e)
print("1:",r1)

cond = np.char.str_len(e) == len(pattern[4])
r4 = np.extract(cond,e)
print("4:",r4)

cond = np.char.str_len(e) == len(pattern[7])
r7 = np.extract(cond,e)
print("7:",r7)

cond = np.char.str_len(e) == len(pattern[8])
r8 = np.extract(cond,e)
print("8:",r8)


endtime = time.time()

print("===========================")
print("AOC 2021 - day 8 - puzzle 2")
print(f"*** Answer : {answer}")
print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
