import smtplib

def send_mail():
    from_addr = 'abc@gmail.com'
    to_addr = 'def@gmail.com'

    subject = 'Title'
    body = 'Body'

    message = ('From: %s\nTO: %s\nSubject: %s\n%s' % (from_addr, to_addr, subject, body))
    username = 'abc@gmail.com'
    password = 'abc'

    server = smtplib.SMTP('stmp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, message.encode('euc-kr'))
    server.quit()

def main():
    send_mail()

if __name__ == '__main__':
    main()