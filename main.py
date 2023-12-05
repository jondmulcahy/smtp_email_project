import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Test Account'
email['to'] = '**********@outlook.com'
email['subject'] = 'Test Email for Python Project'

email.set_content('Generic text for testing purposes.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('t3stpy.acc0unt@gmail.com', '**** **** **** ****')
    smtp.send_message(email)
    print('Message sent successfully.')