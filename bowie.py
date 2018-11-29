#!/usr/bin/python
import sys
import subprocess

file = open(sys.argv[1], 'rb')
fcon = file.read()
#print(fcon)

def aline(content):
	alines = content.splitlines()
	l1 = []
	for i in alines:
		if '$input eq' in i:
			l1.append(i.lstrip())
	#		print(i.lstrip())
	#		print(str(i.lstrip().find('(')) + " " + str(i.lstrip().rfind(')')))
	l2 = []
	for i in range(len(l1)):
		l2.append(l1[i][l1[i].find('(')+1:l1[i].rfind(')')])

	l3 = []
	for i in range(len(l2)):
		l3.append(l2[i][l2[i].find('(')+1:l2[i].rfind(')')])

#	print l3

	l4 = []
	for i in l3:
		l4.append(eval(i.replace('.', '+')))
#		for j in word:
#			l4.append(sys.stdout.write(eval(j)))
#			sys.stdout.write(eval(j))
#		print

	return l4

#aline(fcon.splitlines())
#print(fcon.splitlines())

def eline(content):
	elines = content.splitlines()
	l1 = []
	for i in elines:
		if 'eval' in i:
			l1.append(i.lstrip())
	
	l2 = []
	for i in range(len(l1)):
		l2.append(l1[i][l1[i].find('(')+1:l1[i].rfind(')')])

	l3 = []
	for i in l2:	
		l3.append(i.decode('base64'))

	return l3[0]

#	for i in l3:
#		print i

#print type(eline(fcon.splitlines()))
#for i in aline(fcon.splitlines()):
#	print i

def rec(content):
	al = [aline(content)]
	print al
	el = [eline(content)]
	print el

	return rec(el)

rec(fcon)

#print aline(eline(fcon))[0]
#print eline(eline(fcon.splitlines()).splitlines())
