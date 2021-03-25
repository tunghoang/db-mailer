import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header
port = 587
sender_email = 'cntt.uet@gmail.com'
sender_name = 'Văn Phòng Khoa CNTT - ĐHCN - ĐHQGHN'
password = '2020f1t-u37'

def buildEmailMessage(receipient, subject, html, text):
  message = MIMEMultipart('alternative')
  message["Subject"] = subject
  message["From"] = formataddr( (str(Header(sender_name, 'utf-8')), sender_email) )
  message["To"] = receipient
  textPart = MIMEText(text, 'plain', 'utf-8') if text is not None else None
  htmlPart = MIMEText(html, 'html', 'utf-8') if html is not None else None

  if textPart is not None:
    message.attach(textPart)

  if htmlPart is not None:
    message.attach(htmlPart)
  return message

def getserver():
  context = ssl.create_default_context()
  server = smtplib.SMTP('smtp.gmail.com', port)
  server.ehlo()  # Can be omitted
  server.starttls(context=context)
  server.ehlo()  # Can be omitted
  server.login(sender_email, password)
  return server

def sendmail1(server, receiver_email, subject, html, text):
  message = buildEmailMessage(receiver_email, subject, html, text)
  server.sendmail(sender_email, receiver_email, message.as_string());

def quitserver(server):
  server.quit()

def sendmail(receiver_email, subject, html, text):
  context = ssl.create_default_context()
  with smtplib.SMTP('smtp.gmail.com', port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    message = buildEmailMessage(receiver_email, subject, html, text)
    server.sendmail(sender_email, receiver_email, message.as_string());
