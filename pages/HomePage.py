from selenium.webdriver.common.by import By
from common.base_page import BasePage



class HomePage(BasePage):
    TITLE = "The Internet"

# elements
    BUTTON_LOGOUT = (By.CSS_SELECTOR, ".button.secondary.radius")
    CONFIRM_LOGIN = (By.ID, "flash")

# constractor
    def __init__(self, driver):
        super().__init__(driver)
        assert self.driver.title == self.TITLE

# sevices
    def logout(self):
        from pages.LoginPage import LoginPage
        self.click_element(self.BUTTON_LOGOUT)
        return LoginPage(self.driver)

    def get_confirm_login(self):
        return self.find_element(self.CONFIRM_LOGIN).text


