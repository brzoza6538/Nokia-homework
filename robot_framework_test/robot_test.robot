*** Settings ***
Library    SeleniumLibrary
Library    Process

*** Variables ***
${URL}          https://www.telerik.com/kendo-react-ui/components/layout/contextmenu
${REMOTE_URL}   http://selenium:4444/wd/hub

*** Test Cases ***
Robot Framework Test Automation Task
    Open Page
    Handle Cookies

    Scroll Down

    Select Theme 

    Select Style
    
    Sleep    1s
    Capture Page Screenshot          output.png

    [Teardown]    Close Browser

*** Keywords ***
Handle Cookies    
    Sleep    1s
    Wait Until Element Is Visible    xpath=//button[contains(@id,'onetrust-reject-all-handler')]    10s
    Sleep    1s
    Click Element    xpath=//button[contains(@id,'onetrust-reject-all-handler')]

Scroll Down
    Execute JavaScript    document.evaluate("//p[text()='The following example demonstrates the KendoReact ContextMenu in action.']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView(true);

Select Demo Frame
    Wait Until Element Is Visible    xpath=//iframe[contains(@class,'demo-module--demoFrame')]    10s
    Select Frame    xpath=//iframe[contains(@class,'demo-module--demoFrame')]

Unselect Demo Frame
    Unselect Frame

Wait For Context Menu To Load
    Wait Until Element Is Visible    xpath=//div[contains(@class,'target')]    10s

Select Theme 
    Select Demo Frame
    Wait For Context Menu To Load
    Unselect Demo Frame

    Click Element    xpath=//button[@aria-label='Change theme']
    Wait Until Element Is Visible    xpath=//button[.//div[text()='Main']]    10s
    Sleep    1s
    Click Element    xpath=//button[.//div[text()='Main']]

Select Style
    Select Demo Frame
    Wait For Context Menu To Load

    Open Context Menu    xpath=//div[contains(@class,'target')]
    Wait Until Element Is Visible     xpath=//li[.//span[text()='Style']]    10s
    Sleep    1s
    Mouse Over    xpath=//li[.//span[text()='Style']]
    Wait Until Element Is Visible   xpath=//li[.//span[text()='Underline']]    10s
    Sleep    1s
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


# https://stackoverflow.com/questions/3401343/scroll-element-into-view-with-selenium