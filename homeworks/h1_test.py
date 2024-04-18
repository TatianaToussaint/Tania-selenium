import time
import pytest
from Screenshot import Screenshot
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.target.com/")


def test_target_registry(driver):
    # Press the link Registry click
    driver.find_element(By.LINK_TEXT, "Registry").click()

    # Press on the button Find a registry click
    driver.find_element(By.XPATH, "//button[contains(text(),'Find a registry')]").click()
    time.sleep(4)

    # Check that you are on the right page Search Results
    #assert driver.current_url == "https://www.target.com/gift-registry/search-results"
    assert driver.title == "Search Results : Gift Registry : Target"

    # and that the string Find a registry is present
    find_a_registry_element = driver.find_element(By.CSS_SELECTOR, ".lfA-Dem.styles__StyledHeading-sc-1xmf98v-0")
    assert find_a_registry_element.is_displayed()

    # by tag name  the string Find a registry is present
    visible_text = driver.find_element(By.TAG_NAME, "h1").text
    assert visible_text == "Find a registry"

    time.sleep(4)


