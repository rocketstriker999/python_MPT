import socket
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#               IP-ADRESS FINDER                #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
u=raw_input("\n[+]PLEASE ENTER TARGER (e.g. www.xyz.com)")
print "\n[+]IP-ADRESS OF GIVEN TARGET IS :",socket.gethostbyname(u)
raw_input("\n[+]PRESS ANY KEY TO EXIT")
