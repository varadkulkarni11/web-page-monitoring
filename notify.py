import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import datetime
import time

def read_file(fileName):
	li = []
	with open(fileName) as f:
		li = [line.rstrip() for line in f]

	return li

def read_credentials_from_file():
	credentials = read_file('credentials.txt')
	return credentials

def shoot_alert(url):
	
	li = read_file('ids.txt')
	credentials = read_credentials_from_file()
	EMAIL_USER = credentials[0]
	EMAIL_PWD = credentials[1]
	for dest in li: 
		ts = time.time()
		TIME_STAMP = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') 
		msg = MIMEMultipart()
		msg['From'] = credentials[0]
		msg['To'] = dest
		msg['Subject'] = 'ALERT!! CHANGE DETECTED '+ str(TIME_STAMP)
		body = '\nA CHANGE WAS DETECTED IN THE FOLLOWING WEBPAGE: '+ str(url)
		msg.attach(MIMEText(body,'plain'))
		text = msg.as_string()
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls() 
		s.login(EMAIL_USER, EMAIL_PWD) 
		print ("Sending email")
		s.sendmail(EMAIL_USER, dest, text) 
		print ("sent")
		s.quit() 


if __name__ == '__main__':
    shoot_alert("TEST_URL")