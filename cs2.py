#!/usr/bin/python

import socket

s = socket.socket()
host = "misc.chal.csaw.io"
port = 8000
s.connect((host, port))
r = s.recv(1024).split()
r = r[0:2]
for i in range(len(r)):
	r[i] = r[i].strip("$")
	r[i] = r[i].replace(",","")
	r[i] = float(r[i])
print r

bills = [10000, 5000, 1000, 500, 100, 50, 20, 10, 5, 1, .5, .25, .1, .05, .01]

ls = []
for i in bills:
	ls.append(int(r[0]/i))
	r[0] = round(r[0]%i, 2)
	print(str(i) + ":\t" + str(ls) + "\t" + str(r[0]))

print r

for i in ls:
	print i
	s.send(str(i) + "\n")
	r = s.recv(1024).split()
	print r

while 1:
	print "Here we go!"
	print r
#	for i in range(len(r)):
#		print type(r[i])
	r[1] = r[1].strip("$")
	r[1] = r[1].replace(",","")
	r[1] = float(r[1])

	ls = []
	for i in bills:
		ls.append(int(r[1]/i))
		r[1] = round(r[1]%i, 2)
		print(str(i) + ":\t" + str(ls) + "\t" + str(r[1]))

	print r

	for i in ls:
#		print i
		s.send(str(i) + "\n")
		r = s.recv(1024).split()
#		print r

