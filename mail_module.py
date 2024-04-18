#!usr/bin/env python3

import os
import smtplib as smtp
import tkinter as tk
from tkinter import filedialog
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class To_Mail:
    def __init__(self, send, key, rec, sub):
        # Set the smtp server
        self.server = smtp.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(send, key)
        self.m = MIMEMultipart()
        self.m['From'] = send
        self.m['To'] = rec
        self.m['Subject'] = sub

    def add_file(self, tex, files):

        self.m.attach(MIMEText(tex, 'plain'))
        # File attachment
        for ach in files:
            with open(ach, "rb") as attc:
                obj = MIMEBase('application', 'octet-strem')
                obj.set_payload(attc.read())
            encoders.encode_base64(obj)
            # Retrive the file name
            file_name = os.path.basename(ach)
            obj.add_header(
                "Content-Disposition",
                f"attachment; filename = {file_name}"
            )
            self.m.attach(obj)
            

    def get_attach():
        root = tk.Tk()
        root.geometry("1200x750")
        root.withdraw()
        file_l = filedialog.askopenfilename(
            parent=root,
            title='Choose files',
            multiple=True
        )

        file_list = list(file_l)
        file_l = []
        for files in file_list:

            # files = files.strip()
            if os.path.isfile(files):
                file_l.append(files)
            else:
                print(f"File not found: {files}, skipping....")

        if file_l:
            return file_l

    def send_mail(send, rec):
        try:
            self.server.sendmail(send, rec, self.m.as_string())
        except Exception as e:
            print(f"Faild: {e}")
    
    def quit_server(self):
        self.server.quit()
        print("Sent")