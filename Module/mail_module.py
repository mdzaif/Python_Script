#!usr/bin/env python3
#Description: Useful methods for mail
#Library requried: tkinter.
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
        while True:
            fs_t = 0.0
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
                if os.path.isfile(files):
                    fs = float(os.stat(files) / (1024 * 1024))
                    fs_t += fs
                    file_l.append(files)
                else:
                    print(f"File not found: {files}, skipping....")

            if file_l:
                if fs_t <= 25.0:
                    return file_l
                else:
                    print("File limit is upto 25.0 MB")
                    print("Re-upload Files...")
                    continue

    def custom(self, tex, html):
        set1 = MIMEText(tex, "plain")
        set2 = MIMEText(html, "html")
        self.m.attach(set1)
        self.m.attach(set2)

    def sending(self):
        try:
            self.server.sendmail(self.m['From'], self.m['To'], self.m.as_string())
        except Exception as e:
            print(f"Faild: {e}")

    def quit_server(self):
        self.server.quit()
        print("Sent")
