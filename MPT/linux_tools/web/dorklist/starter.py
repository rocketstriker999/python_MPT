

import os


print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#                 DORKs --- LIST                #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"

print"\n[+]FOR ADMIN PANEL DORKS PRESS 1"
print"\n[+]FOR LFI DORKS PRESS 2"
print"\n[+]FOR SQL INJECTION DORKS PRESS 3"

u=raw_input("\n[+]PLEASE ENTER CHOICE :")
if u=='1':
	os.system('python adminpaneldork.py')
elif u=='2':
	os.system('python lfidork.py')
elif u=='3':
	os.system('python sqlinjectiondork.py')
raw_input("\n[+]PRESS ANY KEY TO EXIT")
