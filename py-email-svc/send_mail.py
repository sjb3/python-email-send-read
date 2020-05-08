import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'sjb3uw@gmail.com'
password = 'Just/123'


def send_mail(text='Email body', subject='Hello World', from_email='Hungry H <sjb3uw@gmail.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list)
  # Login to SMTP server
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ','.join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()
