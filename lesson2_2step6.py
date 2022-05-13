from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x= browser.find_element_by_id("input_value").text
    y=calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox1)
    checkbox1.click()
    radiobtn1 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn1)
    radiobtn1.click()29.01202663032254
    button = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
