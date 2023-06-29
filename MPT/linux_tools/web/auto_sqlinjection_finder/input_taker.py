import os
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#            AUTO SQL LOOP HOLE FINDER          #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
print"\n[+]ENTER A WEBSITE OR URL LIKE http://www.xyz.com/index.php"
print"\n[+]I WILL CALL THE CRAWLER FIRST AND THEN I WILL TEST FOR ALL URLS"
d=raw_input("\n[+]URL OR WEBSITE : ")
f=' -w -C 5'
u='python crawler.py -u '
s=u+d+f
print "\nCOMMAND GENERATED IN CRAWLER IS :",s
os.system(s)

print"\n[+]NOW CALLING SQL INJECTION TESTER...PLEASE WAIT"
t='python link_sqli_tester.py'
os.system(t)
