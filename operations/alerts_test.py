import time

import pytest
from selenium.webdriver.common.by import By
from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")


def test_jsalert(driver):
    driver.find_element(By.XPATH, "//ul[1]/li[1]/button[1]").click()
    time.sleep(4)
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert"
    alert.accept()
    time.sleep(4)

def test_jsconfirm(driver):
    driver.find_element(By.XPATH, "//ul[1]/li[2]/button[1]").click()
    time.sleep(4)
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()
    time.sleep(4)