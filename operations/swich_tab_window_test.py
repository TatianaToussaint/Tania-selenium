import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base_test import driver

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.selenium.dev/")

def test_switch_tabs_and_windows(driver):
    selenium_handle = driver.current_window_handle
    #print(selenium_handle)

    driver.switch_to.new_window('tab')  #new tab
    driver.get("https://www.python.org/")
    python_handle = driver.current_window_handle

    #new browser window
    driver.switch_to.new_window('window')
    driver.get("https://docs.pytest.org/")
    pytest_handle = driver.current_window_handle

    driver.switch_to.window(python_handle)
    time.sleep(6)
    driver.switch_to.window(selenium_handle)
    time.sleep(6)
    driver.switch_to.window(pytest_handle)
    print(driver.title)
    time.sleep(6)

    selenium_title = "Selenium"
    python_title = "Welcome to Python.org"
    pytest_title = "pytest: helps you write better programs — pytest documentation"

    swichTo(driver, python_title)
    time.sleep(6)
    swichTo(driver, selenium_title)
    time.sleep(6)
    swichTo(driver, pytest_title)
    time.sleep(6)

def swichTo(driver, window_title):
    all_windows = driver.window_handles
    for handle in all_windows:
        driver.switch_to.window(handle)
        if driver.title ==window_title:
            break

