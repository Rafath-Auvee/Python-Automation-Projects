from multiprocessing import context
from urllib import response
import requests as req
from bs4 import BeautifulSoup as bs
import csv
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import password

# collecting current time 
now = datetime.datetime.now()

url = "https://www.baust.edu.bd/category/notice/"

# parsing BAUST notice board 
def parsing_notice_board(url):
  print('Parsing All Notices...')
  doc = ''
  doc +=(f'<b>BAUST Notice Board: {str(now.day)}-{str(now.month)}-{str(now.year)} </b>\n'+'<br>'+'-'*50+'<br><br>' )
  response = req.get(url)
  data = response.content
  result = bs(data, 'html.parser')
  # print(result.prettify())

  all_notices = result.find_all("div", attrs={"class" : "ArchItemDiv"})

  # Notice Titles 
  titles = result.find_all("h2", attrs={"class", "h1MarginTOpRmv"})
  title = [title.string.strip() for title in titles]

  # all notice time date
  dates = result.find_all("span", attrs={"class", "date-day"})
  date = [date.string.strip() for date in dates]

  # all notice time month
  months = result.find_all("span", attrs={"class" : "date-month"})
  month = [month.string.strip() for month in months]

  # all hyper links
  links = result.select("div#text > a")
  link = [link["href"].strip()  for link in links]

  info = []
  # printing all values
  for i, (title, date, month, link) in enumerate(zip(title, date, month, link)):
    data = [str(i+1),title, date, month, link]
    info.append(data)
    
    doc += (f'{str(i+1)}: {title} --> [{date}-{month}]\n<br>{link}\n\n<br><br>')
    # print(f'{title} \n{date}-{month}\n{link}\n')
    # print(data)
  return doc

data = parsing_notice_board(url)

email_portion = ""
email_portion += data
email_portion += ('<br>------<br>')
email_portion +=('<br><br>End of Message')

# print(email_portion)



# smtp part 

SERVER = 'smtp.gmail.com' 
PORT = 587 
FROM =  'jacobcass73@gmail.com' # "your from email id"
TO = ['rafath.auvee@gmail.com', 'yeasir06@gmail.com'] # "your to email ids"  # can be a list
PASS = password.password # "your email id's password"


msg = MIMEMultipart()
msg['Subject'] = 'BAUST Notice Board [Automated Email]' + ' ' + str(now.day) + ' - ' + str(now.month) + '-' + str(
    now.year)
msg['From'] = FROM
msg['To'] = ", ".join(TO)

msg.attach(MIMEText(email_portion, 'html'))
# fp.close()

print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
#server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()
