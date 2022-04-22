import smtplib  # these are all built into Python 3.6 and above
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = "srcgithub@gmail.com"
receiver_email = "srcgithub@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.set_content(body)  (notice the built-in method)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")  # adding the "alternative" content of html.

context = ssl.create_default_context()  # this gives us a secure connection to Gmail's server, since we dont have our own server

print("Sending Email")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: # 465 is the port
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success!")