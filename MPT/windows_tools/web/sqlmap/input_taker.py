import os
print"ENTER A WEBSITE OR URL LIKE http://www.xyz.com/index.php"
d=raw_input("URL OR WEBSITE : ")
u='sqlmap.py -u '
s=u+d
print "\nCOMMAND GENERATED IN CRAWLER IS :",s
os.system(s)
