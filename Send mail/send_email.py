# import smtplib

# EMAIL_ADDRESS = "shourovcse17@gmail.com"
# PASSWORD = "1112704646"
# send_to = "snydercut.c40@gmail.com"

# subject = "Test subject"
# msg = "Hello there, \nhow are you today?"""

# try:
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login(EMAIL_ADDRESS, PASSWORD)
#     message = 'Subject: {}\n\n{}'.format(subject, msg)
#     server.sendmail(EMAIL_ADDRESS,send_to, message)
#     server.quit()
#     print("Success: Email sent!")
# except:
#     print("Email failed to send.")

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
me =  "shourovcse17@gmail.com"
send_to_mail = "snydercut.c40@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = send_to_mail
Dh = "3GJ6LK2"
html = f"""\
<html>
<head></head>
<body>
    <p>Hi!<br>
        How are you?<br>
        Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
    Code:
    <h2>{Dh}</h2>
</body>
</html>
"""
text_body = MIMEText(html, 'html')
try:
    msg.attach(text_body)
    mail = SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login( "shourovcse17@gmail.com", '1112704646')
    mail.sendmail(me, send_to_mail, msg.as_string())
    mail.quit()
    print("Success: Email sent!")
except:
    print("Email failed to send.")