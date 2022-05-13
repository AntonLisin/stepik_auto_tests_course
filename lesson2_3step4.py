from selenium import webdriver
import time
import os
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x= browser.find_element_by_id("input_value").text
    y=calc(x)
    y_value = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

