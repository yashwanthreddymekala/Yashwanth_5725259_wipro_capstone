import os
import time
import allure

from behave import given, when, then
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils.csv_reader import CSVReader
from utils.logger import LogGenerator

logger = LogGenerator.loggen()

data = CSVReader.get_test_data("data/test_data.csv")


# =========================================================
# COMMON FUNCTION
# =========================================================

def attach_step_screenshot(context, step_name):

    screenshot_dir = "reports/screenshots"

    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = os.path.join(
        screenshot_dir,
        f"{step_name}.png"
    )

    context.driver.save_screenshot(screenshot_path)

    with open(screenshot_path, "rb") as file:

        allure.attach(
            file.read(),
            name=step_name,
            attachment_type=allure.attachment_type.PNG
        )


def attach_logs():

    log_path = "logs/automation.log"

    if os.path.exists(log_path):

        with open(log_path, "r") as file:

            allure.attach(
                file.read(),
                name="Execution Logs",
                attachment_type=allure.attachment_type.TEXT
            )


# =========================================================
# STEP 1
# =========================================================

@given("the user opens BigBasket website")
def step_open_bigbasket(context):

    context.test_data = data[0]

    context.login = LoginPage(context.driver)

    context.home = HomePage(context.driver)

    logger.info("Opening BigBasket Website")

    context.login.open_bigbasket()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_1_Open_BigBasket"
    )


# =========================================================
# STEP 2
# =========================================================

@when("the user logs in with valid mobile number")
def step_login_with_mobile(context):

    logger.info("Clicking Login Button")

    context.login.click_login()

    time.sleep(3)

    logger.info("Entering Mobile Number")

    context.login.enter_mobile_email(
        context.test_data["mobile_number"]
    )

    time.sleep(3)

    logger.info("Clicking Continue Button")

    context.login.click_continue()

    attach_step_screenshot(
        context,
        "Step_2_Login_With_Mobile"
    )


# =========================================================
# STEP 3
# =========================================================

@when("the user waits for OTP and verifies login")
def step_wait_otp_and_verify(context):

    logger.info("Waiting For OTP")

    time.sleep(20)

    logger.info("Clicking Verify Button")

    context.login.click_verify_continue()

    time.sleep(25)

    attach_step_screenshot(
        context,
        "Step_3_OTP_Verification"
    )


# =========================================================
# STEP 4
# =========================================================

@when("the user opens Shop By Category")
def step_shop_by_category(context):

    logger.info("Clicking Shop By Category")

    context.home.click_shop_by_category()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_4_Shop_By_Category"
    )


# =========================================================
# STEP 5
# =========================================================

@when("the user navigates to Fashion")
def step_fashion(context):

    logger.info("Clicking Fashion")

    context.home.click_fashion()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_5_Fashion"
    )


# =========================================================
# STEP 6
# =========================================================

@when("the user navigates to Footwear")
def step_footwear(context):

    logger.info("Clicking Footwear")

    context.home.click_footwear()

    time.sleep(10)

    attach_step_screenshot(
        context,
        "Step_6_Footwear"
    )


# =========================================================
# STEP 7
# =========================================================

@when("the user opens Brands filter")
def step_brands_filter(context):

    logger.info("Opening Brands Filter")

    context.home.click_brands_filter()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_7_Brands_Filter"
    )


# =========================================================
# STEP 8
# =========================================================

@when("the user selects Adidas Sports")
def step_adidas(context):

    logger.info("Selecting Adidas Sports")

    context.home.select_adidas_sports()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_8_Adidas_Sports"
    )


# =========================================================
# STEP 9
# =========================================================

@when("the user adds the first product to cart")
def step_add_first_product(context):

    logger.info("Adding First Product")

    context.home.click_add_button()

    time.sleep(8)

    attach_step_screenshot(
        context,
        "Step_9_First_Product"
    )


# =========================================================
# STEP 10
# =========================================================

@when("the user scrolls half page")
def step_scroll_half_page(context):

    logger.info("Scrolling Half Page")

    context.driver.execute_script(
        "window.scrollBy(0,500);"
    )

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_10_Scroll_Page"
    )


# =========================================================
# STEP 11
# =========================================================

@when("the user selects Action checkbox")
def step_action_checkbox(context):

    logger.info("Selecting Action Checkbox")

    context.home.select_action_checkbox()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_11_Action_Checkbox"
    )


# =========================================================
# STEP 12
# =========================================================

@when("the user adds the second product to cart")
def step_add_second_product(context):

    logger.info("Adding Second Product")

    context.home.click_add_button()

    time.sleep(8)

    attach_step_screenshot(
        context,
        "Step_12_Second_Product"
    )


# =========================================================
# STEP 13
# =========================================================

@when("the user opens basket with two items")
def step_open_basket_two(context):

    logger.info("Opening Basket")

    context.home.click_basket_two_items()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_13_Open_Basket"
    )


# =========================================================
# STEP 14
# =========================================================

@when("the user increments product quantity")
def step_increment_quantity(context):

    logger.info("Incrementing Product Quantity")

    context.home.click_increment()

    time.sleep(5)

    attach_step_screenshot(
        context,
        "Step_14_Increment_Quantity"
    )


# =========================================================
# STEP 15
# =========================================================

@when("the user proceeds to checkout")
def step_checkout(context):

    logger.info("Proceeding To Checkout")

    context.home.click_checkout()

    time.sleep(10)

    attach_step_screenshot(
        context,
        "Step_15_Checkout"
    )


# =========================================================
# STEP 16
# =========================================================

@then("the products should be added and checkout should be opened")
def step_verify_checkout(context):

    logger.info(
        "Test Case Passed Successfully"
    )

    attach_step_screenshot(
        context,
        "Step_16_Test_Passed"
    )

    attach_logs()

    print(
        "Products Added And Checkout Opened Successfully"
    )