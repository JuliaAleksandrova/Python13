import requests
from requests.exceptions import HTTPError
import re
# url = 'https://xkcd.com/353/'
#
# response = requests.get(url, timeout =10)

# print(response.headers['server'])
#200 success
#300 redirect
#400 cient error
#500 server error

# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occured: {http_err}')
#     else:
#         print('Success')
from bs4 import BeautifulSoup as BS
url = 'https://www.gammatest.net/course/python'

response = requests.get(url)
soup = BS(response.content, 'html.parser')
# print(soup.title.text)
# print(soup.title.name)
# print(soup.div['class'])
# print(soup.a['href'])

# match = soup.find('div', class_='col-md-8')
# print(match.h2.text)

# matches = soup.find_all('a')
# for match in matches:
#     print(match['href'])
# matches = soup.find_all('script', type='text/javascript')
# print(soup.div.get_attribute_list('class'))
# print(soup.find_all(['a', 'title']))
# print(soup.find_all('a', string='Eesti keeles'))
# print(soup.find_all(string=True))
# matches = soup.title.findPrevious().findPrevious()
# print(matches)
# matches = soup.td.find_next_sibling()
# print(matches)
# matches = soup.td.find_next('div').h2
# print(matches)
# matches = soup.td.find_parents()
# print(matches)
matches = soup.td.findChildren()
print(matches)






