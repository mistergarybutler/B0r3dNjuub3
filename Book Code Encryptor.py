from itertools import izip, cycle
import base64
import sys


def cleanUp(key):
    tempKey=key.lower()
    finalKey = ""
    for each in tempKey:
        if each in "abcdefghijklmnopqrstuvwxyz":
            finalKey +=each
    return finalKey


def charUNXOR(char1, char2):
    if char1==' ':
        return ' '
    int1 = ord(char1)-96
    int2 = ord(char2)-96
    int3 = (int1-int2)
    if int3<1:
        return chr((int3+26)+96)
    return chr(int3+96)


def charXOR(char1, char2):
    if char1==' ':
        return ' '
    int1 = ord(char1)-96
    int2 = ord(char2)-96
    int3 = (int1+int2)
    if int3>26:
        return chr((int3-26)+96)
    return chr(int3+96)

#main
with open('toEncrypt.txt', 'r') as file:
    toEncrypt = file.read()
    toEncrypt = toEncrypt.lower()
    toEncrypt=toEncrypt.rstrip('\n')

with open('crackstation-human-only.txt', 'r') as file:
    
    while 
    keyFile = file.readlines()
    keyFile=keyFile.replace('\n','')
    for i in keyfile:
        keyFile=cleanUp(i)


print "**********************Key File*************************"
print keyFile
print "**********************End Key File*************************"
print "**********************Encrypt File*************************"
print toEncrypt
print "**********************End Encrypt File*************************"
encrypted = ''.join(charXOR(char1,char2) for (char1,char2) in izip(toEncrypt, cycle(keyFile)))
print "**********************Encrypted Text*************************"
print encrypted
print "**********************End Encrypted Text*********************"
print "**********************Decrypted Text*************************"
decrypted = ''.join(charUNXOR(char1,char2) for (char1,char2) in izip(encrypted, cycle(keyFile)))
print decrypted
print "**********************End Decrypted Text*********************"
