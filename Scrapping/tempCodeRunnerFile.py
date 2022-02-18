from unittest import result
from urllib import response
import requests as req
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

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
print(permanent)
names = permanent.find_all("h3", attrs={"class": "title"})
ranks = permanent.find_all("h6", attrs={"class": "designation-title"})
stars = permanent.find_all("span", attrs={"class": "qualification"})
emails = permanent.find_all("span", attrs={"class": "email"})
# phones = result.select("div.profile-contact-info span")

# all_phones = [phone['title']  for phone in phones] 
# print(all_phones)
all = [email['title'] for email in emails]
# print( [email['title'] for email in emails])

# for name,rank,star in zip(names,ranks,stars):
#     # data = [name.string.strip(), rank.string.strip()]
#     # print(data)
#     print(f'{name.string.strip()} = {rank.string.strip()} = {star.string.strip()} ')  


for name,rank,star, email in zip(names,ranks,stars,all):
    # data = [name.string.strip(), rank.string.strip()]
    # print(data)
    print(f'{name.string.strip()} = {rank.string.strip()} = {star.string.strip()} --> {email.strip()}\n')  