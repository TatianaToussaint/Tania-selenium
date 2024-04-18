import time
import pytest
from selenium.webdriver.common.by import By
from common.base_test import driver
from selenium.webdriver import ActionChains


@pytest.fixture(autouse=True)
def action_builder(driver):
    return ActionChains(driver)

def test_rectangle_moved(driver, action_builder):
    time.sleep(5)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/drag-and-drop.html")
    element_to_drag = driver.find_element(By.ID, "draggable")

    x_sourse = element_to_drag.location['x']
    y_sourse = element_to_drag.location['y']

    action_builder.drag_and_drop_by_offset(element_to_drag, 67,67).perform()

    assert element_to_drag.location['x'] == x_sourse + 67
    assert element_to_drag.location['y'] == y_sourse + 67