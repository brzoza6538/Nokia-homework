*** Settings ***
Library    SeleniumLibrary
Library    Process
Library    src.CustomKeywords


*** Variables ***
${URL}          https://www.telerik.com/kendo-react-ui/components/layout/contextmenu
${REMOTE_URL}   http://selenium:4444/wd/hub

*** Test Cases ***
Robot Framework Test Automation Task
    Open Page
    Handle Cookies
    Scroll To Context Menu Example
    Set Driver From SeleniumLibrary

    Change Theme Using Python Keyword
    Interact With Context Menu
    Sleep    1s
    Capture Page Screenshot    output.png
    [Teardown]    Close Browser

*** Keywords ***
Handle Cookies    
    Sleep    1s
    Wait Until Element Is Visible    xpath=//button[contains(@id,'onetrust-reject-all-handler')]    10s
    Sleep    1s
    Click Element    xpath=//button[contains(@id,'onetrust-reject-all-handler')]


Scroll To Context Menu Example
    Execute JavaScript    document.evaluate("//p[text()='The following example demonstrates the KendoReact ContextMenu in action.']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView(true);

    Sleep    10s

Open Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
    Create WebDriver    Remote    command_executor=${REMOTE_URL}    options=${options}
    Go To    ${URL}

