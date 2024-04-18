import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("https://the-internet.herokuapp.com/tables")


def test_tables(driver):
    column_number = 4

    rows = driver.find_elements(By.XPATH, "//table[2]/tbody/tr")
    while len(rows) == 0:  # sinchronization
        rows = driver.find_elements(By.XPATH, "//table[2]/tbody/tr")

    number_of_rows = len(rows)
    print("The number of rows is:", number_of_rows)

    for row in rows:
        print(row.text)

    headings = driver.find_elements(By.XPATH, "//table[2]/thead/tr/th")
    number_of_columns = len(headings)
    print("The number of columns is:", number_of_columns)

    # 1
    print("\nMethod 1")
    for row in rows:
        print(row.text.split(" ")[column_number - 1])

    #2
    print("\nMethod 2")
    for i in range(1,number_of_rows + 1):
        cell_xpath = "//table[2]/tbody[1]/tr[" + str(i) + "]/td[" + str(column_number) + "]"
        print(driver.find_element(By.XPATH, cell_xpath).text)

    #3
    print("\nMethod 3")
    dues = driver.find_elements(By.CLASS_NAME, "dues")
    for i in range(1, number_of_rows + 1):
        print(dues[i].text)