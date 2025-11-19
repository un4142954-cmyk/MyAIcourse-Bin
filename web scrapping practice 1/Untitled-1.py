import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.amazon.com/b/?_encoding=UTF8&node=21217035011&ref_=cct_cg_SHnav2_2a1&pf_rd_p=0b4b41c4-3a43-4ea8-8624-5c61818e900b&pf_rd_r=M47SQ6241J1S9F0A8T13"
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html5lib')

quotes = []  # A list to store quotes
table = soup.find('div',attrs={'data-csa-a-id':'j8w l1v-pf5e16-2umip7-lnzk5c'})

for row in table.find_all('div',
                          attrs= {'class':'a-declarative'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['URL'] = row.a['href']
    quote['img'] = row.img['scr']
    quote['lines'] = row.img['alt']

    quotes.append(quote)


