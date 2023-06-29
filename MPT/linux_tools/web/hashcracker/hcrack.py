
import os, sys ,hashlib

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#         HASH CRACKER (DICTONARY ATTACK)       #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
def encrymd5(pw,algo,fi):
	try:
		words = open(fi, "r")
	except(IOError): 
		print "\n[-]ERROR : FILE NOT FOUND\n"
		return
	words = words.readlines()
	print "\n[+]TOTAL WORDS IN DICTONARY ARE:",len(words)
	if algo == 'md5':
		for word in words:
			hash = hashlib.md5(word[:-1])
			value = hash.hexdigest()
			if pw == value: 
				print "\n[+]DECRIPTED VALUE :",word		
	elif algo == 'sha1':
		for word in words:
			hash = hashlib.sha1(word[:-1])
			value = hash.hexdigest()
			if pw == value: 
				print "\n[+]DECRIPTED VALUE :",word
	elif algo == 'sha256':
		for word in words:
			hash = hashlib.sha256(word[:-1])
			value = hash.hexdigest()
			if pw == value: 
				print "\n[+]DECRIPTED VALUE :",word
	elif algo == 'sha384':
		for word in words:
			hash = hashlib.sha384(word[:-1])
			value = hash.hexdigest()
			if pw == value: 
				print "\n[+]DECRIPTED VALUE :",word		
	elif algo == 'sha512':
		for word in words:
			hash = hashlib.sha512(word[:-1])
			value = hash.hexdigest()
			if pw == value: 
				print "\n[+}DECRIPTED VALUE :",word

hash = raw_input("\n[+}ENTER HASH VALUE : ")
fi = '../../../dictonary.txt'
print"\n[+]AVIABLE ALGORYTHEMS ARE md5,sha1,sha256,sha384,sha512"
algo = raw_input("\n[+]ENTER ALGORYTHEM : ")
encrymd5(hash,algo,fi)


raw_input("\n[+]PRESS ANY KEY TO EXIT")
