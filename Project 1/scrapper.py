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

names = result.find_all("h3", attrs={"class": "title"})
ranks = result.find_all("h6", attrs={"class": "designation-title"})
phones = result.find_all("span", attrs={"class": "designation-title"})
print(ranks)

for name,rank in zip(names,ranks):
    data = [name.string.strip(), rank.string.strip()]
    print(data)
    # print(f'{name.string.strip()} = {rank.string.strip()}')  
    # print(rank.string.strip())

