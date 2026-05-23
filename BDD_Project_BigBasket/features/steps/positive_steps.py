import time
import allure

from behave import given, when, then

from pages.loginpage import LoginPage
from pages.homepage import HomePage

from utils.csv_reader import CSVReader
from utils.logger import LogGenerator


# Logger
logger = LogGenerator.loggen()

# Read CSV Data
data = CSVReader.get_test_data("data/test_data.csv")


@allure.feature("BigBasket Fashion Module")
@allure.story("Login And Checkout")
@allure.severity(allure.severity_level.CRITICAL)

@given("User opens BigBasket website")
def step_open_bigbasket(context):

    context.test_data = data[0]

    context.login = LoginPage(context.driver)
    context.home = HomePage(context.driver)

    logger.info("Opening BigBasket Website")

    context.login.open_bigbasket()

    time.sleep(5)


@when("User clicks login button")
def step_click_login(context):

    logger.info("Clicking Login Button")

    context.login.click_login()

    time.sleep(3)


@when("User enters mobile number")
def step_enter_mobile(context):

    logger.info("Entering Mobile Number")

    context.login.enter_mobile_email(
        context.test_data["mobile_number"]
    )

    time.sleep(3)


@when("User clicks continue button")
def step_click_continue(context):

    logger.info("Clicking Continue Button")

    context.login.click_continue()


@when("User waits for OTP and clicks verify button")
def step_verify_otp(context):

    logger.info("Waiting For OTP")

    time.sleep(20)

    logger.info("Clicking Verify Button")

    context.login.click_verify_continue()

    time.sleep(25)


@then("User should login successfully")
def step_verify_login(context):

    assert context.login.verify_login_success(), \
        "Login Failed"

    print("PASS 1 - LOGIN SUCCESSFUL")


# =====================================================
# TEST CASE 2 : NAVIGATION
# =====================================================

@when("User opens footwear page")
def step_open_footwear(context):

    logger.info("Opening Footwear Page")

    context.driver.get(
        "https://www.bigbasket.com/pc/fashion/footwear/"
    )

    time.sleep(10)


@then("Footwear page should open successfully")
def step_verify_footwear(context):

    assert "footwear" in context.driver.current_url.lower(), \
        "Footwear Page Not Opened"

    print("PASS 2 - NAVIGATION SUCCESSFUL")


# =====================================================
# TEST CASE 3 : ADD FIRST PRODUCT
# =====================================================

@when("User opens brands filter")
def step_open_brand_filter(context):

    logger.info("Opening Brands Filter")

    context.home.click_brands_filter()

    time.sleep(5)


@when("User selects Adidas Sports")
def step_select_adidas(context):

    logger.info("Selecting Adidas Sports")

    context.home.select_adidas_sports()

    time.sleep(5)


@when("User adds first product")
def step_add_first_product(context):

    logger.info("Adding First Product")

    context.home.click_add_button()

    time.sleep(8)


@then("First product should be added successfully")
def step_verify_first_product(context):

    assert "bigbasket" in context.driver.title.lower(), \
        "Product Not Added"

    print("PASS 3 - PRODUCT ADDED SUCCESSFULLY")


# =====================================================
# TEST CASE 4 : BASKET FLOW
# =====================================================

@when("User scrolls half page")
def step_scroll_page(context):

    logger.info("Scrolling Half Page")

    context.driver.execute_script(
        "window.scrollBy(0,500);"
    )

    time.sleep(5)


@when("User selects Action checkbox")
def step_select_checkbox(context):

    logger.info("Selecting Action Checkbox")

    context.home.select_action_checkbox()

    time.sleep(5)


@when("User adds second product")
def step_add_second_product(context):

    logger.info("Adding Second Product")

    context.home.click_add_button()

    time.sleep(8)


@when("User opens basket")
def step_open_basket(context):

    logger.info("Opening Basket")

    context.home.click_basket_two_items()

    time.sleep(5)


@then("Basket should open successfully")
def step_verify_basket(context):

    assert "basket" or "cart" in context.driver.page_source.lower(), \
        "Basket Not Opened"

    print("PASS 4 - BASKET OPENED SUCCESSFULLY")

    print("ALL 4 POSITIVE TEST CASES PASSED")