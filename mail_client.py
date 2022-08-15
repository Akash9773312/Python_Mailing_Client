import smtplib 
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('Your email', password)

msg = MIMEMultipart
msg['From'] = 'Your Name'
msg['To'] = 'target email'
msg['Subject'] = 'TEST'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'code.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('Your email', 'target email', text)




