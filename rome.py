#!/usr/bin/python
'''This is a solution to LasaCTF 2016 Cryptography problem, shifty-letters.
There is some gibberish letter characters interspersed with special
characters. This script simply adds a rotation number to the ASCII decimal
 of the character and prints that character representation. It does this 
for all 26 possible rotations including 0 :). I probably could have 
prevented the rotation of special characters, but this is simple and dirty.
Completed 25 March 2016 - Gary Butler.'''

import sys

string = "jtkw{ny3e_1e_tkw_u0_r5_tkw3i5_u0}"

for j in range(26):
	print(str(j) + ":")
	for i in string:
		if ord(i) == 32:
			sys.stdout.write(str(" "))
		elif i == "{":
			sys.stdout.write(str(i))
		elif i == "}":
			sys.stdout.write(str(i))
		elif i == "_":
			sys.stdout.write(str(i))
		elif i.isdigit():
			sys.stdout.write(str(i))
		else:
			sys.stdout.write(chr(((ord(i)+j)%26)+97)T)
	print
	print string
	print