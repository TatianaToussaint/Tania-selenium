import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from common.base_test import driver

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://automationbookstore.dev/")


def test_below_and_left_of(driver):
    book = driver.find_element(
        locate_with(By.TAG_NAME, "li")
        .below(driver.find_element(By.ID, "pid1"))
        .to_left_of(driver.find_element(By.ID, "pid6"))
    )
    id = book.get_attribute("id")
    assert id == "pid5"
    time.sleep(5)

def test_above_and_rigt_of(driver):
    book = driver.find_element(
        locate_with(By.TAG_NAME, "li")
        .above(driver.find_element(By.ID, "pid6"))
        .to_right_of(driver.find_element(By.ID, "pid1"))
    )
    id = book.get_attribute("id")
    assert id == "pid2"
    time.sleep(5)