#!/usr/bin/python

import sys

if len(sys.argv) <  2:
	sys.exit()

file = open("eyeofthetiger.png", "rb")
position = file.read().find("\x89\x50\x4e\x47")
file.seek(position)
png = file.read()
out = open(sys.argv[1], "wb")
out.write(png)