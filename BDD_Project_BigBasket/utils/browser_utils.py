from selenium.webdriver.common.by import By


class BrowserUtils:

    # ================= WINDOW HANDLING =================

    @staticmethod
    def close_extra_windows(driver, main_window):

        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                driver.close()

        driver.switch_to.window(main_window)

    # ================= POPUP HANDLING =================

    @staticmethod
    def close_popups(driver):

        try:
            popups = driver.find_elements(
                By.XPATH,
                "//button[contains(.,'Accept') or contains(.,'Close') or contains(.,'Got it') or contains(.,'OK')]"
            )

            for p in popups:
                try:
                    p.click()
                except:
                    driver.execute_script("arguments[0].click();", p)

        except:
            pass