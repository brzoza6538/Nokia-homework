import pytest
from src.FrameHandler import FrameHandler
from src.GlobalVariables import *

def test_select_demo_frame(mocker):
    mock_driver = mocker.Mock()
    mock_iframe= mocker.Mock()

    mock_wait = mocker.Mock()
    mock_wait.until.return_value = mock_iframe
    mocker.patch('src.FrameHandler.WebDriverWait', return_value=mock_wait)

    menu = FrameHandler(mock_driver)
    menu.select_demo_frame()

    mock_wait.until.assert_called_once()
    mock_driver.switch_to.frame.assert_called_once_with(mock_iframe)

    called_arg = mock_wait.until.call_args.args[0]
    expected = EC.visibility_of_element_located((By.XPATH, demo_frame_xpath))
    assert type(called_arg) == type(expected)

def test_unselect_demo_frame(mocker):
    mock_driver = mocker.Mock()

    menu = FrameHandler(mock_driver)
    menu.unselect_demo_frame()

    mock_driver.switch_to.default_content.assert_called_once()

def test_wait_for_context_menu_to_load(mocker):
    mock_driver = mocker.Mock()

    mock_wait = mocker.Mock()
    mocker.patch('src.FrameHandler.WebDriverWait', return_value=mock_wait)

    menu = FrameHandler(mock_driver)
    menu.wait_for_context_menu_to_load()
    
    mock_wait.until.assert_called_once()

    called_arg = mock_wait.until.call_args.args[0]
    expected = EC.visibility_of_element_located((By.XPATH, context_target_xpath))
    assert type(called_arg) == type(expected)

