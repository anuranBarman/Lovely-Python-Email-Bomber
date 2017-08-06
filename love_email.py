# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:02:46 2017

@author: Anuran Barman

DISCLAIMER: The contents here are property of the  website(www.lovelysms.com) scrapped with the script.
The script simply uses the content for demonstration purposes only, not for any kind
of commercial usage.
"""

from bs4 import BeautifulSoup
import urllib3
import smtplib  
import mimetypes 
import sys 
import time 
from email.mime.text import MIMEText

http=urllib3.PoolManager()

url="http://www.lovelysms.com/cute-love-sms-messages.htm"

response = http.request('GET', url)
soup = BeautifulSoup(response.data,"lxml")

posts=soup.find_all('p')

messages=[]

for post in posts:
    messages.append(post.text)
#for msg in messages:
#    print(msg+"\n"+'*'*50)
class SMTP(object):
      def title(self):
            print("PYTHON MAIL BOMBER IS WORKING")
 
      def SMTPconnect(self):
            print ("We are in the SMTPconnect") 
            self.smtpserver="smtp.gmail.com"
            self.smtpport=587
            try:
                  self.mailServer = smtplib.SMTP(self.smtpserver,self.smtpport)
            except IOError as e:
                  print(e)
                  time.sleep(5)
                  sys.exit(1)
            self.mailServer.starttls()
            self.username="your username" #Username
            self.password="your password" #password
            try:
                  self.mailServer.login(self.username,self.password)
            except BaseException as e:
                  print(e) 
                  time.sleep(3)
                  sys.exit(1)
      def buildemail(self):
            x = 1
            while x < len(messages)-1:
                  print( " We are inside Buildemail ")
                  print ("Building message part")
                  self.From = self.username # From
                  self.To = "Your Girlfriend's Email ID" # TO
                  self.Subject = "I Love You" #Subject
                  self.Message = messages[x] #message
                  mail = MIMEText(self.Message)
                  mail['From']=self.From
                  mail['To']=self.To
                  mail['Subject']=self.Subject
                  self.mailServer.sendmail(self.From, self.To, mail.as_string())
                  x+=1
            print( "sending successful")
            time.sleep(7)
            sys.exit()

s = SMTP()
s.title()
s.SMTPconnect()
s.buildemail()