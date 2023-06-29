import urllib2
import time
import os
import sys
import re
import subprocess
print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#              SQL INJECTION TESTER             #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
fobj = open('log.txt','r')
	


SQLeD = {'MySQL': 'error in your SQL syntax',
         'MySQL_Valid_Argument': 'Supplied argument is not a valid MySQL result resource in',
         'MySQL_fetch':'mysql_fetch_assoc()',
         'MySQL_array': 'mysql_fetch_array()',
         'MySQL_result': 'mysql_free_result()',
         'MySQL_start': 'session_start()',
         'MYSQL': 'getimagesize()',
         'MySQL_call': 'Call to a member function',
         'Oracle1': 'Microsoft OLE DB Provider for Oracle',
         'Mysql_re': 'Warning: require()',
         'MysQl_11': 'array_merge()',
         'MySQLi': 'mysql_query()',
         'Oracle': 'ORA-01756',
         'MiscError': 'SQL Error',
	 'MiscError2': 'mysql_fetch_row',
	 'MiscError3': 'num_rows',
         'JDBC_CFM': 'Error Executing Database Query',
         'JDBC_CFM2': 'SQLServer JDBC Driver',
         'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
         'MSSQL_Uqm': 'Unclosed quotation mark',
         'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
         'Postgrey_error': 'An error occured',
         'SQL_errore' : 'Unknown Column',
         'MS-Access_JETdb': 'Microsoft JET Database'}


for links in fobj:
    u= links.rstrip()
    print"\n\n[+]TRYING :",u
    try:
        
           
    
        p="'"
        host=u+p

        for type,eMSG in SQLeD.items():
            r=urllib2.urlopen(host).read()
            if re.search(eMSG, r):
                print "\n\n\n[+]SQL INJECTION BUG FOUND ERROR TYPE IS:", type,"\n\n"
                #logfile.write("\n"+host)
				
            else:
                pass

    except:
        pass

    
print"\n[+]YOU FOUND YOUR WEBSITE IN SQL INJECTION VULNRABLE???"
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
import os
print os.getcwd()
os.chdir('../../')
print os.getcwd()
raw_input("\n[+]PRESS ANY KEY TO EXIT")
