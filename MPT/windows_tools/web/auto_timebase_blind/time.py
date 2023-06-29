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






f = open( "payloads.txt", "r" )
pay = []
for line in f:
    pay.append(line)

               
file2 =open('log for blind sql injection'+'.txt','w')
fobj = open("payloads.txt")
fobjj = open('log.txt','r')


for links in fobjj:
    u= links.rstrip()
    
    for payloads in pay:
        p= payloads.rstrip()
        t=u+p
        print "\n[*]TESTING URL WITH THIS PAYLOAD : ",t
        try:
            nf = requests.get(t).elapsed.total_seconds()
        except:
            pass
        print "[-]TIME TAKEN TO LOAD :",nf,"SECONDS"
        try:
            if nf > 7:
                print"\n\n\n[+]TIME BASE BLIND SQL INJECTION BUG FOUND AT : ",t,"\n\n\n"
                print"[+]TIME TAKEN TO LOAD : ",nf,"SECONDS"
                file2.write(t + '  :BUG WAS FOUND\n')
            
        except:
            pass
        
        

    

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
raw_input("\nPRESS ANY KEY TO EXIT :")

