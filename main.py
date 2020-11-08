from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

if (__name__ == "__main__"):
    # Step 3a: Get username and password
    Username = input("Enter your username:")
    Password = getpass("Enter your password:")

    # Step 6: Set up Chrome opening timer
    now = datetime.today()
    chromeOpenDate = datetime.today()
    chromeOpenDate = chromeOpenDate.replace(day = datetime.today().day, hour = 6, minute = 55, second = 0, microsecond = 0)
    deltaChromeDate = chromeOpenDate - now
    time.sleep(deltaChromeDate.seconds + 1)

    # Step 1: Open up google chrome.
    driver = webdriver.Chrome(executable_path = './chromedriver')
    driver.get('https://sis.jhu.edu/sswf/')

    # Step 2: Click sign in button
    signInButton = driver.find_element_by_xpath('//*[@id="linkSignIn"]')
    signInButton.click()
    time.sleep(2)

    # Step 3b: Enter in username and password
    usernameInputBox = driver.find_element_by_xpath('//*[@id="i0116"]')
    usernameInputBox.send_keys(Username)
    nextButton = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    nextButton.click()
    time.sleep(2)

    passwordInputBox = driver.find_element_by_xpath('//*[@id="i0118"]')
    passwordInputBox.send_keys(Password)
    signInButtonMicrosoft = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    signInButtonMicrosoft.click()
    time.sleep(2)

    # Step 4: Click my cart tab
    actionList = ActionChains(driver)
    registrationTab = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[3]/nav[2]/div/ul[1]/li[1]/a')
    myCartTab = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[3]/nav[2]/div/ul[1]/li[1]/ul/li[3]/a')
    actionList.move_to_element(registrationTab)
    actionList.perform()
    time.sleep(2)
    actionList.move_to_element(myCartTab)
    actionList.click()
    actionList.perform()
    time.sleep(2)

    # Step 5: Click checkbox and register
    checkbox = driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_rptCart_ctl01_SelectSection"]')
    checkbox.click()

    # Step 7: Set up Registration timer
    now = datetime.today()
    registrationDate = datetime.today()
    registrationDate = registrationDate.replace(day = datetime.today().day, hour = 7, minute = 0, second = 0, microsecond = 0)
    deltaRegistrationDate = registrationDate - now
    time.sleep(deltaRegistrationDate.seconds + 1)
    registerButton = driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_ibEnroll"]')
    registerButton.click()

    # Optional Step: close webdriver
    time.sleep(1000)
    # driver.quit()
