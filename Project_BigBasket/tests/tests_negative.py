import time
import allure
import pytest

from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader
from utils.logger import LogGenerator
from utils.screenshot_util import ScreenshotUtil

logger = LogGenerator.loggen()


# ==========================================
# TEST CASE 1: INVALID MOBILE NUMBER
# ==========================================

@allure.feature("BigBasket Negative Test Cases")
@allure.severity(allure.severity_level.CRITICAL)

def test_negative_scenarios(driver):

    login = LoginPage(driver)

    logger.info("Opening BigBasket Website")
    login.open_bigbasket()
    time.sleep(5)

    logger.info("Clicking Login Button")
    login.click_login()
    time.sleep(3)

    logger.info("Entering Invalid Mobile Number")
    login.enter_mobile_email("12345")
    time.sleep(3)

    logger.info("Checking Continue Button Disabled")

    assert login.is_continue_button_disabled(), "Continue button should be disabled"

    print("Invalid Mobile Number Test Passed")


# ==========================================
# TEST CASE 2: INVALID OTP
# ==========================================

@allure.title("Invalid OTP Test")
@pytest.mark.order(6)
@pytest.mark.usefixtures("driver")

def test_invalid_otp(driver):

    login = LoginPage(driver)

    logger.info("Reading CSV Data")
    data = CSVReader.get_test_data("data/test_data.csv")

    # FIXED CSV KEY
    mobile = data[0]["mobile_number"]

    logger.info("Opening BigBasket Website")
    login.open_bigbasket()
    time.sleep(5)

    logger.info("Clicking Login Button")
    login.click_login()
    time.sleep(3)

    logger.info("Entering Mobile Number")
    login.enter_mobile_email(mobile)
    time.sleep(3)

    logger.info("Clicking Continue Button")
    login.click_continue()
    time.sleep(5)

    logger.info("Enter Invalid OTP Manually")
    time.sleep(15)

    logger.info("Clicking Verify & Continue")
    login.click_verify_continue()
    time.sleep(5)

    # Screenshot
    ScreenshotUtil.capture_screenshot(driver, "invalid_otp")

    logger.info("Screenshot Captured for Invalid OTP")

    # =====================================================
    # FIXED ASSERTION (STATE-BASED, NOT TEXT-BASED)
    # =====================================================
    assert login.is_user_not_logged_in(), "OTP should be invalid but login succeeded"

    logger.info("Invalid OTP Test Passed")

    print("Invalid OTP Test Passed")