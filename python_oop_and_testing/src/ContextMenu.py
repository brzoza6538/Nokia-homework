
from .GlobalVariables import *

class ContextMenu:
    def __init__(self, driver):
        self.driver = driver

    def open_context_menu(self):
        target = WebDriverWait(self.driver, wait_until_time).until(EC.visibility_of_element_located((By.XPATH, context_target_xpath)))
        ActionChains(self.driver).context_click(target).perform()

    def click_style(self):
        style = WebDriverWait(self.driver, wait_until_time).until(EC.visibility_of_element_located((By.XPATH, style_xpath)))
        time.sleep(animation_wait_time)
        ActionChains(self.driver).move_to_element(style).perform()

    def click_underline(self):
        underline = WebDriverWait(self.driver, wait_until_time).until(EC.visibility_of_element_located((By.XPATH, underline_xpath)))
        time.sleep(animation_wait_time)
        underline.click()
