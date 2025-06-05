from unittest.mock import MagicMock
import pytest
from src.DropdownElement import DropdownElement


def test_select_main_theme(mocker):
    mock_driver = MagicMock()
    mock_demo_frame = MagicMock()
    mock_button = MagicMock()
    mock_option = MagicMock()

    # Metody potrzebne przez EC.element_to_be_clickable
    mock_button.is_displayed = MagicMock(return_value=True)
    mock_button.is_enabled = MagicMock(return_value=True)
    mock_button.click = MagicMock()

    mock_option.is_displayed = MagicMock(return_value=True)
    mock_option.is_enabled = MagicMock(return_value=True)
    mock_option.click = MagicMock()

    # Mockowanie find_element na driverze
    def find_element_side_effect(by, value):
        if value == "//iframe[contains(@class,'demo-module--demoFrame')]":
            return mock_demo_frame
        elif value == "//button[@aria-label='Change theme']":
            return mock_button
        elif value == "//button[.//div[text()='Main']]":
            return mock_option
        else:
            return MagicMock()

    mock_driver.find_element.side_effect = find_element_side_effect

    # Mockowanie WebDriverWait.until i jego side_effect
    def wait_until_side_effect(predicate):
        locator = getattr(predicate, 'locator', None)
        if locator:
            by, xpath = locator
            if xpath == "//iframe[contains(@class,'demo-module--demoFrame')]":
                return mock_demo_frame
            elif xpath == "//div[contains(@class,'target')]":
                return MagicMock()  # Dla wait_for_context_menu_to_load()
            elif xpath == "//button[@aria-label='Change theme']":
                return mock_button
            elif xpath == "//button[.//div[text()='Main']]":
                return mock_option

        try:
            # Jeżeli predicate jest funkcją, wywołujemy ją z mock_driver
            return predicate(mock_driver)
        except Exception:
            return MagicMock()

    mock_wait = MagicMock()
    mock_wait.until.side_effect = wait_until_side_effect

    # Podmieniamy WebDriverWait w DropdownElement na nasz mock
    mocker.patch('src.DropdownElement.WebDriverWait', return_value=mock_wait)

    dropdown = DropdownElement(mock_driver)

    dropdown.open_dropdown()
    dropdown.select_main_theme()

    # Sprawdź, czy kliknięto przycisk i opcję
    mock_button.click.assert_called_once()
    mock_option.click.assert_called_once()
