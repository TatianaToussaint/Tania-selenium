import time
import pytest
from selenium.webdriver.common.by import By
from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://www.target.com/") #Open https://www.target.com/

def test_weekly_ads (driver, target_title=None):

    driver.find_element(By.LINK_TEXT, "Weekly Ad").click()   #Press Weekly Ad link
    weekly_ads_handle = driver.current_window_handle
    driver.find_element(By.ID, "bullseye").click()  #Press the Target logo
    time.sleep(3)

    for handle in driver.window_handles:
        if handle != weekly_ads_handle:
            target_window_handle = handle
            break

    driver.switch_to.window(target_window_handle)
    target_title = "Target : Expect More. Pay Less."
    assert driver.title == target_title
    driver.close()

    driver.switch_to.window(weekly_ads_handle)
    weekly_ads_title = "Weekly Deals In Stores Now : Target Weekly Ad"
    assert driver.title == weekly_ads_title
    time.sleep(2)

    visible_text = driver.find_element(By.TAG_NAME, "h3").text
    assert visible_text == "Weekly Ads & Catalogs"

    time.sleep(10)

