*** Settings ***
Library    SeleniumLibrary
Library    Process

*** Variables ***
${URL}          https://www.wp.pl
${REMOTE_URL}   http://selenium:4444/wd/hub

*** Test Cases ***
Screenshot Test
    # [Setup]    Log Firefox And GeckoDriver Version
    Open Page
    Capture Page Screenshot    screenshot.png
    [Teardown]    Close Browser

*** Keywords ***
Log Firefox And GeckoDriver Version
    ${firefox_version}=    Run Process    firefox    --version    shell=True    stdout=TRUE
    Log    Firefox version: ${firefox_version.stdout}
    ${gecko_version}=     Run Process    geckodriver    --version    shell=True    stdout=TRUE
    Log    Geckodriver version: ${gecko_version.stdout}

Open Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
    Create WebDriver    Remote    command_executor=${REMOTE_URL}    options=${options}
    Go To    ${Url}
