import os
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#                LAN HOST SCANNER               #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
h=raw_input("\n[+]ENTER LAST TWO DIGITS OF IP TO START SCANNING FROM 192.168.")
while True:
    s="192.168."
    t=s+h
    response = os.system("ping " + t)
    a=float(h)
    h=a + 0.1
    h=str(h)
    
#and then check the response...
    if response == 0:
      print "\n\n[+]FOUND ALIVE HOST :",t,"\n\n"
    else:
      print "[-]FOUND DEAD HOST :",t
      
raw_input("[+]PRESS ANY KEY TO EXIT")
