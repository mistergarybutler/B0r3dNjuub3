#!/usr/bin/python

import sys

strA = "RNFLPGS{LBHTBGVG}"

for i in range(26):
	for j in range(len(strA)):
		if strA[j] != " ":
			sys.stdout.write(chr(((ord(strA[j]) - 97) + i) % 26 + 97))
		else:
			sys.stdout.write(" ")
	print(str("\n^Rot:") + str(i))