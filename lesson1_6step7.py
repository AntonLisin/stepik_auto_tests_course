import time
from selenium import webdriver
import math

try:
    link='http://suninjuly.github.io/find_xpath_form'
    browser = webdriver.Chrome()
    browser.get(link)
    fields = browser.find_elements_by_xpath('//input')
    for field in fields:
        field.send_keys('anton')
    button = browser.find_element_by_xpath('//button [@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
