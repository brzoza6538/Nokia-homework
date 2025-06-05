*** Settings ***
Library    SeleniumLibrary
Library    Process

*** Variables ***
${URL}          https://www.telerik.com/kendo-react-ui/components/layout/contextmenu
${REMOTE_URL}   http://selenium:4444/wd/hub
${wait_until_time}    10
${animation_wait_time}    1
*** Test Cases ***
Robot Framework Test Automation Task
    Open Page
    Handle Cookies

    Scroll Down

    Select Theme 

    Select Style
    
    Sleep    ${animation_wait_time}s
    Capture Page Screenshot          output.png

    [Teardown]    Close Browser

*** Keywords ***
Handle Cookies    
    Sleep    ${animation_wait_time}s
    Wait Until Element Is Visible    xpath=//button[contains(@id,'onetrust-reject-all-handler')]    ${wait_until_time}s
    Sleep    ${animation_wait_time}s
    Click Element    xpath=//button[contains(@id,'onetrust-reject-all-handler')]

Scroll Down
    Execute JavaScript    document.evaluate("//p[text()='The following example demonstrates the KendoReact ContextMenu in action.']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView(true);

Select Demo Frame
    Wait Until Element Is Visible    xpath=//iframe[contains(@class,'demo-module--demoFrame')]    ${wait_until_time}s
    Select Frame    xpath=//iframe[contains(@class,'demo-module--demoFrame')]

Unselect Demo Frame
    Unselect Frame

Wait For Context Menu To Load
    Wait Until Element Is Visible    xpath=//div[contains(@class,'target')]    ${wait_until_time}s

Select Theme 
    Select Demo Frame
    Wait For Context Menu To Load
    Unselect Demo Frame

    Click Element    xpath=//button[@aria-label='Change theme']
    Wait Until Element Is Visible    xpath=//button[.//div[text()='Main']]    ${wait_until_time}s
    Sleep    ${animation_wait_time}s
    Click Element    xpath=//button[.//div[text()='Main']]

Select Style
    Select Demo Frame
    Wait For Context Menu To Load

    Open Context Menu    xpath=//div[contains(@class,'target')]
    Wait Until Element Is Visible     xpath=//li[.//span[text()='Style']]    ${wait_until_time}s
    Sleep    ${animation_wait_time}s
    Mouse Over    xpath=//li[.//span[text()='Style']]
    Wait Until Element Is Visible   xpath=//li[.//span[text()='Underline']]    ${wait_until_time}s
    Sleep    ${animation_wait_time}s
    Click Element    xpath=//li[.//span[text()='Underline']]
    Unselect Demo Frame


Log Firefox And GeckoDriver Version
    ${firefox_version}=    Run Process    firefox    --version    shell=True    stdout=TRUE
    Log    Firefox version: ${firefox_version.stdout}
    ${gecko_version}=     Run Process    geckodriver    --version    shell=True    stdout=TRUE
    Log    Geckodriver version: ${gecko_version.stdout}

Open Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
    Create WebDriver    Remote    command_executor=${REMOTE_URL}    options=${options}
    Go To    ${URL}
