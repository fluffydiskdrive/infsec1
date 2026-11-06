import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "redacted_sender_email" 
sender_password = "redacted"    
receiver_email = "receiver_email"

subject = "Daily Status Report"
body = """
Good Morning, Sir,\n\n

This is an automated message to report your made-up server functionality.\n 
Everything seems in order.\n\n

Pardon the sketchiest email address ever created by man. Not spam.\n\n

Best regards,\n
Rob Johnson Jr.\n\n

Made Up Company
"""

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


# Attach the body with the HTML content
message.attach(MIMEText(body, "html"))


# Send the email
try:
   # Establish a secure session with the server
   server = smtplib.SMTP(smtp_server, smtp_port)
   server.starttls()  # Secure the connection
   server.login(sender_email, sender_password)  # Log into the email server
   text = message.as_string()
   server.sendmail(sender_email, receiver_email, text)  # Send the email
except Exception as e:
   print(f"Error sending email: {e}")
finally:
   server.quit()

