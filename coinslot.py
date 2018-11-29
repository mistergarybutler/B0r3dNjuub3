#!/usr/bin/python

import socket, sys, os
from decimal import *

getcontext().prec = 1

s = socket.socket()
host = "misc.chal.csaw.io"
port = 8000
s.connect((host, port))
r = s.recv(1024)
#print r
r1 = float(r.split()[0].lstrip("$"))
print r1
r = r.split()[1]
#print r

def decomp(d):
#	print type(r1)
#	print type(d)
	print r1
	print type(r1)
	ans = (int(r1)/int(d))
#	ans = int(ans)
	print ans
	print type(ans)
	rmdr = Decimal.__float__(Decimal(r1)%Decimal(d))
	s.send(str(ans) + "\n")
	print
	print ans
	print rmdr
	print type(rmdr)
	print
	r = s.recv(1024)
	print r
#	print "passed r!"
	return rmdr

while 1:
	print("Printing resultant r1: " + str(r1))
	if '10,000' in r:
		r1 = decomp(10000)
	elif '5,000' in r:
		r1 = decomp(5000)
	elif '1,000' in r:
		r1 = decomp(1000)
	elif '500' in r:
		r1 = decomp(500)
	elif '100' in r:
		r1 = decomp(100)
	elif '50' in r:
		r1 = decomp(50)
	elif '20' in r:
		r1 = decomp(20)
	elif '10' in r:
		r1 = decomp(10)
	elif '5' in r:
		r1 = decomp(5)
	elif '1' in r:
		r1 = decomp(1)
	elif '50c' in r:
		r1 = decomp(.5)
	elif '25c' in r:
		r1 = decomp(.25)
	elif '10c' in r:
		r1 = decomp(.1)
	elif '(5c)' in r:
		r1 = decomp(.05)
	elif '1c' in r:
		r1 = decomp(.01)


'''$10,000 bills: 0
$5,000 bills: 0
$1,000 bills: 0
$500 bills: 0
$100 bills: 0
$50 bills: 0
$20 bills: 0
$10 bills: 0
$5 bills: 0
$1 bills: 0
half-dollars (50c): 0
quarters (25c): 0
dimes (10c): 1
nickels (5c): 0
pennies (1c): 0
'''