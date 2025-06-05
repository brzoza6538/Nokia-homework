from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DropdownElement:
    def __init__(self, driver):
        self.driver = driver
        self.button_xpath = "//button[@aria-label='Change theme']"
        self.option_xpath = "//button[.//div[text()='Main']]"

    def open_dropdown(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_xpath)))
        button.click()

    def select_main_theme(self):
        option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.option_xpath)))
        time.sleep(1)
        option.click()

