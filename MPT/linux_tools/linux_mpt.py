import sys
import time
import os







while True:
    import os
    
    
    
    print'\n\t\t\t#########################'
    print'\t\t\t#                       #'
    print'\t\t\t# WELCOME TO MAIN MENU  #'
    print'\t\t\t#                       #'
    print'\t\t\t#########################'    

    print"\n[+]PRESS 1 FOR WEB PENTESTING.."
    print"\n[+]PRESS 2 FOR NETWORK PENTESTING..."
    print"\n[+]PRESS 3 FOR COMPUTER PENTESTING..."
    print"\n[+]PRESS 4 FOR INFORMATION..."

    c=raw_input("\n\n\n[+]PLEASE ENTER YOUR CHOICE :")

    if c=='1':
        print'\n\n\n\t\t\t###########################'
        print'\t\t\t#                         #'
        print'\t\t\t# WELCOME TO WEB SECTION  #'
        print'\t\t\t#                         #'
        print'\t\t\t###########################\n\n'
        print"\n[+]PRESS 1 FOR HEADER GETTER UTILITY..."
        print"\n[+]PRESS 2 FOR IP FETCHER UTILITY..."
        print"\n[+]PRESS 3 FOR LIST FOR ADVANCE SEARCH QUERY DORKS"
        print"\n[+]PRESS 4 FOR DICTONARY MAKER FOR DICTONARY ATTACKS..."
        print"\n[+]PRESS 5 FOR PORT SCANNER..."
        print"\n[+]PRESS 6 FOR E-MAIL BOMB..."
        print"\n[+]PRESS 7 FOR DDOS ATTACK..."
        print"\n[+]PRESS 8 PROXY LIST TESTING..."
        print"\n[+]PRESS 9 FOR CRAWLER..."
        print"\n[+]PRESS 10 FOR HASH MAKER..."
        print"\n[+]PRESS 11 FOR HASH CRACKER..."
        print"\n[+]PRESS 12 FOR FTP SERVER CRACKER..."
        print"\n[+]PRESS 13 FOR SMTP SERVER CRACKER..."
        print"\n[+]PRESS 14 FOR SSH SERVER CRACKER..."
        print"\n[+]PRESS 15 FOR ADMIN PANEL FINDER...."
        print"\n[+]PRESS 16 FOR FILE INCLUSION TESTS..."
        print"\n[+]PRESS 17 FOR CGI SCANNER..."
        print"\n[+]PRESS 18 FOR SIMPLE SQL INJECTION TESTER..."
        print"\n[+]PRESS 19 FOR RANDOM SQL INJECTION AND LFI LINKS..."
        print"\n[+]PRESS 20 FOR SERVER SCANNING FOR SQL INJECTION..."
        print"\n[+]PRESS 21 FOR TIME BASE SQL INJECTION TESTING..."
        print"\n[+]PRESS 22 FOR ADVANCE SQL INJECTION TESTS..."
        print"\n[+]PRESS 23 FOR XSS TESTER..."
        print"\n[+]PRESS 24 FOR EASY FACEBOOK PHISHING"
        print'\n[+]PRESS 25 FOR AUTO SQL INJECTION BUG FINDER'
        print'\n[+]PRESS 26 FOR DEEP AUTO TIMEBASE SQL INJECTION TESTER'
        print'\n[+]PRESS 27 FOR WEBSITE DATABASE FINDER'
        choice=raw_input("\n\n[+]PLEASE ENTER YOUR CHOICE :")
        if choice=='1' :
            os.chdir('web/header/')
            os.system('python header_getter.py')
        
        elif choice=='2' :
            os.chdir('web/ipfetcher/')
            os.system('python ipadress.py')
        
        elif choice=='3' :
            os.chdir('web/dorklist')
            os.system('python starter.py')
        
        elif choice=='4':
            os.chdir('web/dictonarymaker')
            os.system('python dictonarymaker.py')
        
        elif choice=='5':
            os.chdir('web/portscanner')
            os.system('python portscanner.py')
        
        elif choice=='6':
            os.chdir('web/emaibomb')
            os.system('python email_bomb.pyc')
        
        elif choice=='7':
            os.chdir('web/ddos/')
            os.system('python request_flooder.py')
        
        elif choice=='8':
            os.chdir('web/proxylisttester/')
            os.system('python proxy_list_tester.py')
        
        elif choice=='9':
            os.chdir('web/crawler')
            os.system('python input_taker.py')
        
        elif choice=='10':
            os.chdir('web/hashmaker')
            os.system('python hashgen.py')
        
        elif choice=='11':
            os.chdir('web/hashcracker')
            os.system('python hcrack.py')
            
        elif choice=='12':
            os.chdir('web/ftpcracker/')
            os.system('python ftpcracker.py')
        
        elif choice=='13':
            os.chdir('web/smtpcracker/')
            os.system('python smtpcracker.py')
        
        elif choice=='14':
            os.chdir('web/sshcracker')
            os.system('python input_taker.py')
        
        elif choice=='15':
            os.chdir('web/adminpanelfinder/')
            os.system('python adminpanel_finder.py')
        
        elif choice=='16':
            os.chdir('web/fiscanner/')
            os.system('perl lfi_scanner.pl')
        
        elif choice=='17':
            os.chdir('web/cgiscanner/')
            os.system('python input_taker.py')
        
        elif choice=='18':
            os.chdir('web/linksqli')
            os.system('python link_sqli_tester.py')
        
        elif choice=='19':
            os.chdir('web/randomsqlifinder/')
            os.system('python starter.py')
        
        elif choice=='20':
            os.chdir('web/serversqlitest/')
            os.system('python whole_server_sqli.py')
        
        elif choice=='21':
            os.chdir('web/timebasesqli/')
            os.system('python time.py')
        
        elif choice=='22':
            os.chdir('web/sqlmap/')
            os.system('python input_taker.py')
        
        elif choice=='23':
            os.chdir('web/xss/')
            os.system('python xss.py')

        elif choice=='24':
              os.chdir('web/easyfbphisher')
              os.system('easyfbphisher.pyc')

        elif choice=='25':
              os.chdir('web/auto_sqlinjection_finder')
              os.system('python input_taker.py')

        elif choice=='26':
              os.chdir('web/auto_timebase_blind')
              os.system('python input_taker.py')

        elif choice=='27':
              os.chdir('web/database_finder')
              os.system('python database_finder.py')
        
        else:
            print"\n[-]WRONG CHOICE...PLEASE ENTER CORRECT CHOICE"
            
        
    elif c=='2':
        print"\n\n\n\t\t\t###############################"
        print"\t\t\t#                             #"
        print"\t\t\t# WELCOME TO NETWORK SECTION  #"
        print"\t\t\t#                             #"
        print"\t\t\t###############################\n\n"
        print"\n[+]PRESS 1 FOR LAN HOST CHECKER..."
        print"\n[+]PRESS 2 FOR ROUTER PASSWORD CRACKING..."
        print"\n[+]PRESS 3 FOR PACKER SNIFFER..."
        print"\n[+]PRESS 4 FOR JAMMING ALL WIFI AROUND YOU..."
        cn=raw_input("\n\n[+]PLEASE ENTER YOUR CHOICE :")

        if cn=='1':
            os.chdir('network/lanhostscanner/')
            os.system('python lanscanner.py')

        elif cn=='2':
            os.chdir('network/routercracker/')
            os.system('python routercracker.py')

        elif cn=='3':
            os.chdir('network/packet/')
            os.system('python packet.py')

        elif cn=='4':
            os.system('python network/wifijammer/wifijammer.py')

        else:
            print"\n[-]WRONG CHOICE...PLEASE ENTER CORRECT CHOICE"
            
        
    elif c=='3':
        print"\n\n\n\t\t\t################################"
        print"\t\t\t#                              #"
        print"\t\t\t# WELCOME TO COMPUTER SECTION  #"
        print"\t\t\t#                              #"
        print"\t\t\t################################"
        print"\n[+]PRESS 1 FOR RAR OR ZIP PASSWORD CRACKER..."
        cc=raw_input("\n\n[+]PLEASE ENTER YOUR CHOICE :")

      

        if cc=='1':
            os.chdir("computer/rarcracker/")
            os.system('python rarp.py')
            
        else:
            print'\n[-]WRONG CHOICE...PLEASE ENTER CORRECT CHOICE'
            


    elif c=='4':
        print'\n\n\n\t\t\t###################################'
        print'\t\t\t#                              	  #'
        print'\t\t\t# WELCOME TO INFORMATION SECTION  #'
        print'\t\t\t#                                 #'
        print'\t\t\t###################################'
        print"\n[+]PRESS 1 FOR CREDIT..."
        print"\n[+]PRESS 2 FOR ABOUT..."
        print"\n[+]PRESS 3 FOR HOW TO USE..."
        co=raw_input("\n\n[+]PLEASE ENTER YOUR CHOICE :")

        if co=='1':
            os.chdir("otherinformations")
            os.system('python credits.py')

        elif co=='2':
            os.chdir("otherinformations")
            os.system('python about.py')

        elif co=='3':
            os.chdir("otherinformations")
            os.system('python use.py')

        
        else:
            print"\n[-]WRONG CHOICE...PLEASE ENTER CORRECT CHOICE"
              

    
    else:
        print"\n[-]WRONG CHOICE...PLEASE ENTER CORRECT CHOICE"
        

    os.chdir('../../')


