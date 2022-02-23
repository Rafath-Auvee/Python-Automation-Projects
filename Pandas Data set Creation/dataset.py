import requests as req
from bs4 import BeautifulSoup as bs
import datetime
import pandas as pd

# collecting current time 
now = datetime.datetime.now()

url = "https://www.baust.edu.bd/category/notice/"

# parsing BAUST notice board 
def parsing_notice_board(url):
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
    # print(f'{title} \n{date}-{month}\n{link}\n')
    print(data)
  return data


csvheader = ['No', 'Title', 'Date', 'Month', 'Links']
value = parsing_notice_board(url)

df = pd.DataFrame(value , columns= csvheader)

df.head()