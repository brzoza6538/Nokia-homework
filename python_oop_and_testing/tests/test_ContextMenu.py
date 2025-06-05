import pytest
from src.ContextMenu import ContextMenu
from src.GlobalVariables import *

def test_open_context_menu(mocker):
    mock_driver = mocker.Mock()
    mock_target = mocker.Mock()

    mock_wait = mocker.Mock()
    mock_wait.until.return_value = mock_target
    mocker.patch('src.ContextMenu.WebDriverWait', return_value=mock_wait)

    mock_action_chain = mocker.Mock()
    mock_action_chain.context_click.return_value = mock_action_chain
    mock_action_chain.perform.return_value = None
    mocker.patch('src.ContextMenu.ActionChains', return_value=mock_action_chain)

    menu = ContextMenu(mock_driver)
    menu.open_context_menu()

    mock_wait.until.assert_called_once()
    mock_action_chain.context_click.assert_called_once_with(mock_target)
    mock_action_chain.perform.assert_called_once()

    called_arg = mock_wait.until.call_args.args[0]
    expected = EC.visibility_of_element_located((By.XPATH, context_target_xpath))
    assert type(called_arg) == type(expected)


def test_click_style(mocker):
    mock_driver = mocker.Mock()
    mock_style = mocker.Mock()

    mock_wait = mocker.Mock()
    mock_wait.until.return_value = mock_style
    mocker.patch('src.ContextMenu.WebDriverWait', return_value=mock_wait)

    mock_action_chain = mocker.Mock()
    mock_action_chain.move_to_element.return_value = mock_action_chain
    mock_action_chain.perform.return_value = None
    mocker.patch('src.ContextMenu.ActionChains', return_value=mock_action_chain)

    mocker.patch('src.ContextMenu.time.sleep')

    menu = ContextMenu(mock_driver)
    menu.click_style()

    mock_wait.until.assert_called_once()
    mock_action_chain.move_to_element.assert_called_once_with(mock_style)
    mock_action_chain.perform.assert_called_once()

    called_arg = mock_wait.until.call_args.args[0]
    expected = EC.visibility_of_element_located((By.XPATH, style_xpath))
    assert type(called_arg) == type(expected)

def test_click_underline(mocker):
    mock_driver = mocker.Mock()
    mock_underline = mocker.Mock()

    mock_wait = mocker.Mock()
    mock_wait.until.return_value = mock_underline
    mocker.patch('src.ContextMenu.WebDriverWait', return_value=mock_wait)

    mocker.patch('src.ContextMenu.time.sleep')

    menu = ContextMenu(mock_driver)
    menu.click_underline()

    mock_wait.until.assert_called_once()
    mock_underline.click.assert_called_once()

    called_arg = mock_wait.until.call_args.args[0]
    expected = EC.visibility_of_element_located((By.XPATH, underline_xpath))
    assert type(called_arg) == type(expected)
