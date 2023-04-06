import os
import urllib.parse

import cfscrape
from bs4 import BeautifulSoup

scraper = cfscrape.create_scraper()
urls = [
        "https://www.PASTE_YOUR_URL_HERE.com",
        "https://www.PASTE_YOUR_URL_HERE.com",
        "https://www.PASTE_YOUR_URL_HERE.com",

        
        
        ]

for url in urls:
    response = scraper.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    filename = os.path.basename(urllib.parse.urlparse(url).path)
    with open(filename + '.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
