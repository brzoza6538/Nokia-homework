*** Settings ***
Library    SeleniumLibrary
Library    Process
Library    src.CustomKeywords
Variables        src.GlobalVariables


*** Variables ***
${URL}          https://www.telerik.com/kendo-react-ui/components/layout/contextmenu

*** Test Cases ***
Robot Framework Test Automation Task
    Log Firefox And GeckoDriver Version
    Open Page
    Handle Cookies
    Scroll To Context Menu Example
    Set Driver From SeleniumLibrary

    Change Theme Using Python Keyword
    Interact With Context Menu
    Sleep    ${animation_wait_time}s
    Capture Page Screenshot    output.png
    [Teardown]    Close Browser

*** Keywords ***
Handle Cookies    
    Sleep    ${animation_wait_time}s
    Wait Until Element Is Visible    xpath=//button[contains(@id,'onetrust-reject-all-handler')]    ${wait_until_time}s
    Sleep    ${animation_wait_time}s
    Click Element    xpath=//button[contains(@id,'onetrust-reject-all-handler')]


Scroll To Context Menu Example
    Execute JavaScript    document.evaluate("//p[text()='The following example demonstrates the KendoReact ContextMenu in action.']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView(true);
    Sleep    ${animation_wait_time}s

Log Firefox And GeckoDriver Version
    ${firefox_version}=    Run Process    firefox    --version
    Log    Firefox version: ${firefox_version.stdout}
    ${gecko_version}=     Run Process    geckodriver    --version
    Log    Geckodriver version: ${gecko_version.stdout}

Open Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --headless
    Create WebDriver    Firefox    options=${options}
    Go To    ${URL}
