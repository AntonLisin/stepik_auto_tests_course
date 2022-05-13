from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    f_name = browser.find_element_by_css_selector('.first_block .first')
    f_name.send_keys('Lisin')
    l_name = browser.find_element_by_css_selector('.first_block .second')
    l_name.send_keys('Anton')
    email = browser.find_element_by_css_selector('.first_block .third')
    email.send_keys('lisin94@kk.com')
    button = browser.find_element_by_class_name("btn-default")
    button.click()
    time.sleep(4)

     # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
