# standar imports
import sys
import re
import getopt
import urllib2
import urlparse
import httplib
import copy
import os
import time
import socket
import datetime

import getpass

####################
# Global Variables
debug=False
vernum='1.0.1'
verbose=False
log=False
auth=False

time_responses = []

# This is for identify links in a HTTP answer
#linkregex = re.compile('[^>](?:href=|src=|content=\"http)[\'*|\"*](.*?)[\'|\"]',re.IGNORECASE)
linkregex = re.compile('[^>](?:href\=|src\=|content\=\"http)[\'*|\"*](.*?)[\'|\"].*?>',re.IGNORECASE)
linkredirect = re.compile('(?:open\\(\"|url=|URL=|location=\'|src=\"|href=\")(.*?)[\'|\"]')
linksrobots = re.compile('(?:Allow\:|Disallow\:|sitemap\:).*',re.IGNORECASE)
information_disclosure = re.compile('(?:<address>)(.*)[<]',re.IGNORECASE)


# HTTP Response Codes
# -------------------
error_codes={}
error_codes['0']='USER ABOARTED'
error_codes['1']='SKYPPING URL'
error_codes['-2']='NAME OR SERVICE UNKNOWN'
error_codes['22']='22 UNKNOWN ERROR'
error_codes['104']='104 CONNECTION RESET BY HOST'
error_codes['110']='110 CONNECTION TIMED OUT'
error_codes['111']='111 CONNECTION REFUSED'
error_codes['200']='200 EVERTHING IS OK'
error_codes['300']='300 MULTIPLE CHOICES AVILABLE'
error_codes['301']='301 MOVED PERMENENTLY'
error_codes['302']='MOVED'
error_codes['305']='305 USE PROXY'
error_codes['307']='307 TEMPORARY REDIRECT'
error_codes['400']='400 BAD REQUEST'
error_codes['401']='401 UNAUTHORIZED'
error_codes['403']='403 FORBIDDEN'
error_codes['404']='404 NOT FOUND'
error_codes['405']='405 METHOD NOT ALLOWED'
error_codes['407']='407 PROXY AUTHENTICATION REQUIRED'
error_codes['408']='408 REQUEST TIME OUT'
error_codes['500']='500 INTERNAL SERVER'
error_codes['503']='503 SERVICE NOT AVILABLE'
error_codes['504']='504 GATEWAY TIME OUT'
error_codes['505']='505 HTTP VERSION NOT SUPPORTED'
error_codes['9999']='UNKNOWN RESPONSE '


# End of global variables
###########################


# Print version information and exit
def version():
	"""
	This function prints the version of this program. It doesn't allow any argument.
	"""
	print "+----------------------------------------------------------------------+"

# Print help information and exit:
def usage():
	print"\nPLEASE ENTER A URL OR WEBSITE THAT YOU WANT TO CRAWL"
	print"\nE.g. http://www.xyz.com/index.php"
	print"\nCRAWLER IS BY DEFAULT SET TO CRAWL LINKS AND ELEMENTS AVIALABELE ON WEBPAGE"
	print"\nALL THE DETAILS OF CRAWLER WILL BE SAVED TO LOG FILE IN SAME FOLDER"
	sys.exit(1)

def printout(input_text,output_file):

	"""
	To main functionalities are covered in this function:
	1. Prints a text in the stdout
	2. Write a text in the given file. 

	Not return any value.
	"""

	global debug
	global verbose

	try:
		print input_text  
		if output_file:
			try:
                                output_file.write(input_text+'\n')
			except:
				print '\n[-]ERROR IN FILE SYSTEM' 

        except Exception as inst:
		print '[-]CAN NOT RUN SCRIPT PERFACTLY'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def check_url(url):

	"""
	This function verifies that the given 'url' is well formatted, this means that it has defined a protocol and a domain. 
	The urlparse.urlparse() function is used. 

	The return values can be 'True'/'False'.
	"""

	global debug
	global verbose

	try:
		url_parsed = urlparse.urlparse(url)
		if url_parsed.scheme and url_parsed.netloc:
			return True
		else:
			return False

        except Exception as inst:
		print '\n[-]PLEASE CHECK THE URL '
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def encode_url(url):

	"""
	This function encode the URL according to Percentage or URL encoding.  
	Actually only replaces a 'space' to '%20'.

	Returns an URL.
	"""

	global debug
	global verbose

	url_encoded = ""
	try:	
		url_encoded = url.replace(" ","%20")
		#url_encoded = url_encoded.replace("&amp;","&")
		
		return url_encoded

        except Exception as inst:
		print '\n[-]CANNOT ENCODE THE URL'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def log_line(request, response_code, response_size,log_file):

	"""
	This function generates an output line of a given HTTP request in CLF (Common Log Format)

	Not return any value.
	"""

	global debug
	global verbose

	try:
		try:
			if response_size == -1:
				content_size = '-'
			else:
				content_size = str(response_size)
			local_hostname = socket.gethostname()
			local_user = os.getenv('USER')
			timestamp = time.strftime('%e/%b/%Y:%X %z').strip()
			method = request.get_method()
			protocol = 'HTTP/1.1'	# This is the version of the protocol that urllib2 uses
			user_agent = request.get_header('User-agent')
			url = request.get_full_url()
			
			# COMMON LOG FORMAT
			log_file.write(local_hostname+' '+'-'+' '+local_user+' '+'['+timestamp+']'+' '+'"'+method+' '+url+' '+protocol+'"'+' '+str(response_code)+' '+content_size+' "-" "'+user_agent+'"\n')

			# URLSNARF FORMAT
			#log_file.write(local_hostname+' '+'- - '+'['+timestamp+']'+' '+'"'+method+' '+url+' '+protocol+'"'+' - - "-" "'+user_agent+'"\n')
		except:
			print 'Not logging the following request: {0}'.format(request.get_full_url())

	except Exception as inst:
		print '\n[-]LOOKS LIKE THERE ARE SOME PROBLEM WITH LOG FILE'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y

def get_url(url, host, username, password, download_files_flag):

	"""
	This function does a HTTP request of the given URL using the urllib2 python library. 

	Returns two values: [request,response]
	"""

	global debug
	global verbose
	global auth

	#Vector to save time responses of each request. For now it is a global variable.
	global time_responses


	starttime=0
	endtime=0
	handler=""

	try:
		try:
			starttime= time.time()

			url = encode_url(url)
			if debug:
				print '\n[+]ENCODED URL: '+url
			request = urllib2.Request(url)
			request.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5; Windows NT 5.0)')
			
			if auth:
				password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
				password_manager.add_password(None, host, username, password)

				handler = urllib2.HTTPBasicAuthHandler(password_manager)

			if not download_files_flag:
				#First we do a head request to see the type of url we are going to crawl
				request.get_method = lambda : 'HEAD'

				if handler:
					opener_web = urllib2.build_opener(handler)
				else: 
					opener_web = urllib2.build_opener()

				response = opener_web.open(request)

				# If it is a file, we don get the content
				if 'text/html' not in response.headers.typeheader:
					opener_web.close()
					
					endtime= time.time()
					time_responses.append(endtime-starttime)

					return [request,response]
			
			request.get_method = lambda : 'GET'
			if handler:
				opener_web = urllib2.build_opener(handler)
			else: 
				opener_web = urllib2.build_opener()

			response = opener_web.open(request)

			opener_web.close()

			endtime= time.time()
			time_responses.append(endtime-starttime)

			return [request,response]


                except urllib2.HTTPError,error_code:
			return [request,error_code.getcode()]
		except urllib2.URLError,error_code:
			error = error_code.args[0]
			return [request,error[0]]
		except socket.error,error_code:
			error = error_code.args[0]
			try:
				error = error[0]
			except:
				pass
			return [request,error]
			
	except KeyboardInterrupt:
		try:
			print '\n[-]PRESS ANY TO EXIT' 
			raw_input()
			return ["",1]
		except KeyboardInterrupt:
			return ["",0]
        except Exception as inst:
		print '\n[-]CAN NOT RUN SCRIPT PERFACTLY'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1	

def get_links(link_host, link_path, content):

	"""
	This function uses a regular expresion to find links in a HTML source page. 
	The regular expresion used is defined in the 'linkregex' variable.

	Returns a vector of extracted links
	"""

	global debug
	global verbose
	global linkregex

	try:
		# We obtain the links in the given response
		links = linkregex.findall(content)

		# We analyze each link 
		for link in links:
			try:
				link_clean = link.strip(' ')
			except:
				print '\n[-]UNKNOWN ERROR'
			parsed_link = urlparse.urlparse(link_clean)
			if not parsed_link.scheme and not parsed_link.netloc:
				if link_clean.startswith('/'):
					if link_host.endswith('/'):
						links[links.index(link)] = link_host.rstrip('/')+link_clean
					else:
						links[links.index(link)] = link_host+link_clean
				elif link_clean.startswith('./'):
						links[links.index(link)] = link_host+link_clean
				else:
					links[links.index(link)] = link_path+link_clean
			else:
				links[links.index(link)] = link_clean

		for link in links:
			links[links.index(link)] = link.split('#')[0]

		return links

        except Exception as inst:
		print '\n[-]CAN NOT RUN THE SCRIPT PROPERLY'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def crawl(url,usuario,password,output_filename,crawl_limit=0,log=False,log_filename='none',crawl_depth=0):
	
	"""
	Crawl a given url using a breadth first exploration. 

	The function returns the following values: [links_crawled, urls_not_crawled, links_to_files]
	"""

	global debug
	global verbose
	global error_codes
	
	# Vector that stores the remaining URLs to crawl
	urls_to_crawl = []
	urls_not_crawled = []
	links_crawled = []
	links_extracted = []
	files=[]
	crawl_limit_flag=False

	urls_to_crawl.append(url)

	if (crawl_limit>0):
		crawl_limit_flag=True
	if crawl_depth > 0:
		crawl_depth = crawl_depth + 3
	try:
		printout(''+url,output_filename)
		
		if output_filename:
			printout('',output_filename)
		if log:
			printout(''+log_filename.name,output_filename)

		printout('',output_filename)
		
		

		while urls_to_crawl:
			if crawl_limit_flag:
				if (len(links_crawled) >= crawl_limit):
					break
			try:
				# We extract the next url to crawl
				url = urls_to_crawl[0]
				urls_to_crawl.remove(url)

				# Here we limit the crawl depth
				if crawl_depth > 0:
					if url.endswith('/'):
						if url.rpartition('/')[0].count('/') >= crawl_depth:
							continue
					elif url.count('/') >= crawl_depth:
							continue

				# We add the url to the links crawled
				links_crawled.append(url)

				# We print the URL that is being crawled
				printout(''+str(url),output_filename)

				# We extract the host of the crawled URL	
				parsed_url = urlparse.urlparse(url)
				host = parsed_url.scheme + '://' + parsed_url.netloc

				if parsed_url.path.endswith('/'):
					link_path = host + parsed_url.path
				else:
					link_path = host + parsed_url.path.rpartition('/')[0] + '/'

				# We obtain the response of the URL
				[request,response] = get_url(url,host,usuario, password,False)

				# If there is a response
				if response:
					#If the server didn't return an HTTP Error
					if not isinstance(response, int):
						content = response.read()

						if log:
							log_line(request,response.getcode(),len(content),log_filename)

						# We print the file type of the crawled page
						if response.headers.typeheader:
							# If it isn't an HTML file
							if 'text/html' not in response.headers.typeheader:
								if url not in files:
									files.append([url,str(response.headers.typeheader.split('/')[1].split(';')[0])])
								if verbose:
									printout('\t[-] ('+str(response.getcode())+') '+str(response.headers.typeheader),output_filename)
							else:
								#if verbose:
								#	printout('\t[-] ('+str(response.getcode())+') '+str(response.headers.typeheader),output_filename)

								links_extracted = get_links(host, link_path, content)
								links_extracted.sort()

								# We add new links to the list of urls to crawl
								for link in links_extracted:
									if debug:
										print '\n[+] {0}'.format(link)
									parsed_link= urlparse.urlparse(link)
									link_host = parsed_link.scheme + '://' + parsed_link.netloc

									# We just crawl URLs of the same host
									if link_host == host:
										if link not in links_crawled and link not in urls_to_crawl:
											urls_to_crawl.append(link)
									elif link not in urls_not_crawled:
										urls_not_crawled.append(link)
					else:
						# We print the error code if neccesary
						if log:
							log_line(request,response,-1,log_filename)
				else:
					if response==1:
						continue
					if response==0:
						print '\n[-]Skypping THE REST OF URL'
						break

			except KeyboardInterrupt:
				try:
					print '[-]PRESS ANY KEY TO SKIP' 
					raw_input()
					continue
				except KeyboardInterrupt:
					print '[-]EXITING'
					break	

			except Exception as inst:
				print '\n[-]CAN NOT RUN SCRIPT PERFACTLY'
				print type(inst)     # the exception instance
				print inst.args      # arguments stored in .args
				print inst           # __str__ allows args to printed directly
				x, y = inst          # __getitem__ allows args to be unpacked directly
				print 'x =', x
				print 'y =', y
				break
		
		
		printout('',output_filename)

		return [links_crawled,urls_not_crawled,files]

	except KeyboardInterrupt:
		try:
			print '\n[-]PRESS ANY KEY TO SKIP' 
			raw_input()
			return 1
		except KeyboardInterrupt:
			print '[-]SKIPPING'
			return 1
       
	except Exception as inst:
		print '\n[-]CAN NOT RUN SCRIPT PERFACTLY'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		return -1

def external_links():
        print ''
        
	
	


def indexing_search(usuario, password,links_vector,output_filename):

	print''

def report_files(export_file_list,files_vector,output_filename):
	
	print''
def download_files(extensions_to_download,files_vector,usuario,password,interactive_flag,output_filename):
        print''
def statistics(global_time, directories, indexing, links_crawled, files, extensions_found, output_filename):
	print''

##########
# MAIN
##########
def main():

	global debug
	global verbose
	global log
	global auth
	global output
	global output_name

	url_to_crawl = ""
	usuario = "crawler123"
	password = "crawler123"
	crawl_limit = 0
	extensions_to_download = "" 
	download_files_flag=False
	export_file_list = False
	interactive_flag=False

	starttime=0
	endtime=0

	#Data lists
	directories = []
	indexing = []
	links_crawled = []
	externals_url_vector = []
	files_vector = []
	extensions_found = []
	crawl_depth = 0
	save_output=False
	output_name = ""
	output_file = ""
	log_name = ""
	log_file = ""

	try:

		# By default we crawl a max of 5000 distinct URLs
		opts, args = getopt.getopt(sys.argv[1:], "hVDwu:vLU:Pl:[d:]eiC:", ["help","version","debug","write","url=","verbose","common-log-format","usuario=","password","crawl-limit=","[download-file=]","export-file-list","interactive-download","crawl-depth="])


	except getopt.GetoptError: usage()	

	for opt, arg in opts:
		if opt in ("-h", "--help"): usage()
		if opt in ("-V", "--version"): version();exit(1)
		if opt in ("-D", "--debug"): debug=True
		if opt in ("-w", "--write"): save_output=True
		if opt in ("-u", "--url"): url_to_crawl = arg
		if opt in ("-v", "--verbose"): verbose = True
		if opt in ("-L", "--common-log-format"): log = True
		if opt in ("-U", "--usuario"): usuario = arg
		if opt in ("-P", "--password"): password = getpass.getpass() ; auth = True
		if opt in ("-l", "--crawl-limit"): crawl_limit = int(arg) 
		if opt in ("-d", "--download-file"): extensions_to_download = arg ; download_files_flag=True
		if opt in ("-i", "--interactive-download"): interactive_flag=True
		if opt in ("-e", "--export-file-list"): export_file_list = True
		if opt in ("-C", "--crawl-depth"): crawl_depth = arg
	try:

		if debug:
			print '[+] Debugging mode enabled'

		if check_url(url_to_crawl):

			date = str(datetime.datetime.today()).rpartition('.')[0].replace('-','').replace(' ','_').replace(':','')
			if save_output:
				output_name = 'log.txt'
				try:
					output_file = open(output_name,'w')
				except OSError, error:
					if 'File exists' in error:
						pass
					else:
						output_name = ""
			else:
				output_name = ""
			
			if log:
				log_name = date +'_'+ urlparse.urlparse(url_to_crawl).netloc + '.log'
				try:
					log_file = open(log_name,'w')
				except OSError, error:
					if 'File exists' in error:
						pass
					else:
						log=False

			starttime=time.time()

			# Crawl function
			[links_crawled,externals_url_vector, files_vector] = crawl(url_to_crawl, usuario, password, output_file, crawl_limit, log,log_file,int(crawl_depth))
			
			# Indexing search
			[directories, indexing] = indexing_search(usuario, password,links_crawled,output_file)
			
			# Printing found files and exporting files to an output file
			report_files(export_file_list,files_vector,output_file)

			# Searching for external links
			external_links(url_to_crawl,externals_url_vector,output_file)
			
			# Download files
			if download_files_flag or interactive_flag:
				extensions_found = download_files(extensions_to_download,files_vector,usuario,password,interactive_flag,output_file)
			
			printout('',output_file)
			printout('[+]END TIME: '+str(datetime.datetime.today()),output_file)

			endtime=time.time()
			# Printing statistics
			statistics(endtime-starttime,directories,indexing,links_crawled,files_vector,extensions_found,output_name)

			try:
				output_file.close()
			except:
				pass
			try:
				log_file.close()
			except:
				pass

		else:
			print
			print '\n[-]PLEASE CHECK THE URL AGAIN'
			print
			usage()

	except KeyboardInterrupt:
		# CTRL-C pretty handling
		print '\n[-]USER AVOARTED'
		sys.exit(1)
	except Exception as inst:
		print '[-]CAN NOT RUN SCRIPT PROPERLY'
		print type(inst)     # the exception instance
		print inst.args      # arguments stored in .args
		print inst           # __str__ allows args to printed directly
		x, y = inst          # __getitem__ allows args to be unpacked directly
		print 'x =', x
		print 'y =', y
		sys.exit(1)


if __name__ == '__main__':
	main()


raw_input("\n[+]PRESS ANY KEY TO EXIT")
