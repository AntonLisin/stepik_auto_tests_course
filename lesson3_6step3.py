import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
def test_guest_should_see_login_link(browser, number):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{number}/step/1"cj
    browser.get(link)
    browser.find_element_by_tag_name("textarea").send_keys(answer)
    browser.find_element_by_css_selector(".submit-submission").click()
    corr_text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert corr_text == "Correct!", f"Не тот текст, получили - {corr_text}"


