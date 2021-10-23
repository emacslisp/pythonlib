import requests

result = requests.get("http://www.example.com")

## print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text, 'lxml')

## print(soup)

print(soup.select('title'))

site_p = soup.select('p')

print(site_p[0].getText())


res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, "lxml")

for item in soup.select(".toctext"):
    print(item.getText())


res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')

index = 1
print(soup.select('.thumbimage'))

for item in soup.select('.thumbimage'):
    imgUrl = item['src']
    imageData = requests.get('https:{}'.format(imgUrl))
    f = open("{}.png".format(index), "wb")
    f.write(imageData.content)
    f.close()
    print(index)
    index+=1
    


