import os
import time

import pytest

from common.base_test import login_page
import csv

from utils.utilis import get_rows

username = "tomsmith"
password = "SuperSecretPassword!"
data_file = os.path.join(os.path.dirname(__file__), "../data/invalid.csv")

def test_valid_login(login_page):
    home_page = login_page.open() \
                            .valid_login(username, password)
    confirm_login = home_page.get_confirm_login()
    assert "You logged into" in confirm_login

    confirm_logout = home_page.logout() \
                                .get_confirmation()
    assert "You logged out" in confirm_logout


@pytest.mark.parametrize("username, password, expected", get_rows(data_file))
def test_invalid_login(login_page, username, password, expected):
    login_error = login_page.open() \
                    .invalid_login(username,password) \
                    .get_confirmation()

    assert expected in login_error

    time.sleep(3)


