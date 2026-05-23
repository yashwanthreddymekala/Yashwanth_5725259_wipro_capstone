import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import allure


def before_all(context):

    options = Options()

    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        options=options
    )

    context.driver.implicitly_wait(10)


# =====================================================
# FAILED STEP SCREENSHOT
# =====================================================

def after_step(context, step):

    if step.status == "failed":

        screenshot_dir = "reports/screenshots"

        os.makedirs(
            screenshot_dir,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot_name = (
            f"{step.name}_{timestamp}.png"
        )

        screenshot_path = os.path.join(
            screenshot_dir,
            screenshot_name
        )

        # ==========================================
        # SAVE SCREENSHOT
        # ==========================================

        context.driver.save_screenshot(
            screenshot_path
        )

        # ==========================================
        # ATTACH SCREENSHOT TO ALLURE
        # ==========================================

        with open(
            screenshot_path,
            "rb"
        ) as file:

            allure.attach(
                file.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        # ==========================================
        # ATTACH LOG FILE
        # ==========================================

        log_path = "logs/automation.log"

        if os.path.exists(log_path):

            with open(log_path, "r") as log_file:

                allure.attach(
                    log_file.read(),
                    name="Failure Logs",
                    attachment_type=allure.attachment_type.TEXT
                )


def after_all(context):

    if hasattr(context, "driver"):

        context.driver.quit()