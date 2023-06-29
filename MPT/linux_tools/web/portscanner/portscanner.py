import socket, sys
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#              PORT SCANNER UTILITY             #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
def scan(u,startport):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(4)
		s.connect((socket.gethostbyname(u), int(startport)))
		print "\n[+]OPEN PORT:", startport
		s.close()
	except:
		print "\n[-]CLOSE PORT:", startport
try:
        u = raw_input("\n[+]ENTER TARGET IP ADDRESS: ")
        ip = socket.gethostbyname(u)
        print "-" * 60
        print "\n\t[+]IP ADRESS OF TARGET", ip
        print "-" * 60
        startport = input("\n[+]START PORT : ")
        endport=input("\n[+]END PORT : ")
        while startport <= endport:
                scan(u,startport)
                startport=startport+1
except:
        print"\n\t\tERROR:PLEASE CHECK YOUR INPUT"

print"\n\n\n"

file = open('wellknownports.txt', 'r')

print file.read()
raw_input("[+]PRESS ANY KEY TO EXIT")
