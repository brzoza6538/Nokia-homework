from unittest.mock import MagicMock
import pytest
from src.DropdownElement import DropdownElement
from src.GlobalVariables import *

def test_select_main_theme(mocker):
    mock_driver = MagicMock()
    mock_demo_frame = MagicMock()
    mock_button = MagicMock()
    mock_option = MagicMock()

    # Konfiguracja mocków dla kliknięcia
    mock_button.is_displayed.return_value = True
    mock_button.is_enabled.return_value = True
    mock_button.click = MagicMock()

    mock_option.is_displayed.return_value = True
    mock_option.is_enabled.return_value = True
    mock_option.click = MagicMock()

    def find_element_side_effect(by, value):
        if value == demo_frame_xpath:
            return mock_demo_frame
        elif value == button_xpath:
            return mock_button
        elif value == option_xpath:
            return mock_option
        else:
            return MagicMock()

    mock_driver.find_element.side_effect = find_element_side_effect

    def wait_until_side_effect(predicate):
        locator = getattr(predicate, 'locator', None)
        if locator:
            by, xpath = locator
            if xpath == demo_frame_xpath:
                return mock_demo_frame
            elif xpath == context_target_xpath:
                return MagicMock()  # Dla innych czekających keywordów
            elif xpath == button_xpath:
                return mock_button
            elif xpath == option_xpath:
                return mock_option

        return predicate(mock_driver)

    mock_wait = MagicMock()
    mock_wait.until.side_effect = wait_until_side_effect

    mocker.patch('src.DropdownElement.WebDriverWait', return_value=mock_wait)

    dropdown = DropdownElement(mock_driver)

    dropdown.open_dropdown()
    dropdown.select_main_theme()

    mock_button.click.assert_called_once()
    mock_option.click.assert_called_once()
