import pytest
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="module")
def shared_driver():
    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    appium_server_url = config['appium_server_url']
    capabilities = config['capabilities']
    
    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)
    
    yield driver 
    driver.quit()