from operator import itemgetter
import sys

ltr = [ "E","T","A","O","I","N","S","R","H","L","D","C","U","M","F","P","G","W","Y","B","V","K","X","J","Q","Z" ]
num = [ "0.1249","0.0928","0.0804","0.0764","0.0757","0.0723","0.0651","0.0628","0.0505","0.0407","0.0382","0.0334","0.0273","0.0251","0.0240","0.0214","0.0187","0.088","0.086","0.0148","0.0105","0.0054","0.0023","0.008","0.0012","0.0009" ]

freq = {}
for i in range(len(ltr)):
	freq[ltr[i]] = num[i]


def split(input, size):
    return[input[start:start+size] for start in range(0, len(input), size)]					

asc = []
file = open('ciphertext', 'rb')
for i in range(1544):
	asc.append(ord(file.read(1)))
file.close()

ripper = ""
test = split(asc, 8)
for j in range(8):
#		print "Byte: " + str(j)
	test_Bytes = []
#		print len(split(asc, 8))-1
	for n in range(len(split(asc, 8))-1):
#				print "location: " + str(n) + ":" + str(j)
		test_Bytes.append(test[n][j])
		
	keys = {}
	for l in range(256):
		keys[l] = 0
	for key_try in range(256):
		for ct in range(len(test_Bytes)):
			if (chr(test_Bytes[ct] ^ key_try)) in freq:
					keys[key_try] = keys[key_try] + float(freq[chr(test_Bytes[ct] ^ key_try)])
			elif (chr(test_Bytes[ct] ^ key_try).upper()) in freq:
					keys[key_try] = keys[key_try] + float(freq[chr(test_Bytes[ct] ^ key_try).upper()])
	
	top_key_ctr = 0
	for key, value in sorted(keys.iteritems(), key=itemgetter(1),reverse=True):
		if top_key_ctr < 1:
#				sys.stdout.write("Key: %02x" % key)
			ripper = ripper + chr(key)
#				for ct in range(len(test_Bytes)):
#					sys.stdout.write(chr(key ^ test_Bytes[ct]))
#				print "\n\n"
			top_key_ctr += 1
#	for k in range(len(split(asc, 8))):
#		for n in range(8):
#			sys.stdout.write(str(split(asc, 8)[k][n]))
#		print
##	print len(split(asc, 8)[0])
##	print split(asc, 8)[-2]
##	print split(asc, 8)[-1]
#	for j in range(8):
#		sys.stdout.write(str(8[j]))
#		print
#print ripper
#print type(ripper)
#    print str(split(asc, KEYSIZE)[0]) + " " + str(split(asc, KEYSIZE)[1])

#print len(split(asc, KEYSIZE)[0])
from Crypto.Cipher import DES
IV = '13245678'
decryptor = DES.new("000000v", DES.MODE_OFB, IV)
f =  open('ciphertext', 'r')
cyphertext = f.read()
print decryptor.decrypt(cyphertext)