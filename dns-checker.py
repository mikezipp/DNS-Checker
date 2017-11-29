import socket
import time
import sys
from datetime import datetime
import csv



list_of_hosts = []

#UPDATE LIST FROM TSV FILE
def update_list():
   with open("website-list.tsv", "rU") as csvfile:
      reader = csv.reader(csvfile, dialect='excel-tab')
      for row in reader:
         list_of_hosts.append(row[0])
update_list()



#TRIES TO RESOLVE HOSTNAME AND SENDS DNS ERRORS TO dns-checker-errors.txt
def dnschecker():
   for host in list_of_hosts:
      currenttime = str(datetime.now())
      try:
         print socket.gethostbyname(host)
      except socket.gaierror as e:
         errormessage = "could not resolve DNS for %s at %s " % (host, currenttime)
         print errormessage
         with open("dns-checker-errors.txt", "a") as myfile:
            myfile.write("%s \n" % (errormessage))
dnschecker()



#OPTIONAL CRON CONFIGURATION
#crontab config (osx)
#env EDITOR=nano crontab -e
#MAILTO=""
#1 * * * * cd /Users/$USER/$REPO/ && /usr/bin/python /Users/$USER/$REPO/$PROGRAM-NAME

