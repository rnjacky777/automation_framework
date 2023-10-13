import json
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser


def init_driver():
    config = configparser.ConfigParser()
    config.read('./core_framework/util/config.ini')
    default_setting = config['default_setting']
    options = Options()
    options.chrome_executable_path = default_setting
    driver = webdriver.Chrome(options=options)
    return driver


class CoreDriver():
    driver: WebDriver
    delay = 3

    def __init__(self, driver=None) -> None:
        if driver is not None:
            self.driver = driver
        self.log = logging.getLogger(__name__)

    def get_element(self, name=None, xpath=None) -> WebElement:
        self.log.info(f"Get {name} xpath: {xpath}")
        try:
            element = WebDriverWait(self.driver, self.delay).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            self.log.error(f'Could not find {name}, xpath is {xpath}')
            element = None
        return element

    def load_cookie(self):
        with open("token.json") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def page_refresh(self):
        self.driver.refresh()

    def wait_page_loading(self):
        WebDriverWait(self.driver, self.delay).until_not(
            EC.presence_of_element_located((By.XPATH, "//*[@class='qZrMO2']")))
