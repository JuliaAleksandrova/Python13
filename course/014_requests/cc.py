import requests
from bs4 import BeautifulSoup as BS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

usd_to_yen = 'https://www.google.com/search?q=usd+to+yen&oq=usd+to+ye&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABKgCALACAA&sourceid=chrome&ie=UTF-8'
response = requests.get(usd_to_yen, headers=headers)
soup = BS(response.content, 'html.parser')
data = soup.find('span', class_='DFlfde SwHCTb')
print(float(data.text.replace(',', '.')))
print(type(data['data-value']))