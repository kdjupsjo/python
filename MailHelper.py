import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def MailInit(MsgBody):
	fromAdr = "excellent.rentz@gmail.com"
	toAdr = "kristoffer.djupsjo@gmail.com"

	mgs = MIMEMultipart()
	mgs['From'] = fromAdr
	mgs['To'] = toAdr
	mgs['Subject'] = "Nya Lägenheter att ta en titt på"
	mgs.attach(MIMEText(MsgBody, 'Plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromAdr, "PASSWORD_GOES_HERE")

	text = mgs.as_string()
	server.sendmail(fromAdr, toAdr, text)
	server.quit()