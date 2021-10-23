import requests

result = requests.get("http://www.example.com")

## print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text, 'lxml')

## print(soup)

print(soup.select('title'))

site_p = soup.select('p')

print(site_p[0].getText())
