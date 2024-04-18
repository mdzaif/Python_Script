#!/usr/bin/env python3
#Description: Custom Email; email server: smtp.gmail.com

from mail_module import *
import csv
#send = input("From: ")
#key = input("App password: ")
#rec = input("To: ")
#sub = input("Subject: ")
send ="mdzaifimammahi@gmail.com"
key = "boey ctnz uiup iakx"
#rec = "mdizaif@gmail.com"
sub = "test"
#Edit the text file
file = open("test.txt", "r")
#Edit the html file
file1 = open("file.html", "r")
text = file.read()
html = file1.read()
adding_file = To_Mail.get_attach()

#read file:
with open("list.csv") as con:
  reader = csv.reader(con)
  next(reader)
  for name, id, email in reader:
    text1 = text.format(name=name, ID=id)
    rec=email
    cust = To_Mail(send, key, rec, sub)
    cust.custom(text1, html)
    cust.add_file("Attachments:", adding_file)
    cust.sending()
    cust.quit_server()