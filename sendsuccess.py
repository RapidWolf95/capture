#!/usr/bin/env python
# modified from http://elinux.org/RPi_Email_IP_On_Boot_Debian
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import urllib2
import os
#CHANGE THESE VARIABLES#
to = 'YOURSENDTOEMAIL@WHEREVER.COM'
gmail_user = 'YOUREMAIL@gmail.com'
gmail_password = 'YOURPASSWORD'
########################
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
hostname = (socket.gethostname())
ethip = os.popen('ifconfig eth0 | grep \' inet \' | cut -d \' \' -f10').read().strip()
wlanip = os.popen('ifconfig wlan0 | grep \' inet \' | cut -d \' \' -f10').read().strip()
extip = os.popen('curl -s icanhazip.com').read().strip()
with open('caplog.txt', 'r') as myfile:
    logs=myfile.read()
message = "I HAVE A CONNECTION.\n\n-------------\nEXT IP: %s\nETH IP: %s\nWLAN0 IP: %s\n-------------\n\n\n-PI (3.1415) \n\n\n\n\n\nMY LOGS:\n\n%s" %(extip,ethip,wlanip,logs)
my_message = message
msg = MIMEText(my_message)
msg['Subject'] = '--PI CONNECTED-- %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
