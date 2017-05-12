#!/usr/bin/python3

# Stupid cunts...
# How am I supposed to find a box in my neightborhood
# with 10 addresses at a time on 156...
# https://www.post.lu/particuliers/courrier/trouver-une-boite-aux-lettres#

import requests

status_code = 200
url = 'https://www.post.lu/naos-microapps-app/ajax/json/getBoxForCity.json'
city = 'LUXEMBOURG'
page = 0
last_page = False
res = []

while not last_page:
  resp = requests.get(url, params={ 'city': city, 'page': page })
  resp_d = resp.json()
  last_page = resp_d['lastPage'] 
  page += 1
  for entry in resp_d['content']:
      entry.pop('id')
      entry.pop('localite')
      entry.pop('type')
      res.append(entry)

for entry in res:
  entry_csv = '%s;%s;%s' % (entry['rue'], entry['relevesSem'], entry['relevesSam'])
  print(entry_csv)
