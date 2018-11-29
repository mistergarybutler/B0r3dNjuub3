#!/usr/bin/python

import os, sys

def split(input, size):
        return[input[start:start+size] for start in range(0, len(input), size)]

f = open("kek.txt", "rb")
content = f.read()

ls = content.split()

tab = {}
for i in ls:
	tab[i]=0

for i in ls:
	tab[i]+=1

freq = sorted(( k  for k,v in tab.iteritems()), reverse=True)
#print sorted(tab.keys())

matrix = {}
gen = "etaoinsrhldcum"
for i in range(len(freq)):
	matrix[freq[i]]=gen[i]

'''for i in ls:
	sys.stdout.write(matrix[i])'''

numbers=[]
for i in ls:
	count = 0
	for j in range(len(i)):
		if i[j]=="!":
			count+=1
	numbers.append(count)

eights = split(numbers,16)

for i in eights:
	summ=0
	for j in i:
		summ+=j
	sys.stdout.write(str(summ)+" ")

print

print ls
print sorted(( (v,k)  for k,v in tab.iteritems()), reverse=True)