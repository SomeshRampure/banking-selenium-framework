#  browser setup and teardown

import os
from datetime import datetime
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    yield driver
    driver.quit()

def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{timestamp}.html"

    config._metadata = {
        "Project": "Tutorialspoint Student Form",
        "Tester": "Somesh",
        "Browser": "Chrome",
        "Environment": "Local",
    }