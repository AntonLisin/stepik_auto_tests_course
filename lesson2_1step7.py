from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element= browser.find_element_by_id("treasure")
    x = x_element.get_attribute('valuex')
    y=calc(x)
    y_value = browser.find_element_by_id("answer")
    y_value.send_keys(y)
    checkbox1 = browser.find_element_by_id("robotCheckbox").click()
    radiobtn1 = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_class_name("btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
