import time
from selenium.webdriver.common.action_chains import ActionChains


class ActionUtils:

    @staticmethod
    def smart_click(driver, element, retries=3):

        for i in range(retries):

            try:
                # 1. scroll into center
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    element
                )

                time.sleep(0.5)

                # 2. normal click attempt
                element.click()
                return True

            except Exception as e:

                print(f"Click attempt {i+1} failed: {e}")

                try:
                    # 3. action chains click
                    ActionChains(driver).move_to_element(element).click().perform()
                    return True

                except:

                    try:
                        # 4. JS click fallback
                        driver.execute_script("arguments[0].click();", element)
                        return True

                    except:
                        time.sleep(1)

        raise Exception("Smart click failed after retries")