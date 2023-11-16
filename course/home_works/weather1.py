import requests
from bs4 import BeautifulSoup as BS
def get_weather(city):
    url = "https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    response = requests.get(url, headers)
    soup = BS(response.content, 'html.parser')
    temperature = soup.find('tbody').find('tr').find_all('td')[1].text.strip()
    return f"The temperature in {city} is {temperature}."
city = input("Enter the town/city name: ")
result = get_weather(city)

print(result)



#city = input("Enter the town/city name: ")
#result = get_weather(city)
# table = soup.find('table')
#towns = []
# for row in table.find_all('tr'):
#     columns = row.find_all('td')
#     if columns:
#         town = columns[0].text.strip()
#         towns.append(town)
#
# print(towns)