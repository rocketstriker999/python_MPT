import os
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#            WEB APPLICATION CRAWLER            #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
print"\n[+]ENTER A WEBSITE OR URL LIKE http://www.xyz.com/index.php"
d=raw_input("\n[+]URL OR WEBSITE : ")

f=' -w -i -C 5'
u='crawler.py -u '
s=u+d+f
print "\nCOMMAND GENERATED IN CRAWLER IS :",s
os.system(s)
