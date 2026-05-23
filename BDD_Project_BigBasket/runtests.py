import os

os.system(
    "behave -f allure_behave.formatter:AllureFormatter -o reports/ features"
)