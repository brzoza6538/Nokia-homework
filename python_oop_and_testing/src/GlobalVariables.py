import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

demo_frame_xpath = "//iframe[contains(@class,'demo-module--demoFrame')]"
context_target_xpath = "//div[contains(@class,'target')]"

style_xpath = "//li[.//span[text()='Style']]"
underline_xpath = "//li[.//span[text()='Underline']]"

button_xpath = "//button[@aria-label='Change theme']"
option_xpath = "//button[.//div[text()='Main']]"

wait_until_time = 10
animation_wait_time = 1