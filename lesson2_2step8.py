from selenium import webdriver
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector('[name="firstname"]').send_keys('Lisin')
    browser.find_element_by_css_selector('[name="lastname"]').send_keys('Anton')
    browser.find_element_by_css_selector('[name="email"]').send_keys('lisin94@kk.com')
    send_file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir,'lll.txt')
    send_file.send_keys(file_path)
    browser.find_element_by_class_name("btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()
