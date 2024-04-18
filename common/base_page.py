from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
   def __init__(self, driver):
       self.driver = driver

#stable operation
   def click_element(self, locator):
       WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(locator)).click()

   def open_page(self, url, title):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(ec.title_is(title))

   def find_element(self,locator):
       return WebDriverWait(self.driver, 15).until(ec.presence_of_element_located(locator))