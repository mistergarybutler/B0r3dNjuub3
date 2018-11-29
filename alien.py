#!/usr/bin/python
#english.txt found at http://www.wordgamedictionary.com/english-word-list/download/english.txt for now...
#http://wordsolver.net

import sys, os

f = open("8letterwords.txt", "rb")
words = []
for i in f:
	words.append(i)

#print words

'''for i in words:
	if len(i)==5:
		if i[1]==i[2] and i[0]!=[3] and i[0]!=i[1] and i[2]!=i[3]:
			print(i.rstrip())

print("")

for i in words:
	if len(i)==5:
		if i[0]!=i[1] and i[0]!=i[2] and i[0]!=i[3] and i[1]!=i[2] and i[1]!=i[3] and i[2]!=i[3]:
			print(i.rstrip())

print("")'''

for i in words:
	if len(i)==9:
		if i[0]==i[7] and i[2].lower()=="e" and i[0]!=i[1] and i[0]!=i[2] and i[0]!=i[3] and i[0]!=i[4] and i[0]!=i[5] and i[0]!=i[6] and i[1]!=i[2] and i[1]!=i[3] and i[1]!=i[4] and i[1]!=i[5] and i[1]!=i[6] and i[1]!=i[7] and i[2]!=i[3] and i[2]!=i[4] and i[2]!=i[5] and i[2]!=i[6] and i[2]!=i[7] and i[3]!=i[4] and i[3]!=i[5] and i[3]!=i[6] and i[3]!=i[7] and i[4]!=i[5] and i[4]!=i[6] and i[4]!=i[7] and i[5]!=i[6] and i[5]!=i[7] and i[6]!=i[7] and "C" not in i and "I" not in i and "T" not in i and "F" not in i:
			print(i.rstrip())

for i in words:
	if len(i)==9:
		if i[1]==i[3] and i[0].lower()=="f":
			print(i[4])