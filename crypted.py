#!/usr/bin/python

import os, sys

if len(sys.argv) > 1:
	if (not os.path.isfile(sys.argv[1])):
		print(sys.argv[1] + " not found.")
	else:
		f = open(sys.argv[1], "rb").read()
		
		content = []
		for i in f:
			content.append(i.upper())

		changed = [ "F" for i in range(len(f))]
		for i in range(len(changed)):
			if changed[i]=="F" and content[i].isalnum():
				if content[i].lower() == "w":
					content[i] = "i"
					changed[i] = "T"
				elif content[i].lower() == "v":
					content[i] = "c"
					changed[i] = "T"
				elif content[i].lower() == "y":
					content[i] = "e"
					changed[i] = "T"
				elif content[i].lower() == "k":
					content[i] = "t"
					changed[i] = "T"
				elif content[i].lower() == "t":
					content[i] = "f"
					changed[i] = "T"
				elif content[i].lower() == "e":
					content[i] = "o"
					changed[i] = "T"
				elif content[i].lower() == "g":
					content[i] = "w"
					changed[i] = "T"
				elif content[i].lower() == "z":
					content[i] = "l"
					changed[i] = "T"
				elif content[i].lower() == "c":
					content[i] = "m"
					changed[i] = "T"					
				elif content[i].lower() == "m":
					content[i] = "n"
					changed[i] = "T"
				elif content[i].lower() == "o":
					content[i] = "r"
					changed[i] = "T"					
				elif content[i].lower() == "d":
					content[i] = "s"
					changed[i] = "T"
				elif content[i].lower() == "q":
					content[i] = "g"
					changed[i] = "T"
				elif content[i].lower() == "s":
					content[i] = "u"
					changed[i] = "T"
				elif content[i].lower() == "l":
					content[i] = "h"
					changed[i] = "T"
				elif content[i].lower() == "r":
					content[i] = "y"
					changed[i] = "T"
				elif content[i].lower() == "j":
					content[i] = "a"
					changed[i] = "T"
				elif content[i].lower() == "a":
					content[i] = "p"
				elif content[i].lower() == "u":
					content[i] = "d"
					changed[i] = "T"	
				elif content[i].lower() == "x":
					content[i] = "v"
					changed[i] = "T"	
				elif content[i].lower() == "i":
					content[i] = "k"
					changed[i] = "T"
				elif content[i].lower() == "b":
					content[i] = "b"
					changed[i] = "T"																																					

		for i in content:
			sys.stdout.write(i)
		for i in changed:
			sys.stdout.write(i)

else:
	print("No file name supplied.")