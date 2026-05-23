import time

from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    SHOP_CATEGORY = (
        By.XPATH,
        "//button[contains(.,'Shop by')]"
    )

    FASHION_CATEGORY = (
        By.XPATH,
        "//a[@href='/cl/fashion/?nc=nb']"
    )

    FOOTWEAR_CATEGORY = (
        By.XPATH,
        "//a[@href='/pc/fashion/footwear/?nc=ct-fa']"
    )

    # Brands Filter
    BRANDS_FILTER = (
        By.XPATH,
        "//span[contains(text(),'Brands')]"
    )

    # Adidas Sports Checkbox
    ADIDAS_SPORTS = (
        By.XPATH,
        "//label[@for='i-AdidasSports']"
    )

    # Add To Cart Button
    ADD_BUTTON = (
        By.XPATH,
        "(//button[contains(text(),'Add')])[1]"
    )
    # Basket Button
    BASKET_BUTTON = (
        By.XPATH,
        "//span[contains(text(),'1 Item')]"
    )
    # Action Checkbox
    ACTION_CHECKBOX = (
        By.XPATH,
        "//*[contains(text(),'Action')]"
    )

    # Basket With 2 Items
    BASKET_TWO_ITEMS = (
        By.XPATH,
        "//span[contains(text(),'2 Items')]"
    )

    # Increment Button
    INCREMENT_BUTTON = (
        By.XPATH,
        "//button[@id='increment']"
    )

    # Proceed To Checkout
    CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Proceed to Checkout')]"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def click_shop_by_category(self):

        element = self.driver.find_element(*self.SHOP_CATEGORY)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def click_fashion(self):

        element = self.driver.find_element(*self.FASHION_CATEGORY)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def click_footwear(self):

        element = self.driver.find_element(*self.FOOTWEAR_CATEGORY)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def click_brands_filter(self):

        element = self.driver.find_element(*self.BRANDS_FILTER)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def select_adidas_sports(self):

        element = self.driver.find_element(*self.ADIDAS_SPORTS)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def click_add_button(self):

        element = self.driver.find_element(*self.ADD_BUTTON)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Open Basket
    def click_basket(self):
        element = self.driver.find_element(*self.BASKET_BUTTON)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Select Action Checkbox
    def select_action_checkbox(self):
        # Scroll down slowly
        self.driver.execute_script(
            "window.scrollBy(0,1000);"
        )

        time.sleep(5)

        element = self.driver.find_element(
            By.XPATH,
            "//label[contains(.,'Action')]"
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Open Basket
    def click_basket_two_items(self):

        time.sleep(5)

        basket_xpath_list = [

            "//span[contains(text(),'2 Items')]",

            "//span[contains(text(),'2 items')]",

            "//span[contains(text(),'Item')]",

            "//span[contains(@class,'Basket')]",

            "//span[contains(@class,'basket')]",

            "//div[contains(@class,'basket')]",

            "//a[contains(@href,'basket')]",

            "//button[contains(@class,'basket')]"
        ]

        for xpath in basket_xpath_list:

            elements = self.driver.find_elements(By.XPATH, xpath)

            if len(elements) > 0:

                try:
                    self.driver.execute_script(
                        "arguments[0].click();",
                        elements[0]
                    )

                    return

                except:
                    pass

        raise Exception("Basket button not found")

    # Increase Quantity
    def click_increment(self):
        element = self.driver.find_element(*self.INCREMENT_BUTTON)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # Proceed Checkout
    def click_checkout(self):
        element = self.driver.find_element(*self.CHECKOUT_BUTTON)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def get_basket_count(self):

        try:
            basket = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@class,'cart') or contains(@class,'Cart') or contains(@class,'badge')]")
                )
            )

            text = basket.text.strip()

            if text == "" or text is None:
                return "0"

            return text

        except:
            return "0"