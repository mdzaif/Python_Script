import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = input("From: ")
password_key = input("App password: ")
receiver_email = input("To: ")


subject = input("Subject: ")

# SMTP Server and port no for GMAIL.com
gmail_server = "smtp.gmail.com"
gmail_port = 465

# Starting connection
my_server = smtplib.SMTP_SSL(gmail_server, gmail_port)

# Login with your email and password
my_server.login(my_email, password_key)

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = my_email
message["To"] = receiver_email

#Gmail_User = "Md. Zaif"
text ="""\
Hi,
See your Details:
Name:
Your Id:"""
html_content = """
<html>
  <body>
    <p>You can find me at:</p>
    <p align="left">
      <a href="mailto:mdizaif@gmail.com" target="_blank"><img align="center" src="https://raw.githubusercontent.com/mdzaif/mdzaif/main/images/gmail_1.jpg" alt="mdzaifimammahi" height="30" width="40" /></a>
      <a href="https://www.linkedin.com/in/md-zaif-imam-mahi-70aa84241/" target="_blank"><img align="center" src="https://raw.githubusercontent.com/mdzaif/mdzaif/main/images/LinkedIn_1.jpg" alt="mdzaifimammahi" height="30" width="40" /></a>
      <a href="https://twitter.com/mdzaifimamamahi" target="_blank"><img align="center" src="https://raw.githubusercontent.com/mdzaif/mdzaif/main/images/twitter_1.jpg" height="30" width="40" /></a>
      <a href="https://fb.com/mdzaifimammahi" target="_blank"><img align="center" src="https://raw.githubusercontent.com/mdzaif/mdzaif/main/images/facebook_1.jpg" alt="mdzaifimammahi" height="30" width="40" /></a>
      <a href="https://gitlab.com/mdzaif" target="_blank"><img align="center" src="https://raw.githubusercontent.com/mdzaif/mdzaif/main/images/gitlab_1.jpg" alt="mdzaifimammahi" height="30" width="40" /></a>
    </p>
    <br>
    <br>
  </body>
</html>
"""

message.attach(MIMEText(html_content, "html"))

# Convert message to string
message_str = message.as_string()

my_server.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=message_str)
my_server.quit()

