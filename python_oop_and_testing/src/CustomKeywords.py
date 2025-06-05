
from .GlobalVariables import *
from .DropdownElement import *
from .ContextMenu import *

driver_instance = None

class CustomKeywords:

    @keyword("Set Driver From SeleniumLibrary")
    def set_driver_from_seleniumlibrary(self):
        global driver_instance
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        driver_instance = seleniumlib.driver

    @keyword("Select Demo Frame")
    def select_demo_frame(self):
        WebDriverWait(driver_instance, wait_until_time).until(
            EC.visibility_of_element_located((By.XPATH, demo_frame_xpath))
        )
        iframe = driver_instance.find_element(By.XPATH, demo_frame_xpath)
        driver_instance.switch_to.frame(iframe)

    @keyword("Unselect Demo Frame")
    def unselect_demo_frame(self):
        driver_instance.switch_to.default_content()

    @keyword("Wait For Context Menu To Load")
    def wait_for_context_menu_to_load(self):
        WebDriverWait(driver_instance, wait_until_time).until(
            EC.visibility_of_element_located((By.XPATH, context_target_xpath))
        )

    @keyword("Change Theme Using Python Keyword")
    def change_theme_using_python_keyword(self):
        dropdown = DropdownElement(driver_instance)
        self.select_demo_frame()
        self.wait_for_context_menu_to_load()
        self.unselect_demo_frame()
        dropdown.open_dropdown()
        dropdown.select_main_theme()

    @keyword("Interact With Context Menu")
    def interact_with_context_menu(self):
        context_menu = ContextMenu(driver_instance)
        self.select_demo_frame()
        self.wait_for_context_menu_to_load()
        context_menu.open_context_menu()
        context_menu.click_style()
        context_menu.click_underline()
        self.unselect_demo_frame()
