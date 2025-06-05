from DropdownElement import DropdownElement
from ContextMenu import ContextMenu
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver_instance = None


demo_frame_xpath = "//iframe[contains(@class,'demo-module--demoFrame')]"
contex_target_xpath = "//div[contains(@class,'target')]"

def select_demo_frame(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, demo_frame_xpath)))
    iframe = driver.find_element(By.XPATH, demo_frame_xpath)
    driver.switch_to.frame(iframe)
def unselect_demo_frame(driver):
    driver.switch_to.default_content()

def wait_for_context_menu_to_load(driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, context_target_xpath)))


class CustomKeywords:

    @keyword("Set Driver From SeleniumLibrary")
    def set_driver_from_seleniumlibrary(self):
        global driver_instance
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        driver_instance = seleniumlib.driver

    @keyword("Change Theme Using Python Keyword")
    def change_theme_using_python_keyword(self):
        dropdown = DropdownElement(driver_instance)
        select_demo_frame(dropdown.driver)
        wait_for_context_menu_to_load(dropdown.driver)
        unselect_demo_frame(dropdown.driver)
        dropdown.open_dropdown()
        dropdown.select_main_theme()

    @keyword("Interact With Context Menu")
    def interact_with_context_menu(self):
        context_menu = ContextMenu(driver_instance)
        select_demo_frame(context_menu.driver)
        wait_for_context_menu_to_load(context_menu.driver)
        context_menu.open_context_menu()
        context_menu.click_style()
        context_menu.click_underline()
        unselect_demo_frame(context_menu.driver)
