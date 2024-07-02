#!/usr/bin/env python3
# Description: Custom Email; email server: smtp.gmail.com

import sys
import mail_module as mm
import csv
send = ""
key = ""
sub = ""

file = open("test.txt", "r")
file1 = open("file.html", "r")
text = file.read()
html = file1.read()
file.close()
file1.close()

with open("list.csv") as con:
  reader = csv.reader(con)
  next(reader)
  for name, id, email in reader:
    text1 = text.format(name=name, ID=id)
    rec=email
    cust = mm.To_Mail(send, key, rec, sub)
    cust.custom(text1, html)
    att = input("Add files: 1 for yes 0 for no: ")
    att = att.strip()
    if att == '1':
        adding_file = mm.To_Mail.get_attach()
        cust.add_file("Attachments:", adding_file)
        cust.sending()
        cust.quit_server()
    else:
        cust.sending()
        cust.quit_server()
