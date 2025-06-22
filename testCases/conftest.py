import tempfile

import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
import os
from datetime import datetime
from utilities.readProperties import ReadConfig


# Fixture to launch browser
# @pytest.fixture()
# def setup(browser):
#     if browser == 'edge':
#         options = webdriver.EdgeOptions()
#         options.add_experimental_option("detach", True)
#         options.add_argument("--headless")
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

@pytest.fixture()
def setup(browser_platform):
  baseenv = ReadConfig.getEnvironment()
  browser,platform = browser_platform
  if baseenv == "remote":
      options = {
          "chrome": webdriver.ChromeOptions,
          "edge": webdriver.EdgeOptions,
          "firefox": webdriver.FirefoxOptions
      }
      if browser not in options:
          raise ValueError(f"Unsupported browser: {browser}")
      platform_mapping = {"windows": "WIN10", "mac": "MAC", "linux": "LINUX"}
      platform_name = platform_mapping.get(platform)
      if not platform_name:
          raise ValueError(f"Unsupported platform: {platform}")
      opt = options[browser]()
      opt.add_experimental_option("detach", True) if browser in ["chrome", "edge"] else None
      # opt.add_argument("--headless")
      opt.platform_name = platform_name
      driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=opt)
  elif baseenv == "local":
      if browser == 'edge':
          options = webdriver.EdgeOptions()
          options.add_experimental_option("detach", True)
          driver = webdriver.Edge(options=options)
          print("Launching Edge browser.........")
      elif browser == 'firefox':
          options = webdriver.FirefoxOptions()
          driver = webdriver.Firefox(options=options)
          print("Launching firefox browser.........")
      else:
          options = webdriver.ChromeOptions()
          options.add_experimental_option("detach", True)
          # ✅ Fix: Provide isolated user-data-dir
          temp_dir = tempfile.mkdtemp()
          options.add_argument(f"--user-data-dir={temp_dir}")

          # ✅ Recommended for CI: Run headless & safe
          # options.add_argument("--headless=new")
          options.add_argument("--window-size=1920,1080")
          options.add_argument("--no-sandbox")
          options.add_argument("--disable-dev-shm-usage")
          driver = webdriver.Chrome(options=options)
          print("Launching chrome browser.........")
  yield driver
  driver.quit()

# CLI argument hook
# def pytest_addoption(parser):
#     parser.addoption("--browser")

def pytest_addoption(parser):
  parser.addoption("--browser", default="chrome", choices=["chrome", "edge", "firefox"], help = "Browser to test")
  parser.addoption("--os", default="linux", choices=["windows", "mac", "linux"], help = "Operating system to test")

# Fixture to fetch browser option
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

@pytest.fixture()
def browser_platform(request):
  browser = request.config.getoption("--browser")
  platform = request.config.getoption("--os")
  return browser,platform

# Hook 1: Configure report path and add custom metadata
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    # config.option.htmlpath = (
    #         os.path.abspath(os.getcwd()) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    # )
    config.stash[metadata_key]['Project Name'] = 'TutorialNinja'
    config.stash[metadata_key]['Module Name'] = 'CustRegistration'
    config.stash[metadata_key]['Tester Name'] = 'KMR'

# Hook 2: Remove default metadata
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python", None)
    metadata.pop("Plugins", None)

# Hook 3: Capture screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_dir = os.path.abspath(os.getcwd()) + "/screenshots/"
            os.makedirs(screenshot_dir, exist_ok=True)
            driver.save_screenshot(f"{screenshot_dir}{item.name}.png")
            allure.attach(
                driver.get_screenshot_as_png(), name=f"{item.name}", attachment_type=AttachmentType.PNG
            )

