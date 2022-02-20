from urllib import response
import requests as req
from bs4 import BeautifulSoup as bs
import csv
import datetime

# collecting current time 
now = datetime.datetime.now()

url = "https://www.baust.edu.bd/category/notice/"

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
for title, date, month, link in zip(title, date, month, link):
  data = [title, date, month, link]
  info.append(data)
  print(f'{title} \n{date}-{month}\n{link}\n')
  # print(data)

