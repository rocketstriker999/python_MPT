#!/usr/bin/python
import urllib2
import sys
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#           INFORMATION GETHERING UTILITY       #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
try:
    u = raw_input("\n[+]ENTER FULL URL OR WEBSITE [with http://]:")
    u.rstrip()
    header = urllib2.urlopen(u).info()
    print(str(header))
except:
    print"\n\t\t[-]ERROR : PLEASE CHECK INPUT...!!!"

raw_input("[+]PRESS ANY KEY TO EXIT")
