#Amelithic 11-2-2020

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.timeanddate.com/weather/ireland/waterford/historic?month=1&year=2010').text

soup = BeautifulSoup(source, 'lxml')
#x = soup.find('div', attrs={"id":"weatherContainer"})    #finds the whole container where temperature is
body = soup.find('body')
#print(x.prettify)
wrapper = body.find('div', class_='wrapper')
main = wrapper.find('div', class_='main-content-div')
grid = main.find('article', class_='layout-grid--sky')
maingrid = grid.find('section', class_='layout-grid__main')
graphw = maingrid.find('div', class_='weather-graph')
containw = graphw.find('div', attrs={'id':'weatherContainer'})
w2 = containw.find('div', attrs={'id':'weather'})
wsect2 = w2.find('div', class_='section')
#can't find other objects, coded in javascript
print(wsect2)


# color 03 & cls & py .\Desktop\web_scrape\lets-a-go.pyw
