import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.base_test import driver



@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://duckduckgo.com/")


def test_search_box(driver):
    search_box = driver.find_element(By.ID, "searchbox_input")
    search_box.send_keys("maven" + Keys.ENTER)
    time.sleep(4)

    search = driver.find_element(By.NAME, "q")
    maven = search.get_attribute("value")
    assert maven == "maven"

    maven_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Apache Maven")

    assert len(maven_link) != 0, "No links with the text 'apache maven' were found."
    time.sleep(4)
