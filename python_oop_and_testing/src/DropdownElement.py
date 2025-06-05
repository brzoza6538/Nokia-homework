from .GlobalVariables import *

class DropdownElement:
    def __init__(self, driver):
        self.driver = driver

    def open_dropdown(self):
        button = WebDriverWait(self.driver, wait_until_time).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        button.click()

    def select_main_theme(self):
        option = WebDriverWait(self.driver, wait_until_time).until(EC.visibility_of_element_located((By.XPATH, option_xpath)))
        time.sleep(animation_wait_time)
        option.click()

