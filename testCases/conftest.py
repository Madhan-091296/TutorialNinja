# import allure
# import pytest
# from allure_commons.types import AttachmentType
# from pytest_metadata.plugin import metadata_key
# from selenium import webdriver
# import os
# from datetime import datetime
#
#
# # Fixture to launch browser
# @pytest.fixture()
# def setup(browser):
#     if browser == 'edge':
#         options = webdriver.EdgeOptions()
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Edge(options=options)
#         print("Launching Edge browser.........")
#     elif browser == 'firefox':
#         options = webdriver.FirefoxOptions()
#         driver = webdriver.Firefox(options=options)
#         print("Launching Firefox browser.........")
#     else:
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=options)
#         print("Launching Chrome browser.........")
#     yield driver
#     driver.quit()
#
# # CLI argument hook
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# # Fixture to fetch browser option
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# # Hook 1: Configure report path and add custom metadata
# @pytest.hookimpl(optionalhook=True)
# def pytest_configure(config):
#     config.option.htmlpath = (
#             os.path.abspath(os.getcwd()) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
#     )
#     config.stash[metadata_key]['Project Name'] = 'TutorialNinja'
#     config.stash[metadata_key]['Module Name'] = 'CustRegistration'
#     config.stash[metadata_key]['Tester Name'] = 'KMR'
#
# # Hook 2: Remove default metadata
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("Python", None)
#     metadata.pop("Plugins", None)
#
# # Hook 3: Capture screenshot on test failure
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("setup")
#         if driver:
#             screenshot_dir = os.path.abspath(os.getcwd()) + "/screenshots/"
#             os.makedirs(screenshot_dir, exist_ok=True)
#             driver.save_screenshot(f"{screenshot_dir}{item.name}.png")
#             allure.attach(
#                 driver.get_screenshot_as_png(), name=f"{item.name}", attachment_type=AttachmentType.PNG
#             )
#
#
import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
from datetime import datetime

# Fixture to launch browser
@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        print("Launching Firefox browser.........")
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        print("Launching Chrome browser.........")
    yield driver
    driver.quit()

# CLI argument hook
def pytest_addoption(parser):
    parser.addoption("--browser")

# Fixture to fetch browser option
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Hook 1: Configure report path and add custom metadata
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.htmlpath = (
        os.path.abspath(os.getcwd()) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )
    config.stash[metadata_key]['Project Name'] = 'TutorialNinja'
    config.stash[metadata_key]['Module Name'] = 'CustRegistration'
    config.stash[metadata_key]['Tester Name'] = 'KMR'

# Hook 2: Remove default metadata
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python", None)
    metadata.pop("Plugins", None)

# # Hook 3: Capture screenshot on test failure
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get("setup", None)
#         if driver:
#             try:
#                 # This will fail if browser is already closed
#                 screenshot_dir = os.path.abspath(os.getcwd()) + "/screenshots/"
#                 os.makedirs(screenshot_dir, exist_ok=True)
#                 path = f"{screenshot_dir}{item.name}.png"
#                 driver.save_screenshot(path)
#                 allure.attach(
#                     driver.get_screenshot_as_png(),
#                     name=item.name,
#                     attachment_type=AttachmentType.PNG
#                 )
#             except Exception as e:
#                 # Log but ignore errors like NoSuchWindowException
#                 print(f"Error while capturing screenshot: {e}")
