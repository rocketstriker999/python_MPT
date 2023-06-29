import os
import time
print "\n\t\t#################################################"
print "\t\t#                   AUTOMATIC                   #"
print "\t\t#   SQL INJECTION & LFI LINKS FETCHER UTILITY   #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"

print"\n[+]GETHERRING ALL DORKS AND TOOLS...PLEASE WAIT..."



i=raw_input("\n[+]PLEASE ENTER PERAMETER....(e.g. id=,cat=,item=...) :")
s=raw_input("\n[+]PLEASE ENTER DOMAIN NAME TO SEARCH...(e.g. com,lk,pk...) :")
f=raw_input("\n[+]PLEASE ENTER SOURCE TYPE...(e.g. php,asp,jsp...) :")

main='python search.py -i'+' '+i+' '+'-s'+' '+s+' '+'-f'+' '+f
print main
os.system(main)
