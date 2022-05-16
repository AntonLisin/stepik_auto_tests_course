from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        try:
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
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Не тот текст")
        finally:
            time.sleep(5)
            browser.quit()
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        try:
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
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Не тот текст")
        finally:
            time.sleep(5)
            browser.quit()
if __name__ == "__main__":
    unittest.main()

