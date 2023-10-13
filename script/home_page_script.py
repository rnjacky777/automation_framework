import json,time
from selenium.webdriver.common.by import By
from core_framework.core_framework import CoreDriver


class HomePageScript(CoreDriver):

    def __init__(self) -> None:
        super().__init__()

    def go_to_homepage(self):
        self.driver.get("https://shopee.tw/")
    
    def check_pop_up_banner(self):
        name = "pop_up_banner"
        xpath = "//shopee-banner-popup-stateful"
        try:
            self.get_element(name,xpath)
            return True
        except:
            return False

    def close_pop_up_banner(self):
        try:
            if self.check_pop_up_banner():
                self.driver.execute_script('document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector(".shopee-popup__close-btn").click()')
                self.log.info('close pop_up_banner')
        except:
            self.log.info('Does not find pop_up_banner')