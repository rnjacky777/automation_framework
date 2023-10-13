import configparser
from selenium.webdriver.chrome.options import Options
import core_framework.core_framework as core_framework
from selenium import webdriver
import pytest

@pytest.fixture(autouse=True,scope="function")
def init_driver():
    print("Start testing")
    config = configparser.ConfigParser()
    config.read('./core_framework/util/config.ini')
    default_setting = config['default_setting']
    options = Options()
    options.chrome_executable_path = default_setting
    driver = webdriver.Chrome(options=options)
    core_framework.CoreDriver.driver= driver
    yield
    core_framework.CoreDriver.driver.quit()