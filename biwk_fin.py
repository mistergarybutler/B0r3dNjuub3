#!/usr/bin/python

import os, sys

input = sys.argv
#print(input)
args = input[1:len(input)]
#print(args)

def is_numeric_inc_pts(s):
	try:
		float(s)
	except ValueError:
		return False
	return True

def schedule(balance, month, extra):
	interest=balance*periodicrate
#	print("\t\t" + str(interest))
	principal=pai-interest
	balance=balance-principal-(extra/2)
	interest=interest+(balance*periodicrate)
	print("\t\t" + str(interest))
	balance=balance-(extra/2)
	month+=1
	print("Month " + str(month) + " balance: " + str(balance))
#	print("\t\t" + str(principal))
	while(balance>0):
		return(schedule(balance, month, extra))

switchCt = 0
for i in range(len(args)):
	if (("-" in args[i])==False):
		switchCt+=1
if switchCt==len(args):
	print("Please supply switches.\nSee documentation for further information.")
	sys.exit(1)


if len(args)%2==0:
	for i in range(len(args)-1):
		if (args[i]=="-balance") and is_numeric_inc_pts(args[i+1]):
			balance=float(args[i+1])
		elif (args[i]=="-rate") and is_numeric_inc_pts(args[i+1]):
			rate=float(args[i+1])
		elif (args[i]=="-tax") and is_numeric_inc_pts(args[i+1]):
			tax=float(args[i+1])
		elif (args[i]=="-payment") and is_numeric_inc_pts(args[i+1]):
			payment=float(args[i+1])
		elif (args[i]=="-extra") and is_numeric_inc_pts(args[i+1]):
			extra=float(args[i+1])
else:
	print("Please pair your arguments.")

try:
	balance, rate, tax, payment
except:
	print("The required arguments were not supplied.")
	sys.exit(1)

try:
	extra
except:
	extra=float(0)

periodicrate=((rate/100)/365)*((365/12)/2)
#print("Monthly rate:\t\t\t" + str(periodicrate))

#pai == principal and interest
pai=payment-tax
#print("Principal and Interest:\t\t\t" + str(pai))

interest=balance*periodicrate
#print("Interest:\t\t\t" + str(interest))

principal=pai-interest
#print("Principal:\t\t\t" + str(principal))

balance=balance-principal-(extra/2)
month=1
print("Month " + str(month) + " balance: " + str(balance))
#print("\t\t" + str(principal))

schedule(balance, month, extra)