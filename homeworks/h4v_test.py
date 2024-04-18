import time

import pytest
from selenium.webdriver.common.by import By
from common.base_test import driver

heading = "CPU"
@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("http://www.uitestingplayground.com/dynamictable/")

def test_all_columns_in_the_table(driver):
    headers = driver.find_elements(By.XPATH, "//div[@role='table']//span[@role='columnheader']")
    print("Headings of columns are:")
    for header in headers:
        print(header.text, "", end='')

    index = 0
    for header in headers:
        index += 1
        if header.text == heading:
            break
    print(f"\nThe column number: {index}")

    rows = driver.find_elements(By.XPATH, "//div[@role='table']//div[@role='rowgroup']/div[@role='row']")
    for row in rows:
        print(row.text)
    print("Contents of "+ heading + " column:")
    for i in range(1, len(rows)):
        cell = driver.find_element(By.XPATH, "//div[3]/div[" + str(i) + "]/span[" + str(index) + "]")
        print(cell.text)