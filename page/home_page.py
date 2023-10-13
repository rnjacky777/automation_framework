import json,time
from selenium.webdriver.common.by import By
from core_framework.core_framework import CoreDriver


class HomePage(CoreDriver):

    def __init__(self) -> None:
        super().__init__()
        # with open('data.json') as f:
        #     data = json.load(f)

    def search_button(self):
        xpath = "//button[contains(@class ,'btn-solid-primary')]"
        name = "search_button"
        # xpath = "//button[contains(@class ,'btn-solid-primar789y')]"
        return self.get_element(name,xpath)

    def cart_icon(self):
        xpath = "//div[@id='cart_drawer_target_id']"
        name = "cart_icon"
        return self.get_element(name,xpath)