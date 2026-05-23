import os
import allure
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils.csv_reader import CSVReader
from utils.logger import LogGenerator
import time


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

    logger.info("Opening BigBasket Website")

    # Open Website
    login.open_bigbasket()
    time.sleep(5)

    logger.info("Clicking Login Button")

    # Click Login
    login.click_login()
    time.sleep(3)

    logger.info("Entering Mobile Number")

    # Enter Mobile Number
    login.enter_mobile_email(test_data["mobile_number"])
    time.sleep(3)

    logger.info("Clicking Continue Button")

    # Click Continue
    login.click_continue()

    logger.info("Waiting For OTP")

    # Enter OTP manually in browser
    time.sleep(20)

    logger.info("Clicking Verify Button")

    # Click Verify
    login.click_verify_continue()
    time.sleep(25)

    logger.info("Clicking Shop By Category")

    # Shop By Category
    home.click_shop_by_category()
    time.sleep(5)

    logger.info("Clicking Fashion")

    # Fashion
    home.click_fashion()
    time.sleep(5)

    logger.info("Clicking Footwear")

    # Footwear
    home.click_footwear()
    time.sleep(10)

    logger.info("Opening Brands Filter")

    # Brands Filter
    home.click_brands_filter()
    time.sleep(5)

    logger.info("Selecting Adidas Sports")

    # Adidas Sports
    home.select_adidas_sports()
    time.sleep(5)

    logger.info("Adding First Product")

    # Add First Product
    home.click_add_button()
    time.sleep(8)

    logger.info("Scrolling Half Page")

    # Scroll Half Page
    driver.execute_script("window.scrollBy(0,500);")
    time.sleep(5)

    logger.info("Selecting Action Checkbox")

    # Select Action Checkbox
    home.select_action_checkbox()
    time.sleep(5)

    logger.info("Adding Second Product")

    # Add Second Product
    home.click_add_button()
    time.sleep(8)

    logger.info("Opening Basket")

    # Open Basket
    home.click_basket_two_items()
    time.sleep(5)

    logger.info("Incrementing Product Quantity")

    # Increment Quantity
    home.click_increment()
    time.sleep(5)

    logger.info("Proceeding To Checkout")

    # Proceed To Checkout
    home.click_checkout()
    time.sleep(10)

    logger.info("Test Case Passed Successfully")

    print("Products Added And Checkout Opened Successfully")


# Automatically Generate And Open Allure Report
def teardown_module():

    os.system("allure generate allure-results -o allure-report --clean")

    os.system("start msedge allure-report\\index.html")