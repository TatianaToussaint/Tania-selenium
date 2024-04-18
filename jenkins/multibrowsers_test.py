import os
import time

from selenium import webdriver

def get_driver(request):
    browser = request.config.getoption("--browser")
    os = request.config.getoption("--OS")
    print("Test server has", os)
    match browser:
        case "Chrome":
            return webdriver.Chrome()
        case "Firefox":
            return webdriver.Firefox()
        case "Edge":
            return webdriver.Edge()

def test_multibrowsers(request):
    driver = get_driver(request)
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()

    assert driver.title == "Selenium"
    print("Current URL:", driver.current_url)
    print("Browser name:", driver.name)

    time.sleep(3)
    driver.quit()