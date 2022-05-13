from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    s = str(int(x)+int(y))
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_visible_text(s)
    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector(f"[value='{s}']").click()
    browser.find_element_by_class_name("btn-default").click()
finally:
    time.sleep(10)
    browser.quit()
