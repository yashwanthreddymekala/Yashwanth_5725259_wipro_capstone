import time
import allure

from behave import given, when, then

from pages.loginpage import LoginPage
from utils.csv_reader import CSVReader
from utils.logger import LogGenerator
from utils.screenshot_util import ScreenshotUtil

logger = LogGenerator.loggen()


# ==========================================
# INVALID MOBILE NUMBER
# ==========================================

@given("the user opens BigBasket website for negative testing")
def step_open_bigbasket_negative(context):

    context.login = LoginPage(context.driver)

    logger.info("Opening BigBasket Website")

    context.login.open_bigbasket()

    time.sleep(5)


@when("the user clicks login button")
def step_click_login(context):

    logger.info("Clicking Login Button")

    context.login.click_login()

    time.sleep(3)


@when("the user enters invalid mobile number")
def step_enter_invalid_mobile(context):

    logger.info("Entering Invalid Mobile Number")

    context.login.enter_mobile_email("12345")

    time.sleep(3)


@then("the continue button should remain disabled")
def step_verify_continue_disabled(context):

    logger.info("Checking Continue Button Disabled")

    assert context.login.is_continue_button_disabled(), \
        "Continue button should be disabled"

    print("Invalid Mobile Number Test Passed")


# ==========================================
# INVALID OTP
# ==========================================

@given("the user opens BigBasket website for OTP negative testing")
def step_open_bigbasket_otp(context):

    context.login = LoginPage(context.driver)

    logger.info("Reading CSV Data")

    context.data = CSVReader.get_test_data(
        "data/test_data.csv"
    )

    logger.info("Opening BigBasket Website")

    context.login.open_bigbasket()

    time.sleep(5)


@when("the user clicks login button for OTP test")
def step_click_login_otp(context):

    logger.info("Clicking Login Button")

    context.login.click_login()

    time.sleep(3)


@when("the user enters valid mobile number")
def step_enter_valid_mobile(context):

    mobile = context.data[0]["mobile_number"]

    logger.info("Entering Mobile Number")

    context.login.enter_mobile_email(mobile)

    time.sleep(3)


@when("the user clicks continue button")
def step_click_continue(context):

    logger.info("Clicking Continue Button")

    context.login.click_continue()

    time.sleep(5)


@when("the user enters invalid OTP manually")
def step_invalid_otp(context):

    logger.info("Enter Invalid OTP Manually")

    time.sleep(15)


@when("the user clicks verify and continue button")
def step_verify_continue(context):

    logger.info("Clicking Verify & Continue")

    context.login.click_verify_continue()

    time.sleep(5)


@then("the login should fail for invalid OTP")
def step_invalid_otp_assert(context):

    ScreenshotUtil.capture_screenshot(
        context.driver,
        "invalid_otp"
    )

    logger.info("Screenshot Captured for Invalid OTP")

    assert context.login.is_user_not_logged_in(), \
        "OTP should be invalid but login succeeded"

    logger.info("Invalid OTP Test Passed")

    print("Invalid OTP Test Passed")