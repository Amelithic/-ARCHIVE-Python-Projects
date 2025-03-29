#21/04/2020
from selenium import webdriver
import time

web_page = 'https://www.timeanddate.com/weather/ireland/waterford/historic?month=1&year=2010'
#chrome_path = r".\chromedriver.exe"
#driver = webdriver.Chrome(chrome_path)
driver = webdriver.Chrome()
driver.get(web_page)
driver.maximize_window()
driver.find_element_by_xpath("""//*[@id="mpo"]/div/div/div/div[2]/div[1]/button[1]""").click()

leftNav = driver.find_element_by_xpath("""//*[@id="navLeft"]""")
posts = driver.find_elements_by_class_name('temp')
count = 0
while (count < 90):
    leftNav.click()
    count = count + 1
if (count == 96):
    for post in posts:
       print(post.text)
       print(count)
       print()
       time.sleep(0.5)
       driver.find_element_by_xpath("""//*[@id="navRight"]""").click()
       
