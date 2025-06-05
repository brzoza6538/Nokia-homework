from unittest.mock import MagicMock
import pytest
from src.ContextMenu import ContextMenu
from src.GlobalVariables import *

def test_context_menu_interaction(mocker):
    mock_driver = MagicMock()
    mock_target = MagicMock()
    mock_style = MagicMock()
    mock_underline = MagicMock()

    def wait_until_side_effect(predicate):
        locator = getattr(predicate, 'locator', None)
        if locator:
            by, xpath = locator
            if xpath == context_target_xpath:
                return mock_target
            elif xpath == style_xpath:
                return mock_style
            elif xpath == underline_xpath:
                return mock_underline
        return predicate(mock_driver)

    mock_wait = MagicMock()
    mock_wait.until.side_effect = wait_until_side_effect

    mocker.patch('src.ContextMenu.WebDriverWait', return_value=mock_wait)

    instances = []

    def action_chains_side_effect(driver):
        instance = MagicMock()
        instance.context_click.return_value = instance
        instance.move_to_element.return_value = instance
        instance.perform.return_value = instance
        instances.append(instance)
        return instance

    mocker.patch('src.ContextMenu.ActionChains', side_effect=action_chains_side_effect)

    menu = ContextMenu(mock_driver)
    menu.open_context_menu()
    menu.click_style()
    menu.click_underline()

    assert len(instances) >= 2
    for instance in instances:
        instance.perform.assert_called_once()
