import smtplib  # these are all built into Python 3.6 and above
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = "srcgithub@gmail.com"
receiver_email = "srcgithub@gmail.com"
password = input("Enter a password: ")
