import sys
#orig = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
if len(sys.argv) < 3:
	if len(sys.argv) == 2:
		fo = open(sys.argv[1], "r", 1)
#		orig = sys.argv[1]
		max_key_ctr = 10
	else:
		print ""
		print "You must supply a string of hex characters and max keys to try."
		print "Example: " + sys.argv[0] + " <hex string> <max keys>"
		print ""
		sys.exit()
else:
	fo = open(sys.argv[1], "r", 1)
#	orig = sys.argv[1]
	max_key_ctr = int(sys.argv[2])


def split(input, size):
	return[input[start:start+size] for start in range(0, len(input), size)]

count = 1
for orig in fo:
	print "Line is: " + str(count)
	print "============"
	ct_list = []
	for i in range(len(split(orig, 2))-1):
		ct_list.append(int(split(orig, 2)[i], 16))
		
	ltr = [ "E","T","A","O","I","N","S","R","H","L","D","C","U","M","F","P","G","W","Y","B","V","K","X","J","Q","Z" ]
	num = [ "0.1249","0.0928","0.0804","0.0764","0.0757","0.0723","0.0651","0.0628","0.0505","0.0407","0.0382","0.0334","0.0273","0.0251","0.0240","0.0214","0.0187","0.0168","0.0166","0.0148","0.0105","0.0054","0.0023","0.0016","0.0012","0.0009" ]

	freq = {}
	for i in range(len(ltr)):
		freq[ltr[i]] = num[i]

##move keys up one level
	keys = {}
##the number of elements in keys needs to equal num lines * 256
	for i in range(256):
		keys[i] = 0
		
	for key_try in range(256):
		for ct in range(len(ct_list)):
				if (chr(ct_list[ct] ^ key_try)) in freq:
						keys[key_try] = keys[key_try] + float(freq[chr(ct_list[ct] ^ key_try)])
				elif (chr(ct_list[ct] ^ key_try).upper()) in freq:
						keys[key_try] = keys[key_try] + float(freq[chr(ct_list[ct] ^ key_try).upper()])
#		print "Sum of Key(" + str(key_try) + "): " + str(keys[key_try])
		
	from operator import itemgetter
	top_key_ctr = 0
	for key, value in sorted(keys.iteritems(), key=itemgetter(1),reverse=True):
		if top_key_ctr < max_key_ctr:
			sys.stdout.write("Key: " + str(key) + " ")
			for ct in range(len(ct_list)):
				sys.stdout.write(chr(key ^ ct_list[ct]))
			print ""
			top_key_ctr += 1
#			print value
	print ""
	count +=1
	
#next you need to output to a dict(line,key,value)

#example people = {}
#people[ "ryan" ] = 8, "lot"
#people["ryan"][0]

#then you sort by value
#then you choose the first n lines
#then you xor all of the bytes in those lines by your key, printing as you go