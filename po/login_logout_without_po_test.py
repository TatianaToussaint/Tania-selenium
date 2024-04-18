import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from common.base_test import driver

def click_element(driver, locator):
    WebDriverWait(driver, 15).until(ec.element_to_be_clickable(locator)).click()


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://the-internet.herokuapp.com/login")

def test_valid_login(driver):
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    click_element(driver, (By.CLASS_NAME, "radius"))
    confirm_login = driver.find_element(By.ID, "flash")
    assert "You logged into" in confirm_login.text

    click_element(driver, (By.CSS_SELECTOR, ".button.secondary.radius"))
    confirm_logout = driver.find_element(By.ID, "flash")
    assert "You logged out" in confirm_logout.text
    time.sleep(3)
