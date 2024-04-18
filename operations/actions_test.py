import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common.base_test import driver


@pytest.fixture(autouse=True)
def action_builder(driver):
    return ActionChains(driver)


def test_hover_over(driver, action_builder):
    driver.get("https://the-internet.herokuapp.com/hovers")
    user1 = driver.find_element(By.XPATH, "//div[1]/div[1]/h5[1]")
    assert not user1.is_displayed()

    img1 = driver.find_element(By.XPATH, "//div[1]/div[1]/img[1]")
    action_builder.move_to_element(img1).perform()
    assert user1.is_displayed()
    time.sleep(5)


def test_move_mouse_with_offset(driver, action_builder):
    driver.get("https://www.webminal.org/")
    register = driver.find_element(By.LINK_TEXT, "Register")
    action_builder.move_by_offset(register.location["x"] + 8, register.location["y"] + 8).click().perform()
    assert driver.find_element(By.XPATH, "//h2[1]").text == "Join"


def test_drag_and_drop(driver, action_builder):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    sourse = driver.find_element(By.ID, "column-a")
    destination = driver.find_element(By.ID, "column-b")
    action_builder.drag_and_drop(sourse, destination).perform()
    assert destination.text == "A"
    time.sleep(5)


def test_right_and_double_click(driver, action_builder):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/dropdown-menu.html")
    dropdown2 = driver.find_element(By.ID, "my-dropdown-2")
    action_builder.context_click(dropdown2).perform()
    context_menu = driver.find_element(By.ID, "context-menu-2")
    assert context_menu.is_displayed()
    time.sleep(3)

    dropdown3 = driver.find_element(By.ID, "my-dropdown-3")
    action_builder.double_click(dropdown3).perform()
    context_menu3 = driver.find_element(By.ID, "context-menu-3")
    assert context_menu3.is_displayed()
    time.sleep(3)