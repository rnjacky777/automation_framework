from appium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.data = {}

    @allure.step('click element')
    def click_element(self, name: str):
        xpath = self.data[name]
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            f"Can't find element '{name}' using xpath: {xpath}"
        )
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath)),
            f"Can't find element '{name}' using xpath: {xpath}")
        element.click()

    @allure.step('send key')
    def send_key(self, name: str, text: str):
        xpath = self.data[name]
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            f"Can't find element '{name}' using xpath: {xpath}"
        )
        element.send_keys(text)

    @allure.step('scroll page')
    def scroll_page(self, pixels: int):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    @allure.step('take screenshot')
    def element_screenshot(self, screenshot_name: str = "screenshot.png"):
        self.driver.save_screenshot(screenshot_name)

    @allure.step('wait for element disappear')
    def wait_element_disappear(self, name: str):
        xpath = self.data[name]
        WebDriverWait(self.driver, 2).until(
            EC.invisibility_of_element_located((By.XPATH, xpath))
        )

    @allure.step('wait for video playing')
    def wait_video_playing(self, timeout: int = 30):
        video_check_js = """
        var v = document.querySelector('video');
        return v && v.readyState === 4 && v.currentTime > 0.5;
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script(video_check_js),
                "Video did not start playing within timeout"
            )
            return True
        except Exception as e:
            print(f"Video play check failed: {e}")
            return False

    @allure.step('waiting element')
    def wait_element(self, name: str):
        xpath = self.data[name]
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)),
            f"Can't find element '{name}' using xpath: {xpath}"
        )

    @allure.step('Wait for URL to change to: {keyword}')
    def wait_url_contains(self, keyword: str, timeout: int = 15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(keyword)
            )
        except Exception:
            actual_url = self.driver.current_url
            raise Exception(
                f"Timeout: URL did not contain '{keyword}' within {timeout}s. Actual URL: {actual_url}")
