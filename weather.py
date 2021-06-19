from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import requests

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

file = open('product.csv', 'w')
headers = 'brand, price\n'
file.write(headers)

# retrieving the data
page = uReq(url)
page_html = page.read()

#parsing the html data
soup = bs(page_html, 'html.parser')
items = soup.findAll('div', {'class': 'item-cell'})
for item in items:
    brand = item.div.div.div.a.img['title']
    print('brand: ',brand)
    prices = item.findAll('li', {'class': 'price-current'})
    for price in prices:
        cost = price.strong.text
        file.write(brand + ',' + cost.replace(',', '') + '\n')

file.close()
page.close()
