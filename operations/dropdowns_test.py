import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base_test import driver

@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://testpages.eviltester.com/styled/basic-html-form-test.html")

def test_dropdowns(driver):
    dropdown = driver.find_element(By.NAME,  "dropdown")
    dr_select = Select(dropdown)
    dr_select.select_by_visible_text("Drop Down Item 6")
    dr_select.select_by_index(1)

    option_selected = dr_select.first_selected_option.text
    assert option_selected == "Drop Down Item 2"

    options = dr_select.options
    print("Total number of options:", len(options))
    for option in options:
        print(option.text)
    time.sleep(10)

def test_multiselect(driver):
    multi = driver.find_element(By.NAME, "multipleselect[]")
    ml_select = Select(multi)
    ml_select.deselect_all()
    ml_select.select_by_index(0)
    ml_select.select_by_index(1)

    time.sleep(10)