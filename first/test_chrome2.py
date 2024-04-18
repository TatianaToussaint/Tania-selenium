import datetime
import os

import pytest
from selenium import  webdriver
from common.base_test import driver
from pathlib import Path

def take_screenshot(driver):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    Path("../screenshots").mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(os.path.join("../screenshots", f"screenshot{current_datetime}.png"))

@pytest.fixture(autouse=True)
def arrange(driver):
    driver.get("http://www.selenium.dev/")

def test1(driver):
    try:
        assert driver.title == "Selenium"
    except AssertionError:
        take_screenshot(driver)
        raise


def test2(driver):
    assert driver.current_url == "https://www.selenium.dev/"

#pytest --screenshot=on --screenshot_path=on first/test_chrome2.py
# command for terminal to create a screenshot when test failed