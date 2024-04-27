#!/usr/bin/env python3
# Description: Send files with email without login; mail_server : smtp.gmail.com.
import sys
import mail_module as mm

send = ""
key = ""
rec = ""
sub = ""
tex = "Attachments: "
files = mm.To_Mail.get_attach()

if files:
    take = mm.To_Mail(send, key, rec, sub)
    take.add_file(tex, files)
    take.sending()
    take.quit_server()
else:
    print("Operation Failed!")
