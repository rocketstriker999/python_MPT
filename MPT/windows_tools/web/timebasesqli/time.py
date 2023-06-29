import urllib
import datetime
import time
import requests
import re
import os

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#     TIMEBASE BLIND SQL INJECTION TESTING      #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"

print("\nPLEASE ENTER URL OR WEBSITE E.g. http://www.xyz.vom/index.php?id=")
u=raw_input("[+]ENTER URL : ")
file2 =open('log'+'.txt','w')
fobj = open("payloads.txt")
for payloads in fobj:
    p= payloads.rstrip()
    t=u+p
    print "\n[*]TESTING URL WITH THIS PAYLOAD : ",t
    nf = requests.get(t).elapsed.total_seconds()
    print "[*]",nf,"Seconds"
    
    if nf > 7:
        print"\n[+]TIME BASE BLIND SQL INJECTION BUG FOUND AT : ",t
        print"[+]TIME TAKEN TO LOAD : ",nf,"Seconds"
        file2.write(t + '  :BUG WAS FOUND\n')
        
    

file2.close()

print"\nLOGS ARE SAVED IN TO log.txt FILE"
# end - start gives you the page load time
print"\n[+]YOU FOUND YOUR WEBSITE IN SQL INJECTION VULNRABLE???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DO WANT SOME HINTS TO STOP THIS ATTACK ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  FILTER META CHARACTERS [e.g. ',%,-- etc etc ] FROM YOUR WEB APPLIACTAION"
    print"\n[+]STEP 2.  MAKE YOUR DATABASE TO READ ONLY"
    print"\n[+]STEP 3.  TRY TO REDIRECT THE ERROR MESSAGES TO OTHER PLACE...THIS WILL MAKE WEB APPLICATION MORE SECURE"
    print'\n[+]STEP 4.  DO NOT ALLOW USERS TO EXECUTE OTHER QUERIES AFTER URL OR USE FIREWALL OR IDS'
    print"\n[+}STEP 5.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass
input("\nPRESS ANY KEY TO EXIT :")

