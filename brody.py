"""
Key Idea: Every html element has a unique 'xpath'.  Thus, we can locate every button
based on their xpaths and click on them accordingly
"""

# Brody & Sis Automation
# MUST INSTALL SELENIUM & WEBDRIVER.  WEBDRIVER IS USED TO OPEN GOOGLE CHROME
# Search up yourself how to install selenium/webdriver because I lowkey forgot

#Import packages that are needed
from datetime import datetime
from threading import Timer
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#Entering Your Username & Password for JHU Portal
Username=input('Type your username here: ')
Passcode=input('Type your password here: ')

#Function to be executed at 12am to reserve BLC 2006 for 8 to 10pm
# Reserving Rooms in Brody Method
def brody_scheme():
	#Open up chrome, get to BLC website
	driver = webdriver.Chrome()
	driver.get("http://jhu.libcal.com/reserve/blc")
	time.sleep(5)

	#Click the time slot that we want
	elem = driver.find_element_by_xpath('//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/table/tbody/tr[5]/td/div/div/a[67]')

	elem.click()
	time.sleep(5)

	#Click an option that indicates until when the room will be reserved. Option[4] is for 2 hours
	list1=driver.find_element_by_xpath('//*[@id="bookingend_1"]')
	option1=driver.find_element_by_xpath('//*[@id="bookingend_1"]/option[4]')
	list1.click()
	option1.click()

	#Submit the time to reserve
	button = driver.find_element_by_id('submit_times')
	button.click()
	time.sleep(5)

	#Automation of typing in username and password to hopkins portal
	userID=driver.find_element_by_xpath('//*[@id="USER"]')
	password=driver.find_element_by_xpath('//*[@id="PASSWORD"]')
	userID.send_keys(Username)
	password.send_keys(Passcode)

	#Click login button
	button2=driver.find_element_by_xpath('//*[@id="submit1"]')
	button2.click()
	time.sleep(5)

	#Click to confirm and submit reservation
	continue_b=driver.find_element_by_xpath('//*[@id="terms_accept"]')
	continue_b.click()
	submit_b=driver.find_element_by_xpath('//*[@id="s-lc-eq-bform"]/fieldset/div[4]/div/button')
	submit_b.click()

	#Confirm that you are good on screen
	print("You're good")

	#Quit google chrome
	driver.quit()

# Course Registration Method
def reg_scheme():
	#Open up chrome, get to BLC website
	driver = webdriver.Chrome()
	driver.get("https://sis.jhu.edu/sswf/")
	time.sleep(5)

	#Click the time slot that we want
	elem = driver.find_element_by_xpath('//*[@id="btSignIn"]')

	elem.click()
	time.sleep(5)

	#Automation of typing in username and password to hopkins portal
	userID=driver.find_element_by_xpath('//*[@id="USER"]')
	password=driver.find_element_by_xpath('//*[@id="PASSWORD"]')
	userID.send_keys(Username)
	password.send_keys(Passcode)

	#Click login button
	button2=driver.find_element_by_xpath('//*[@id="submit1"]')
	button2.click()
	time.sleep(5)

	#Click to confirm and submit reservation
	continue_b1=driver.find_element_by_xpath('//*[@id="btnContinueToIsis"]')
	continue_b1.click()
	time.sleep(5)

	#Hover Over Registration Tab
	mainmenu = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[3]/nav[2]/div/ul[1]/li[1]/a')
	submenu = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[3]/nav[2]/div/ul[1]/li[1]/ul/li[3]/a')
	action=ActionChains(driver)
	action.move_to_element(mainmenu).perform()
	time.sleep(5)
	action.move_to_element(submenu)
	action.click().perform()

	#Click Box
	time.sleep(5)
	submit_b=driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_rptCart_ctl01_SelectSection"]')
	submit_b.click()
	submit_b=driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_rptCart_ctl02_SelectSection"]')
	submit_b.click()
	submit_b=driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_rptCart_ctl03_SelectSection"]')
	submit_b.click()
	submit_b=driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_rptCart_ctl04_SelectSection"]')
	submit_b.click()
	submit_b=driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_rptCart_ctl05_SelectSection"]')
	submit_b.click()

	#Wait before 7am to register

	finalClick=driver.find_element_by_xpath('//*[@id="ctl00_contentPlaceHolder_ibEnroll"]')
	bruh=datetime.today()
	bruh2=bruh.replace(day=x.day, hour=7, minute=5, second=0, microsecond=0)
	delta_time=bruh2-bruh
	seconds=delta_time.seconds+1
	time.sleep(seconds)
	finalClick.click()

	#Confirm that you are good on screen
	print("You're good")
	time.sleep(1000)

	#Quit google chrome
	driver.quit()

if (__name__=="__main__"):
    #True/False Parameter
    booling=0

    #A loop that allows for daily execution of brody_scheme
    # while (booling==0):
    #Takes today's time and counts down the number of seconds to 12am
    x=datetime.today()
    y=x.replace(day=x.day, hour=7, minute=3, second=0, microsecond=0)
    delta_t=y-x
    secs=delta_t.seconds+1

    #Wait for 'secs' number of seconds
    time.sleep(secs)

    # Execute SIS Registration Scheme
    reg_scheme()
