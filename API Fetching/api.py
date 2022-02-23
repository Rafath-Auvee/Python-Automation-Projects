import requests as req 
import csv

res = req.get('https://animechan.vercel.app/api/quotes/character?name=levi' , stream=True)

print(res.status_code)
# print(res.json())

anime_name = res.json()
anime_list = []
csvheader = ['Anime Title', 'Character', 'Quote']

# print(anime_name[0]['quote'])

for i in anime_name:
  listing = [i['anime'],i['character'],i['quote']]
  anime_list.append(listing)
  
print(anime_list)

with open('anime.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)
  
  writer.writerow(csvheader)
  writer.writerows(anime_list)