import json,time
from selenium.webdriver.common.by import By
from core_framework import CoreDriver


class HomePageScript(CoreDriver):

    def __init__(self) -> None:
        super().__init__()
        # with open('data.json') as f:
        #     data = json.load(f)

    def search_button(self):
        xpath = "//button[contains(@class ,'btn-solid-primary')]"
        return self.get_element(xpath)

    def go_to_homepage(self):
        self.driver.get("https://shopee.tw/")
    
    def check_pop_up_banner(self):
        xpath = "//shopee-banner-popup-stateful"
        try:
            self.get_element(xpath)
        except:
            return None

    def close_pop_up_banner(self):
        if self.check_pop_up_banner():
            time.sleep(1)
            self.driver.execute_script('document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector(".shopee-popup__close-btn").click()')
    
    def cart_icon(self):
        xpath = "//div[@id='cart_drawer_target_id']"
        return self.get_element(xpath)