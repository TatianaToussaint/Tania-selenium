import time

import pytest
from selenium.webdriver.common.by import By
from common.base_test import driver


@pytest.fixture(autouse=True)
def setup(driver):
    driver.get("http://www.uitestingplayground.com/dynamictable/")


def test_all_columns_in_the_table(driver):
    headers = driver.find_elements(By.XPATH, "//div[@role='table']//span[@role='columnheader']")
    print("Headings of columns are:")
    for header in headers:
        print(header.text)

    network_index = None
    for index, header in enumerate(headers):
        if header.text == 'Network':
            network_index = index
            print(f"The column number: {index + 1}")
            break

    if network_index is not None:
        rows = driver.find_elements(By.XPATH, "//div[@role='table']//div[@role='rowgroup']/div[@role='row']")
        print("Contents of 'Network' column:")
        for row in rows:
            cells = row.find_elements(By.XPATH, ".//span[@role='cell']")
            if len(cells) > network_index:
                print(cells[network_index].text)
    else:
        print("'Network' column was not found.")

    time.sleep(4)