import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['whoamiagent007@gmail.com', 'musleh35-2313@diu.edu.bd']

msg = EmailMessage()
msg['Subject'] = "Checkout Lech Gotti new pic"
msg['From'] = EMAIL_ADDRESS
msg['To'] = ", ".join(contacts)
msg.set_content('Hi, Agent007. Thanks for choosing our website.\nFrom String Team.')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
	<body>
		<h1 style="color: SlateGray">Hi, Agent007</h1>
                <p>Thanks for choosing our website.</p>
                <p>From String Team</p>
	</body>
</html>
""", subtype="html")


# attachment
# files = ['leahGotti.jpg', 'comic.png', 'leahGotti_converted.jpg']

# for file in files:
#     with open(f"./pngs/{file}", "rb") as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name 
#     msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # subject = "Wanna know why I mail you?"
    # body = "You didn't response my phone last time. That why" 
    # msg = f"Subject: {subject}\n\n{body}" 
    # smtp.sendmail(EMAIL_ADDRESS, "whoamiagent007@gmail.com", msg)

    smtp.send_message(msg)
