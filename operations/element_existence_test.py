import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.selenium.dev/selenium/docs/api/py/api.html")
    driver.find_element(By.LINK_TEXT, "selenium.webdriver.chrome.webdriver").click()


def test_element_existance(driver):
    list = driver.find_elements(By.NAME, "q")
    assert 1 == len(list)

    list = driver.find_elements(By.ID, "Tania")
    assert 0 == len(list)


def test_scrolling(driver):
    #    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2)")
    height = driver.execute_script("return document.body.scrollHeight")
    print("Page height in pixels", height)
    driver.execute_script("window.scrollTo(0, arguments[0] /2)", height)
    time.sleep(6)
