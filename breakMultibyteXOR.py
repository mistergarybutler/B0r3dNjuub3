from operator import itemgetter
import sys
list = []
for i in range(65,91):
	list.append(chr(i))
	
for i in range(65+32,91+32):
	list.append(chr(i))
	
for i in range(10):
	list.append(str(i))
	
list.append("+")
list.append("/")

ltr = [ "E","T","A","O","I","N","S","R","H","L","D","C","U","M","F","P","G","W","Y","B","V","K","X","J","Q","Z" ]
num = [ "0.1249","0.0928","0.0804","0.0764","0.0757","0.0723","0.0651","0.0628","0.0505","0.0407","0.0382","0.0334","0.0273","0.0251","0.0240","0.0214","0.0187","0.0168","0.0166","0.0148","0.0105","0.0054","0.0023","0.0016","0.0012","0.0009" ]

freq = {}
for i in range(len(ltr)):
	freq[ltr[i]] = num[i]

print list

fo = open("encrypted.txt", "r")
orig = fo.read()
orig = orig.replace("\n","")
#orig = "HUIf"

#print "Length of ciphertext: " + str(len(orig)) + "\nLength /4: " + str(len(orig)/4) + "\nLength mod 4: " + str(len(orig)%4)

b64 = []
for i in orig:
	if i == "=":
		break
	else:
		b64.append(list.index(i))

print "Length of ciphertext b64: " + str(len(b64)) + "\nLength /4: " + str(len(b64)/4) + "\nLength mod 4: " + str(len(b64)%4)
#print str(b64)
	
b64_bin = []
for i in b64:
    for j in range(6):
            if bool(i & (32>>j)) == True:
                    b64_bin.append(1)
            else:
                    b64_bin.append(0)

print "Length of ciphertext b64_bin: " + str(len(b64_bin)) + "\nLength /8: " + str(len(b64_bin)/8) + "\nLength mod 8: " + str(len(b64_bin)%8)					
#print str(b64_bin)
					
def split(input, size):
    return[input[start:start+size] for start in range(0, len(input), size)]					
					
asc = []
for i in range(len(b64_bin)/8):
    asc.append(0)

print len(asc)

for i in range(len(b64_bin)/8):
    for j in range(8):
            asc[i] = asc[i] + ((split(b64_bin, 8)[i][j]) * (128>>j))
			
#print asc

prob_key = []
for KEYSIZE in range(2,41):
    pk = []
#   print "Num Elements: " + str(len(asc)/KEYSIZE)
    avg_hamm = []
    for element in range(len(asc)/KEYSIZE):
		hammer = []
#		print "Element Pair: " + str(element) + ":" + str(element+1)
		if element+1 < len(asc)/KEYSIZE:
			for i in range(len(split(asc, KEYSIZE)[element])):
				hammer.append((split(asc, KEYSIZE)[element][i]) ^ (split(asc, KEYSIZE)[element+1][i]))
#			print "Hammed bytes: " + str(split(asc, KEYSIZE)[element])
#			print "Hammed bytes+1: " + str(split(asc, KEYSIZE)[element+1])
#			print "Hammer: " + str(hammer)
			
			hamm = 0
			for o in range(len(hammer)):
				for p in range(8):
					if bool(hammer[o] & (128>>p)) == True:
						hamm +=1
#			print "Hamm: " + str(hamm)
			avg_hamm.append(hamm)
#    print avg_hamm
    hamm = sum(avg_hamm)/len(avg_hamm)

    pk = [ KEYSIZE, hamm, hamm/KEYSIZE, hamm % KEYSIZE ]
    prob_key.append(pk)
#    print "Keysize: " + str(KEYSIZE) + "\tHamm: " + str(hamm) + "\tNormalized: " + str(hamm/KEYSIZE) + "\tRemainder: " + str(hamm % KEYSIZE)

print "\n" + str(prob_key) + "\n"
print "Candidates: " + str(sorted(prob_key, key=itemgetter(2,3))[0:3])
print
candidates = sorted(prob_key, key=itemgetter(2,3))[0:5]
for i in candidates:
	print "KEYSIZE: " + str(i[0])
	print "Num KEYSIZE elements: " + str(len(split(asc, i[0])))
	test = split(asc, i[0])
	for j in range(i[0]):
#		print "Byte: " + str(j)
		test_Bytes = []
#		print len(split(asc, i[0]))-1
		for n in range(len(split(asc, i[0]))-1):
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
				sys.stdout.write("%02x" % (key))
#				for ct in range(len(test_Bytes)):
#					sys.stdout.write(chr(key ^ test_Bytes[ct]))
#				print "\n\n"
				top_key_ctr += 1
#	for k in range(len(split(asc, i[0]))):
#		for n in range(i[0]):
#			sys.stdout.write(str(split(asc, i[0])[k][n]))
#		print
##	print len(split(asc, i[0])[0])
##	print split(asc, i[0])[-2]
##	print split(asc, i[0])[-1]
#	for j in range(i[0]):
#		sys.stdout.write(str(i[0][j]))
#		print
	print 
#    print str(split(asc, KEYSIZE)[0]) + " " + str(split(asc, KEYSIZE)[1])

#print len(split(asc, KEYSIZE)[0])
	

#Test Hamming Code
'''wordA = "this is a test"
wordB = "wokka wokka!!!"

wA = []
wB = []
for i in wordA:
    wA.append(ord(i))

for i in wordB:
    wB.append(ord(i))

bool(len(wA) == len(wB))
	
wC = []
for i in range(len(wA)):
    wC.append(wA[i] ^ wB[i])
	
hamm = 0
for i in range(len(wC)):
    for j in range(8):
            if bool(wC[i] & (128>>j)) == True:
                    hamm += 1
					
print hamm'''
