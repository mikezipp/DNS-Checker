# DNS-Checker
Check for DNS, Send alert when DNS is unreachable


CRONTAB Configuration as follows:
#Use NANO to edit crontab
env EDITOR=nano crontab -e

#Disable mail notifications
MAILTO=""

#Execute every 1 minute by changing to directory and executing script
*/1 * * * * cd /Users/mzipp/DNS-Checker/ && /usr/bin/python dns-checker-v1


#back up the crontab:
crontab -l > my_cron_backup.txt

#Empty it:
crontab -r

#To restore:
crontab my_cron_backup.txt
crontab -l
