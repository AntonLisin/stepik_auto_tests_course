from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_id("book")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    x= browser.find_element_by_id("input_value").text
    y=calc(x)
    y_value = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", y_value)
    y_value.send_keys(y)
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()



