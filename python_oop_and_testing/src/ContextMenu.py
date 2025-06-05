from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ContextMenu:
    def __init__(self, driver):
        self.driver = driver
        self.style_xpath = "//li[.//span[text()='Style']]"
        self.underline_xpath = "//li[.//span[text()='Underline']]"
        self.contex_target_xpath = "//div[contains(@class,'target')]"

    def open_context_menu(self):
        target = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.contex_target_xpath)))
        ActionChains(self.driver).context_click(target).perform()

    def click_style(self):
        style = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.style_xpath)))
        time.sleep(1)
        ActionChains(self.driver).move_to_element(style).perform()

    def click_underline(self):
        underline = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.underline_xpath)))
        time.sleep(1)
        underline.click()
