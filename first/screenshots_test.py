from Screenshot import Screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_screenshot_of_visible_area():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    driver.save_screenshot("visible_area.png")
    driver.quit()

def test_screenshot_of_full_page_firefox():
    driver = webdriver.Firefox()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    driver.save_full_page_screenshot("full_page_firefox.png")
    driver.quit()


def test_screenshot_of_full_page_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    scr = Screenshot.Screenshot()
    scr.full_screenshot(driver, save_path=r'.', image_name="full_page_chrome.png")
    driver.quit()


def test_screenshot_of_web_element():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    driver.maximize_window()
    logo = driver.find_element(By.ID,"selenium_webdriver")
    screenshot = logo.screenshot_as_png
    with open("logo.png", 'wb') as f:
        f.write(screenshot)
    driver.quit()