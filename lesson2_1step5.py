from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element= browser.find_element_by_id("input_value")
    x=x_element.text
    y=calc(x)
    y_value = browser.find_element_by_id("answer")
    y_value.send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radiobtn1 = browser.find_element_by_css_selector("[for='robotsRule']").click()
    button = browser.find_element_by_class_name("btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()


