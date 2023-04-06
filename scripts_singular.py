
import urllib.parse

import cfscrape
from bs4 import BeautifulSoup

scraper = cfscrape.create_scraper()
response = scraper.get("https://www.PASTE_YOUR_URL_HERE.com")

soup = BeautifulSoup(response.content, 'lxml')
with open('NAME.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))


