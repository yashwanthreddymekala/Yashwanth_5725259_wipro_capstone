from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Login/ Sign Up')]"
    )

    MOBILE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter Phone number/ Email Id']"
    )

    CONTINUE_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Continue')]"
    )

    OTP_TEXT = (
        By.XPATH,
        "//h2[contains(text(),'Enter OTP')]"
    )

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Verify')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def open_bigbasket(self):
        self.open_url("https://www.bigbasket.com/")

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def enter_mobile_email(self, value):
        self.enter_text(self.MOBILE_INPUT, value)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def verify_otp_page(self):
        return self.is_displayed(self.OTP_TEXT)

    def click_verify_continue(self):

        element = self.driver.find_element(*self.VERIFY_BUTTON)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def is_continue_button_disabled(self):
        button = self.wait.until(
            EC.visibility_of_element_located(self.CONTINUE_BUTTON)
        )

        return not button.is_enabled()

    def verify_login_success(self):
        return "bigbasket" in self.driver.current_url.lower()

    def get_basket_count(self):
        return self.driver.find_element(
            By.XPATH,
            "//span[contains(@class,'count') or contains(@class,'badge')]"
        ).text

    INVALID_MOBILE_POPUP = (
        By.XPATH,
        "//*[contains(text(),'valid mobile number')]"
    )

    INVALID_OTP_POPUP = (
        By.XPATH,
        "//*[contains(text(),'Please Enter Valid OTP')]"
    )

    def get_invalid_mobile_popup(self):
        return self.wait.until(
            EC.presence_of_element_located(
                self.INVALID_MOBILE_POPUP
            )
        )

    def get_invalid_otp_popup(self):
        return self.wait.until(
            EC.presence_of_element_located(
                self.INVALID_OTP_POPUP
            )
        )

    def is_otp_error_displayed(self):
        try:
            return self.driver.find_element(
                "xpath",
                "//*[contains(text(),'invalid') or contains(text(),'Incorrect') or contains(text(),'try again')]"
            ).is_displayed()
        except:
            return False

    def is_user_not_logged_in(self):
        try:
            # If account/profile exists → user is logged in (FAIL case for negative test)
            self.driver.find_element(
                "xpath",
                "//span[contains(text(),'Account') or contains(text(),'Profile') or contains(text(),'Logout')]"
            )
            return False
        except:
            # If not found → user is NOT logged in (EXPECTED for invalid OTP)
            return True



