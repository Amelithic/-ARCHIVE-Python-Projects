#21/04/2020
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(r'.\chromedriver.exe')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome()
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('im watching you')
time.sleep(1)
search_box.send_keys(Keys.CONTROL, 'a')
search_box.send_keys(Keys.BACKSPACE)
search_box.send_keys('google')
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
time.sleep(10)
driver.quit()

#posts = driver.find_elements_by_class_name('temp')
#for post in posts:
#    print(post.text)
#    print()
#    time.sleep(0.5
