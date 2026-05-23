import os
import pytest
import allure

from datetime import datetime
from selenium import webdriver


# =====================================================
# DRIVER FIXTURE
# =====================================================

@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# =====================================================
# SCREENSHOT ON FAILURE
# =====================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    # Take screenshot only if test failed
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:

            # Create screenshots folder
            screenshot_dir = "reports/screenshots"

            os.makedirs(
                screenshot_dir,
                exist_ok=True
            )

            # Screenshot name
            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            screenshot_name = (
                f"{item.name}_{timestamp}.png"
            )

            screenshot_path = os.path.join(
                screenshot_dir,
                screenshot_name
            )

            # Save screenshot
            driver.save_screenshot(
                screenshot_path
            )

            # Attach screenshot to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )