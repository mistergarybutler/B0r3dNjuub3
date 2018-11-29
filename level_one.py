#!/usr/bin/python
import sys
import socket
import time

plaintext = ""

def print_alnum():
	pt = ""
#	for i in range(65,65+25,1):
#		pt = pt + chr(i)

	for i in range(65,65+25,1):
		pt = pt + (chr(i).lower())

#    for i in range(10):
#    	pt = pt + str(i)

	return pt

plaintext = plaintext + print_alnum()
plain_list = []

for i in plaintext:
	plain_list.append(i)

#print plain_list

#print plaintext

target_host = "146.148.102.236"
target_port = 24069
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
response = client.recv(4096)
print response

client.send("%s\n" % plaintext)

response = client.recv(4096)
print response

def decrypt(response):
	response_list = response.split("\n")

	key = {}
	for i in range(len(plain_list)):
		key[response_list[0].split()[3:][i]] = plain_list[i]

	#print key['.-']
	decrypted = ""
	#sys.stdout.write(response_list[1][2:-1])#.split()[2:-1]

	char = ""
	for i in response_list[1][response_list[1].find(" ",response_list[1].find(" ")+1)+1:response_list[1].rfind("decrypted")]:
	#	print(ord(i))
		if i != " ":
			char = char + i

		else:
	#		print char
			if char in response_list[0].split()[3:]:
				decrypted = decrypted + key[char]
				char = ""
				decrypted = decrypted + " "
			else:
				char = ""
				decrypted = decrypted + "*"
				decrypted = decrypted + " "

	#print decrypted
	decrypted = decrypted.replace(" ","")
	decrypted = decrypted.replace("**"," ")
	decrypted = decrypted.replace("*","")
	return decrypted

outer_decrypted = decrypt(response)
print outer_decrypted
client.send("%s\n" % outer_decrypted)
#time.sleep(5)

response = client.recv(4096)
print response

def challenge_response(plaintext, response):
	client.send("%s\n" % plaintext)

	response = client.recv(4096)
	print response

	outer_decrypted = decrypt(response)
	print outer_decrypted
	client.send("%s\n" % outer_decrypted)

	response = client.recv(4096)
	print response

for i in range(49):
	challenge_response(plaintext, response)

#client.send("%s\n" % "z0123456789-")
#response = client.recv(4096)
#print response

for i in range(49):
	key = {}
	decrypted = ""
	client.send("%s\n" % plaintext)
	response = client.recv(4096)
	print response
	strA = "abcdefghijklmnopqrstuvwxyz0123456789-"
	strB = "nopqrstuvwxyz{|}~ !\"#$%&'(=>?@ABCDEF:"
	for i in range(len(strA)):
		key[repr(strB[i]).replace("'","")] = strA[i]
	print key
	response_list = response.split("\n")
	encrypted = response_list[1][response_list[1].find(" ",response_list[1].find(" ")+1)+1:response_list[1].rfind("decrypted")]
	for i in range(len(encrypted)):
		decrypted = decrypted + key[repr(encrypted[i]).replace("'","")]
	print decrypted
	client.send("%s\n" % decrypted)
	response = client.recv(4096)
	print response



client.close()