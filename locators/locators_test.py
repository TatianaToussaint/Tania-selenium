import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://opencart.abstracta.us/")

def test_locators(driver):
#class name
    driver.find_element(By.CLASS_NAME, "swiper-button-next").click()
#id
    driver.find_element(By.ID, "cart-total").click()
#name
    driver.find_element(By.NAME, "search").send_keys("MacBook") #,Keys.ENTER)

#CSS selector
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()

#link text
    driver.find_element(By.LINK_TEXT, "Your Store").click()

#partial link text
    driver.find_element(By.PARTIAL_LINK_TEXT, "PDAs").click()

#tag name
    visible_text = driver.find_element(By.TAG_NAME, "body").text
    print(visible_text)

#Hpath
    driver.find_element(By.XPATH, "//div[1]/div[1]/div[2]/div[2]/button[1]/span")

    

    time.sleep(10)