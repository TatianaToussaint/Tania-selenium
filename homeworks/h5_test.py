import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("http://opencart.abstracta.us/index.php")


def test_first_item_price(driver):
    driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()
    driver.find_element(By.ID, "list-view").click()
    dropdown = driver.find_element(By.ID, "input-sort")
    dr_select = Select(dropdown)
    dr_select.select_by_visible_text("Price (High > Low)")
    time.sleep(4)

    # price = driver.find_element(By.XPATH, "//div[contains(@class, 'product-layout')][1]//p[contains(@class, 'price')]").text.strip()
    # price_only = price.split("\n")[0].strip()
    # assert price_only == "$337.99"

    prices = driver.find_elements(By.CLASS_NAME, "price")
    assert "$337.99" in prices[0].text
    time.sleep(4)
