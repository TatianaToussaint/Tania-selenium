from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
import os

from pages.LoginPage import LoginPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver = webdriver.Chrome(options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture
def login_page():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver = webdriver.Chrome(options)
    chrome_driver.maximize_window()
    yield LoginPage(chrome_driver)
    chrome_driver.quit()


