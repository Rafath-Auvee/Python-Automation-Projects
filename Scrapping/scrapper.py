from unittest import result
from urllib import response
import requests as req
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import csv

now = datetime.datetime.now()

#email content placeholder
content = ''

def info(url):
  print("Parsing All Data")
  item = ''
  
#Testing 

response = req.get("https://baust.edu.bd/cse/employees/")
data = response.content
result = bs(data, 'html.parser')

# print(result.prettify())

permanent = result.find("div", attrs={"class": "row clearfix"}) 
# print(permanent)
names = permanent.find_all("h3", attrs={"class": "title"})
ranks = permanent.find_all("h6", attrs={"class": "designation-title"})
stars = permanent.find_all("span", attrs={"class": "qualification"})
all_phones = permanent.find_all("div", attrs={"class": "profile-contact-info"})
# all_phones = permanent.select("div.profile-contact-info > span")

# print(phones.findChild().text.strip())

phones = [phone.findChild().text.strip() for phone in all_phones]

# for phone in phones:
#   print(f"{phone}\n")

emails = permanent.find_all("span", attrs={"class": "email"})
emails = [email['title'] for email in emails]



data_list = []
csvheader = ['Name', 'Rank', 'Qualification', 'Email', 'Phone']

for name,rank,star,email,phone in zip(names,ranks,stars,emails,phones):
    data = [name.string.strip(), rank.string.strip(),star.string.strip(), email.strip() ,  phone.strip()]
    print(data)
    data_list.append(data)
    # print(f'{name.string.strip()} = {rank.string.strip()} = {star.string.strip()} --> {email.strip()} ==== {phone} ')      

with open('info2.csv', 'w', newline='',encoding='utf-8') as f:
  writer = csv.writer(f)
  writer.writerow(csvheader)
  writer.writerows(data_list)