#!/usr/bin/env python3
# Description: Send files with email without login; mail_server: smtp.gmail.com.
from mail_module import *

#send = input("From: ")
#key = input("App passwords: ")
#rec = input("To: ")
#sub = input("Subject: ")
send ="mdzaifimammahi@gmail.com"
key = "boey ctnz uiup iakx"
rec = "mdizaif@gamil.com"
sub = "test"
tex = "Attachments: "
files = To_Mail.get_attach()

if files:
    take = To_Mail(send, key, rec, sub)
    take.add_file(tex, files)
    take.sending()
    take.quit_server()
else:
    print("Operation Failed!")