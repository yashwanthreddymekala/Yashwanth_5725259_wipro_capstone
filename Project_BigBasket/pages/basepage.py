from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Open URL
    def open_url(self, url):
        self.driver.get(url)

    # Click Element
    def click_element(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Enter Text
    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    # Get Element Text
    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    # Check Element Displayed
    def is_displayed(self, locator):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False