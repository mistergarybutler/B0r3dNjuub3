from operator import itemgetter
import sys, os
from Crypto.Cipher import AES

#create split method
def split(input, size):
    return[input[start:start+size] for start in range(0, len(input), size)]

#create base64 list. The index is used to convert.	
list = []
for i in range(65,91):
	list.append(chr(i))
	
for i in range(65+32,91+32):
	list.append(chr(i))
	
for i in range(10):
	list.append(str(i))
	
list.append("+")
list.append("/")


#store input in string object
fo = open("aes_encrypted.txt", "r")
orig = fo.read()
orig = orig.replace("\n","")


#convert input b64 chars into index values
b64 = []
for i in orig:
	if i == "=":
		break
	else:
		b64.append(list.index(i))
		

#convert index values into binary stream
b64_bin = []
for i in b64:
    for j in range(6):
            if bool(i & (32>>j)) == True:
                    b64_bin.append(1)
            else:
                    b64_bin.append(0)
					

#convert every 8 bits in binary stream to byte size integers
bin2dec_enc = []
for i in range(len(b64_bin)/8):
    bin2dec_enc.append(0)

for i in range(len(b64_bin)/8):
    for j in range(8):
            bin2dec_enc[i] = bin2dec_enc[i] + ((split(b64_bin, 8)[i][j]) * (128>>j))
		

#convert decimal list into hexidecimal string, create decryptor object and print plaintext
ciphertext = ''.join(chr(i) for i in bin2dec_enc)
decryptor = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
print decryptor.decrypt(ciphertext)

