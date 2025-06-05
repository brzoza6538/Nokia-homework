from .GlobalVariables import *
from .DropdownElement import DropdownElement
from .ContextMenu import ContextMenu
from .FrameHandler import FrameHandler

class CustomKeywords:
    def __init__(self):
        self.driver = None
        self.frame_handler = None

    @keyword("Set Driver From SeleniumLibrary")
    def set_driver_from_seleniumlibrary(self):
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        self.driver = seleniumlib.driver
        self.frame_handler = FrameHandler(self.driver)

    @keyword("Change Theme Using Python Keyword")
    def change_theme_using_python_keyword(self):
        dropdown = DropdownElement(self.driver)
        self.frame_handler.select_demo_frame()
        self.frame_handler.wait_for_context_menu_to_load()
        self.frame_handler.unselect_demo_frame()
        dropdown.open_dropdown()
        dropdown.select_main_theme()

    @keyword("Interact With Context Menu")
    def interact_with_context_menu(self):
        context_menu = ContextMenu(self.driver)
        self.frame_handler.select_demo_frame()
        self.frame_handler.wait_for_context_menu_to_load()
        context_menu.open_context_menu()
        context_menu.click_style()
        context_menu.click_underline()
        self.frame_handler.unselect_demo_frame()
