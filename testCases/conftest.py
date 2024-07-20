from datetime import datetime

import pytest
from selenium import webdriver
import os

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = (os.path.dirname(os.getcwd()) + "\\TutorialNinja\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html")
