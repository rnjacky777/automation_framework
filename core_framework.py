import json
import time
import selenium
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import configparser

#==============================================================
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#==============================================================

def init_driver():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    default_setting = config['default_setting']
    options = Options()
    options.chrome_executable_path = default_setting
    driver=webdriver.Chrome(options=options)
    return driver
class CoreDriver():
    driver:WebDriver
    delay = 10

    def __init__(self,driver=None) -> None:
        if driver is not None:
            self.driver = driver
        self.log = logging.getLogger(__name__)

    @staticmethod
    def driver_init(cls):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        default_setting = config['default_setting']
        options = Options()
        options.chrome_executable_path = default_setting
        driver=webdriver.Chrome(options=options)
        cls(driver)

    def get_element(self,xpath):
        self.log.info(f"Get xpath: {xpath}")
        WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.find_element(by=By.XPATH,value=xpath)

    def load_cookie(self):
        with open("token.json") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
    
    def page_refresh(self):
        self.driver.refresh()

    def wait_page_loading(self):
        WebDriverWait(self.driver, self.delay).until_not(EC.presence_of_element_located((By.XPATH, "//*[@class='qZrMO2']")))
        



