#11/02/2020

from bs4 import BeautifulSoup
import requests
import os

fillet = r'.\test.html'
with open(fillet) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div', class_='article'):
    hd = article.h2.text
    print(hd)
    para = article.p.text
    print(para)

    print()
