from urllib import response
import requests as req
from bs4 import BeautifulSoup as bs
import csv
import datetime

response = req.get("https://www.baust.edu.bd/category/notice/")
data = response.content
result = bs(data, 'html.parser')

# print(result.prettify())

all_notices = result.find_all("div", attrs={"class" : "ArchItemDiv"})
print(all_notices)
