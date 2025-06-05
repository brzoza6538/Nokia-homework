import pytest
from src.DropdownElement import DropdownElement
from src.GlobalVariables import *

def test_open_dropdown(mocker):
    mock_driver = mocker.Mock()
    mock_button = mocker.Mock()

    mock_wait = mocker.Mock()
    mock_wait.until.return_value = mock_button
    mocker.patch('src.DropdownElement.WebDriverWait', return_value=mock_wait)

    dropdown = DropdownElement(mock_driver)
    dropdown.open_dropdown()

    mock_wait.until.assert_called_once()
    mock_button.click.assert_called_once()

def test_select_main_theme(mocker):
    mock_driver = mocker.Mock()
    mock_option = mocker.Mock()

    mock_wait = mocker.Mock()
    mock_wait.until.return_value = mock_option
    mocker.patch('src.DropdownElement.WebDriverWait', return_value=mock_wait)

    mocker.patch('src.DropdownElement.time.sleep')

    dropdown = DropdownElement(mock_driver)
    dropdown.select_main_theme()

    mock_wait.until.assert_called_once()
    mock_option.click.assert_called_once()
