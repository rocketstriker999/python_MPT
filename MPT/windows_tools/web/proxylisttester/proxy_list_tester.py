import sys, httplib
import socket
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#               PROXY LIST TESTER               #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
def testproxy(prox):
	try:
		h2 = httplib.HTTPConnection(prox)
		h2.connect()
		print "[+]Testing:",prox[:-1]
		print "\t[+]WORKING PROXY"
	except(socket.timeout): 
		print "[+]Testing:",prox[:-1]
		print "\t[-]CONNECTION TIMED OUT"	
	except:
		print "[+]Testing:",prox[:-1]
		print "\t[-]BAD PROXY"
pfile='../../../proxy test.txt' 
try:
	lines = open(pfile, "r").readlines()
	print "\n[+]PROXY FOUND IN LIST :",len(lines)
except(IOError): 
 	print "[-]ERROR:FILE NOT FOUND\n" 
for proxy in lines:
	if "\n" in proxy:
		p=proxy.strip("\n")
	testproxy(p)
	
input("\n[+]PRESS ANY KEY TO EXIT")
