#!/usr/bin/env python3

from mail_module import *

#send = input("From: ")
#key = input("App passwords: ")
#rec = input("To: ")
#sub = input("Subject: ")
send="mimolist20@gmail.com"
key="zkgn asgb zoij lgqo"
rec="mdizaif@gmail.com"
sub="test"
tex = "Attachments: "
files = To_Mail.get_attach()

if files:
    take = To_Mail(send, key, rec, sub)
    take.add_file(tex, files)
    take.quit_server()
else:
    print("Operation Failed!")