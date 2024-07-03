import smtplib

from_email = "spoofed@sender.com"
to_email = "your_email@example.com"
subject = "Subject"
body = "Message Body"
smtp_server = "smtp.your_smtp_server.com"
smtp_port = 587
smtp_user = "smtp_user"
smtp_password = "smtp_password"

message = f"""From: {from_email}
To: {to_email}
Subject: {subject}

{body}
"""

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(from_email, to_email, message)
    print("Email sent!")
