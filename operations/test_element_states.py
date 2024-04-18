import time

import pytest
from selenium.webdriver.common.by import By

from common.base_test import driver

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://formy-project.herokuapp.com/form")

def test_read_input(driver):
    first = driver.find_element(By.ID, "first-name")
    first.send_keys("Tania")
    assert first.get_attribute("value") == "Tania"
    time.sleep(3)

def test_get_states(driver):
    radio = driver.find_element(By.ID, "radio-button-3")
    assert radio.is_displayed()

    radio.click()
    assert radio.is_selected()
    time.sleep(3)