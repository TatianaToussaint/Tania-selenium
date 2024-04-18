import pytest
from selenium.webdriver.common.by import By

from common.base_test import driver

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://opencart.abstracta.us/")

def test_links(driver):
    links = driver.find_elements(By.TAG_NAME, "a")
    number_of_links = len(links)
    print("The number of links:", number_of_links)

    for i in range(number_of_links):
        print(i + 1, links[i].text, ";", links[i].get_attribute('href'))

def test_page_html(driver):
    print("Page HTML code:")
    print(driver.page_source)