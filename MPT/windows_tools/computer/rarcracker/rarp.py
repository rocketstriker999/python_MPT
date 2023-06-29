import zipfile
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#           ZIP AND RAR PASSWORD CRACKER        #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"

fobj = open("../../../dictonary.txt",'r')
zip1=raw_input("\n[+]PLEASE ENTER FILE NAME (e.g. eee.zip) :")
zpp='../../../'+zip1
zip = zipfile.ZipFile(zpp)

for pas in fobj:
    p= pas.rstrip()
    print"\n[+]TRYING :",p
    zip.setpassword(p)
    try:
        zip.extractall()
        print "\n\n\n[+]PASSWORD FOUND : ",p,"\n\n\n"
        break
    except:
        pass
        


raw_input("[+]PLEASE ENTER ANY KEY TO EXIT")


