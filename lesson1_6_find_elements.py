import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
f_name = browser.find_element_by_name('first_name')
f_name.send_keys('Lisin')
l_name = browser.find_element_by_name('last_name')
l_name.send_keys('Anton')
city = browser.find_element_by_class_name('city')
city.send_keys('Kazan')
country = browser.find_element_by_id('country')
country.send_keys('Russia')
button = browser.find_element_by_id("submit_button")
button.click()
time.sleep(10)
browser.quit()
