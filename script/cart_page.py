import json
from selenium.webdriver.common.by import By
from core_framework.core_framework import CoreDriver


class CartPageScript(CoreDriver):

    def __init__(self) -> None:
        super().__init__()
    def select_all_checkbox(self):
        xpath = "((//div[contains(@class,'stardust-checkbox__box')]))[1]"
        name = "select_all_checkbox"
        return self.get_element(name,xpath)



