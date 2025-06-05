from unittest.mock import MagicMock
import pytest
from src.ContextMenu import ContextMenu
from selenium.webdriver.common.by import By


def test_context_menu_interaction(mocker):
    mock_driver = MagicMock()
    mock_target = MagicMock()
    mock_style = MagicMock()
    mock_underline = MagicMock()

    def wait_until_side_effect(condition):
        xpath = condition.locator[1]
        if xpath == "//div[contains(@class,'target')]":
            return mock_target
        elif xpath == "//li[.//span[text()='Style']]":
            return mock_style
        elif xpath == "//li[.//span[text()='Underline']]":
            return mock_underline
        else:
            return MagicMock()

    mock_wait = MagicMock()
    mock_wait.until.side_effect = [mock_target, mock_style, mock_underline]

    # Podmieniamy WebDriverWait w ContextMenu na mock z naszym wait
    mocker.patch('src.ContextMenu.WebDriverWait', return_value=mock_wait)

    # Mockujemy ActionChains, by zwracał chainable mocki
    instances = []

    def action_chains_side_effect(driver):
        instance = MagicMock()
        instance.context_click.return_value = instance
        instance.move_to_element.return_value = instance
        instance.perform.return_value = instance
        instances.append(instance)
        return instance

    mock_action_chains = mocker.patch('src.ContextMenu.ActionChains', side_effect=action_chains_side_effect)

    menu = ContextMenu(mock_driver)
    menu.open_context_menu()
    menu.click_style()
    menu.click_underline()

    # Sprawdź, czy ActionChains zostały wywołane i perform wywołane na każdym etapie
    assert len(instances) >= 2
    for instance in instances:
        instance.perform.assert_called_once()
