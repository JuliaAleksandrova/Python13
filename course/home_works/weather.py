import datetime

import requests
from bs4 import BeautifulSoup as BS

url = "https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/"
response = requests.get(url)
soup = BS(response.text, 'html.parser')

table = soup.find('table')

for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    data = []
    for col in columns:
        col_text = col.text
        text1 = col_text.strip()
        data.append(text1)
