import time

import pytest
from selenium.common import ElementNotVisibleException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

def test_explicit(driver):
    driver.find_element(By.TAG_NAME, "button").click()
    # time.sleep(10)
#    hello_world = driver.find_element(By.ID, "finish")
    hello_world = WebDriverWait(driver, 15) \
                   .until(ec.visibility_of_element_located((By.ID, "finish")))
    assert hello_world.text == "Hello World!"

def test_impicit(driver):
    driver.implicitly_wait(15)
    driver.find_element(By.TAG_NAME, "button").click()
    hello_world = driver.find_element(By.ID, "finish")
    assert hello_world.text == "Hello World!"

def test_element_not_on_page_without_wait(driver):
    tanias = driver.find_elements(By.ID, "Tania")
    assert len(tanias) == 0

def test_element_not_on_page_with_implicit_wait(driver):
    driver.implicitly_wait(15)
    driver.find_element(By.ID, "Tania")

def test_element_not_on_page_with_explicit_wait(driver):
    WebDriverWait(driver, 15)\
     .until(ec.invisibility_of_element_located((By.ID, "Tania")))

def test_fluent(driver):
    driver.find_element(By.TAG_NAME, "button").click()
    # hello_world = WebDriverWait(driver, 15) \
    #     .until(ec.visibility_of_element_located((By.ID, "finish")))
    hello_world = WebDriverWait(driver, 15,
                                poll_frequency=1,
                                ignored_exceptions=(ElementNotVisibleException,
                                                      StaleElementReferenceException))\
        .until(ec.element_to_be_clickable((By.ID, "finish")))

    assert hello_world.text == "Hello World!"