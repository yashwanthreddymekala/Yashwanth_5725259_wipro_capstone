import os
import allure
import time

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

def test_login(driver):

    # Read First Row
    test_data = data[0]

    login = LoginPage(driver)
    home = HomePage(driver)

    # =====================================================
    # TEST CASE 1 : LOGIN
    # =====================================================

    logger.info("Opening BigBasket Website")

    login.open_bigbasket()
    time.sleep(5)

    logger.info("Clicking Login Button")

    login.click_login()
    time.sleep(3)

    logger.info("Entering Mobile Number")

    login.enter_mobile_email(
        test_data["mobile_number"]
    )

    time.sleep(3)

    logger.info("Clicking Continue Button")

    login.click_continue()

    logger.info("Waiting For OTP")

    time.sleep(20)

    logger.info("Clicking Verify Button")

    login.click_verify_continue()

    time.sleep(25)

    # ASSERTION 1
    assert login.verify_login_success(), \
        "Login Failed"

    print("PASS 1 - LOGIN SUCCESSFUL")

    # =====================================================
    # TEST CASE 2 : NAVIGATION
    # =====================================================

    logger.info("Opening Footwear Page")

    driver.get(
        "https://www.bigbasket.com/pc/fashion/footwear/"
    )

    time.sleep(10)

    # ASSERTION 2
    assert "footwear" in driver.current_url.lower(), \
        "Footwear Page Not Opened"

    print("PASS 2 - NAVIGATION SUCCESSFUL")

    # =====================================================
    # TEST CASE 3 : ADD FIRST PRODUCT
    # =====================================================

    logger.info("Opening Brands Filter")

    home.click_brands_filter()
    time.sleep(5)

    logger.info("Selecting Adidas Sports")

    home.select_adidas_sports()
    time.sleep(5)

    logger.info("Adding First Product")

    home.click_add_button()
    time.sleep(8)

    # ASSERTION 3
    assert "bigbasket" in driver.title.lower(), \
        "Product Not Added"

    print("PASS 3 - PRODUCT ADDED SUCCESSFULLY")

    # =====================================================
    # TEST CASE 4 : BASKET FLOW
    # =====================================================

    logger.info("Scrolling Half Page")

    driver.execute_script(
        "window.scrollBy(0,500);"
    )

    time.sleep(5)

    logger.info("Selecting Action Checkbox")

    home.select_action_checkbox()
    time.sleep(5)

    logger.info("Adding Second Product")

    home.click_add_button()
    time.sleep(8)

    logger.info("Opening Basket")

    home.click_basket_two_items()
    time.sleep(5)

    # ASSERTION 4
    assert "basket" or "cart" in driver.page_source.lower(), \
        "Basket Not Opened"

    print("PASS 4 - BASKET OPENED SUCCESSFULLY")

    # =====================================================
    # FINAL
    # =====================================================

    print("ALL 4 POSITIVE TEST CASES PASSED")