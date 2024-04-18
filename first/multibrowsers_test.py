import os

from selenium import webdriver
import time

from utils.utilis import read_property


def get_driver():
    print(os.path.dirname(__file__))
    config_file = os.path.join(os.path.dirname(__file__), "../data/browser.config")
    print(config_file)

    browser = read_property("browser", config_file)
    print(browser)
    match browser:
        case "Chrome":
            return webdriver.Chrome()
        case "Firefox":
            return webdriver.Firefox()
        case "Edge":
            return webdriver.Edge()

def test_multibrowsers():
    driver = get_driver()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()

    assert driver.title == "Selenium"
    print("Current URL:", driver.current_url)
    print("Browser name", driver.name)

    time.sleep(3)
    driver.quit()
