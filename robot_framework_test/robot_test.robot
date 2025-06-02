*** Settings ***
Library    SeleniumLibrary
Library    Process

*** Variables ***
${URL}          https://www.telerik.com/kendo-react-ui/components/layout/contextmenu
${REMOTE_URL}   http://selenium:4444/wd/hub

*** Test Cases ***
Robot Framework Test Automation Task
    Open Page
    Run Keyword And Ignore Error    Handle Cookies

    Execute JavaScript    document.evaluate("//p[text()='The following example demonstrates the KendoReact ContextMenu in action.']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView(true);

    Wait Until Element Is Visible    xpath=//iframe[contains(@class,'demo-module--demoFrame')]    10s
    Select Frame    xpath=//iframe[contains(@class,'demo-module--demoFrame')]
    Wait Until Element Is Visible    xpath=//div[contains(@class,'target')]    10s
    Unselect Frame

    Click Element    xpath=//button[@aria-label='Change theme']
    Wait Until Element Is Visible    xpath=//button[.//div[text()='Main']]    10s
    Click Element    xpath=//button[.//div[text()='Main']]

    Wait Until Element Is Visible    xpath=//iframe[contains(@class,'demo-module--demoFrame')]    10s
    Select Frame    xpath=//iframe[contains(@class,'demo-module--demoFrame')]
    Wait Until Element Is Visible    xpath=//div[contains(@class,'target')]    10s
    Open Context Menu    xpath=//div[contains(@class,'target')]

    Capture Page Screenshot          0.png

    Wait Until Element Is Visible     xpath=//li[.//span[text()='Style']]    10s
    Sleep    1s
    Mouse Over    xpath=//li[.//span[text()='Style']]

    Capture Page Screenshot          1.png

    Wait Until Element Is Visible   xpath=//li[.//span[text()='Underline']]    10s
    Sleep    1s
    Capture Page Screenshot          2.png
    Click Element    xpath=//li[.//span[text()='Underline']]

    Capture Page Screenshot          3.png

    Sleep    1s
    Capture Page Screenshot          output.png

    Unselect Frame
    [Teardown]    Close Browser

*** Keywords ***
Handle Cookies
    Wait Until Element Is Visible    xpath=//button[contains(@id,'onetrust-reject-all-handler')]    10s
    Sleep    1s
    Click Element    xpath=//button[contains(@id,'onetrust-reject-all-handler')]
    Sleep    1s


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