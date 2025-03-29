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

posts = driver.find_elements_by_class_name('temp')
#posts2 = driver.find_elements_by_class_name('tempLow')
for post in posts:
    print(post.text)
    print()
    time.sleep(0.5)
