#!/usr/bin/python

import sys

if len(sys.argv) <  2:
	sys.exit()

file = open("carter.jpg", "rb")
position = file.read().rfind("\xFF\xD8\xFF\xE0")
print type(position)
print str(position)
file.seek(position)
jpg = file.read()
out = open(sys.argv[1], "wb")
out.write(jpg)