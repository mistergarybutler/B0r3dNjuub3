#!/usr/bin/python

import itertools
import subprocess
import sys

dances = ["whip","naenae"]

for i in list(itertools.product(dances, repeat=14)):
	moves = ''
	for j in range(len(i)):
			if j != (len(i)-1):
				moves = moves + i[j] + ","
			else:
				moves = moves + i[j]
	sys.stdout.write(".")
	run = subprocess.check_output("printf '%s' | ./dance_noflag" % moves, shell=True)
	if "vip lounge" in run:
			print moves
			break