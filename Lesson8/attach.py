import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail():
    from_addr = 'abc@gmail.com'
    to_addr = 'def@gmail.com'

    subject = 'Title'
    body = 'Body'

    username = 'abc@gmail.com'
    password = 'abc'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    msg.attach(MIMEText(body))

    attach = MIMEBase('application', 'octet-stream')
    attach.set_payload(open('minions.jpg', 'rb').read())
    encoders.encode_base64(attach)

    attach.add_header('Content-Disposition', 'attachment; filename="test.jpg"')
    msg.attach(attach)

    server = smtplib.SMTP('stmp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, msg.encode('euc-kr'))
    server.quit()

def main():
    send_mail()

if __name__ == '__main__':
    main()