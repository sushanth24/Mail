import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Sushanth raj"
receiver = input("Enter the receiver email id: ")
email["to"] = receiver
subject = input("Enter the subject you want to send: ")
email["subject"] = subject
content = input("Enter the content you want to send: ")
email.set_content(content)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("rachakatlasushanthraj481@gmail.com", "Sushi_7271056666")
    smtp.send_message(email)
    print("All goodd!!")
