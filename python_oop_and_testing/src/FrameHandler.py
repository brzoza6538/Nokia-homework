from .GlobalVariables import *

class FrameHandler:
    def __init__(self, driver):
        self.driver = driver

    def select_demo_frame(self):
        WebDriverWait(self.driver, wait_until_time).until(
            EC.visibility_of_element_located((By.XPATH, demo_frame_xpath))
        )
        iframe = self.driver.find_element(By.XPATH, demo_frame_xpath)
        self.driver.switch_to.frame(iframe)

    def unselect_demo_frame(self):
        self.driver.switch_to.default_content()

    def wait_for_context_menu_to_load(self):
        WebDriverWait(self.driver, wait_until_time).until(
            EC.visibility_of_element_located((By.XPATH, context_target_xpath))
        )

