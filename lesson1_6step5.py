import time
from selenium import webdriver
import math

try:
    link='http://suninjuly.github.io/find_link_text'
    browser = webdriver.Chrome()
    browser.get(link)
    texx=str(math.ceil(math.pow(math.pi, math.e)*10000))
    asd = browser.find_element_by_link_text(texx)
    asd.click()

    f_name = browser.find_element_by_name('first_name')
    f_name.send_keys('Lisin')
    l_name = browser.find_element_by_name('last_name')
    l_name.send_keys('Anton')
    city = browser.find_element_by_class_name('city')
    city.send_keys('Kazan')
    country = browser.find_element_by_id('country')
    country.send_keys('Russia')
    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
