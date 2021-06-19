from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

url = 'https://www.etsy.com/search?q=artwork&ref=auto-1'

page = uReq(url)
page_html = page.read()

soup = bs(page_html, 'html.parser')
items = soup.findAll('li', {'class': 'wt-list-unstyled wt-grid__item-xs-6 wt-grid__item-md-4 wt-grid__item-lg-3 wt-grid__item-xl-3 wt-order-xs-0 wt-order-md-0 wt-order-lg-0 wt-order-xl-0 wt-show-xs wt-show-md wt-show-lg wt-show-xl tab-reorder'})
print(len(items))
