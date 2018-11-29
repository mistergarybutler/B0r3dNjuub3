import sys

orig = str(sys.argv[1])
table = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z" , "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z" , "0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "+" , "/"]

def split(input, size):
    return [input[start:start+size] for start in range(0, len(input), size)]

hxls = []

for i in range(len(split(orig, 2))):
    hxls.append(int(split(orig, 2)[i], 16))

breq = 0
if (len(hxls) % 3) != 0:
    trailer = hxls[((len(hxls)/3)*3):]
    breq = 3 - len(trailer)
    for i in range(breq):
	    trailer.append(0)

storedByte = 0

print ""

for i in range(len(hxls)/3):
    for j in range(3):
            if j == 0:
                    sys.stdout.write(table[(split(hxls, 3)[i][j] >> 2)])
                    storedByte = split(hxls, 3)[i][j] & 3
            elif j == 1:
                    sys.stdout.write(table[((storedByte<<4) + (split(hxls, 3)[i][j]>>4))])
                    storedByte = (split(hxls, 3)[i][j] & 15) << 2
            elif j == 2:
                    sys.stdout.write(table[(storedByte + (split(hxls, 3)[i][j]>>6))])
                    sys.stdout.write(table[(split(hxls, 3)[i][j] & 63)])

if breq > 0:
    for i in range(3):
        if i == 0:
			sys.stdout.write(table[trailer[i]>>2])
			storedByte = (trailer[i] & 3)
        elif i == 1:
			sys.stdout.write(table[((storedByte<<4) + (trailer[i]>>4))])
			storedByte = ((trailer[i] & 15)<<2)
        elif i == 2:
			    if breq == 2:
			        sys.stdout.write("==")
			    else:
				    sys.stdout.write(table[storedByte + (trailer[i]>>6)])
				    sys.stdout.write("=")

print ""