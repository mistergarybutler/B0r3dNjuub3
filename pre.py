from operator import itemgetter
import sys


if len(sys.argv) != 2:
	print
#	print "%s" % sys.argv[0]
	print "Use: The first argument is a bitmask for output display."
	print "     This does not control processing."
	print
	print "     1 == base64 table."
	print "     2 == frequency table."
	print "     4 == encrypted base64 string."
	print "     8 == encrypted b64 decimal list."
	print "     16 == encrypted intermediary binary list." 
	print "     32 == encrypted decimal list."
	print
	sys.exit()

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

if bool(1 &  int(sys.argv[1])) == True:
	print "base64 table\n========================"
	print list
	print

#create letter frequency dictionary
ltr = [ "E","T","A","O","I","N","S","R","H","L","D","C","U","M","F","P","G","W","Y","B","V","K","X","J","Q","Z" ]
num = [ "0.1249","0.0928","0.0804","0.0764","0.0757","0.0723","0.0651","0.0628","0.0505","0.0407","0.0382","0.0334","0.0273","0.0251","0.0240","0.0214","0.0187","0.0168","0.0166","0.0148","0.0105","0.0054","0.0023","0.0016","0.0012","0.0009" ]

freq = {}
for i in range(len(ltr)):
	freq[ltr[i]] = num[i]

if bool(2 &  int(sys.argv[1])) == True:
	print "frequency table\n========================"
	print freq
	print

#store input in string object
fo = open("encrypted.txt", "r")
orig = fo.read()
orig = orig.replace("\n","")

if bool(4 &  int(sys.argv[1])) == True:
	print "base64 string\n========================"
	print orig
	print

#convert input b64 chars into index values
b64 = []
for i in orig:
	if i == "=":
		break
	else:
		b64.append(list.index(i))
		
if bool(8 &  int(sys.argv[1])) == True:
	print "b64 decimal list\n========================"
	print b64
	print

#convert index values into binary stream
b64_bin = []
for i in b64:
    for j in range(6):
            if bool(i & (32>>j)) == True:
                    b64_bin.append(1)
            else:
                    b64_bin.append(0)
					
if bool(16 &  int(sys.argv[1])) == True:
	print "intermediary binary list\n========================"
	print b64_bin
	print

#convert every 8 bits in binary stream to byte size integers
bin2dec_enc = []
for i in range(len(b64_bin)/8):
    bin2dec_enc.append(0)

for i in range(len(b64_bin)/8):
    for j in range(8):
            bin2dec_enc[i] = bin2dec_enc[i] + ((split(b64_bin, 8)[i][j]) * (128>>j))

if bool(32 &  int(sys.argv[1])) == True:			
	print "decimal list\n========================"
	print bin2dec_enc
	print

##hamming
#for every keysize
#	for the every keysize block in the ciphertext minus one (dont' exceed range)
#		for every pair of blocks
#			XOR the blocks
#				+1 to a counter for enabled(1) bits
#					store counter in list
#	average the elements in the counter list
#	normalize the average
#	+the norm average to a dictionary where the key is the keysize
#sort the dictionary by the norm average

'''for keysize in range(2,41):
		for block in range(0,len(bin2dec_enc)/keysize,keysize):
		print block'''

##frequency decryption
#for each top keysize in the dictionary
#	create key/n:keysize table|dict
#	for each n:keysize in ciphertext
#		for each 0:255 key
#			XOR n with key
#			if XOR is in freq dict:
#				+freq float to key -|- n (intersect) table|dict.

#print a list of n:keysize indexes separated by tabs
#print the top key for each n separated by tabs
#XOR n:keysize ciphertext byte by the top key
#print each chr(XOR) separated by tabs

#If the output doesn't look right implement the ability to choose the
# next probably key key -|- n intersect

