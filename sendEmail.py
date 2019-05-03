import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime
import time
from time import gmtime, strftime

#currTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
currTime = time.ctime()

file = open("pass.txt", "r") 
data = file.readlines()
passw = data[0]
fromemail = data[1]
toemail = data[2]

msg = MIMEMultipart()
msg['From'] = fromemail
msg['To'] = toemail
msg['Subject'] = "ALERT! Tyler is in the hospital"
 
body = "Tyler has entered the hospital at " + currTime + " and has not silenced his alert notification."
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromemail, passw)
text = msg.as_string()
server.sendmail(fromemail, toemail, text)
server.quit()
