

import sys
import hashlib


print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#                  HASH MAKER                   #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
pw = raw_input("\n[+]PLEASE ENTER SOMETHING FOR HASHING :")

hash = hashlib.md5(pw)
print "\n[+]MD5 HASH :",hash.hexdigest(),"\n"

hash = hashlib.sha1(pw)
print "[+]SHA1 HASH :",hash.hexdigest(),"\n"

hash = hashlib.sha224(pw)
print "[+]SHA224 HASH :",hash.hexdigest(),"\n"

hash = hashlib.sha256(pw)
print "[+]SHA256 HASH :",hash.hexdigest(),"\n"

hash = hashlib.sha384(pw)
print "[+]SHA384 HASH :",hash.hexdigest(),"\n"

hash = hashlib.sha512(pw)
print "[+]SHA512 HASH :",hash.hexdigest(),"\n"

raw_input("\n[+]PRESS ANY KEY TO EXIT")
