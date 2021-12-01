#!/usr/bin/python

depths =[]
variations = []
i=1

fichier = open('data_day1.txt')
for l in fichier:
	depths.append(int(l))


while i < len(depths):
    if (depths[i]>depths[i-1]):
        variations.append("i")
    else: 
        variations.append("d")
    i=i+1
print("inc",variations.count("i"),"dec",variations.count("d"))