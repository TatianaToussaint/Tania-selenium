import time
import pytest
from Screenshot import Screenshot
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from common.base_test import driver

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.target.com/")

def test_product(driver):
    # Type milk in the Search field
    item = driver.find_element(By.ID, "search")
    item.send_keys("milk",Keys.ENTER)
    time.sleep(4)

    # Refresh the page (then insert time.sleep(4))
    driver.refresh()
    time.sleep(4)

    # Verify that the string  (for ”milk”) exists on the page
    element = driver.find_element(By.CSS_SELECTOR, ".h-flex-align-center.h-text-grayDark")
    assert "for “milk”" in element.text

    # Take the page screenshot
    scr = driver.save_screenshot("visible_area.png")
    # Press the button Back in the browser (then insert time.sleep(4))
    driver.back()
    time.sleep(4)

    #Verify that you are on the starting page (target, expect more.pay less)
    assert driver.title == "Target : Expect More. Pay Less."
    time.sleep(4)

