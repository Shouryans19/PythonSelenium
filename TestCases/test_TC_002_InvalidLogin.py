from selenium.webdriver import Chrome
from BaseFiles import InitiateDriver
from selenium.webdriver.common.by import By
from Library import ConfigReader
from Pages import LoginPage

def test_InvalidLogin():
    driver=InitiateDriver.start_Browser()
    login = LoginPage.Login(driver)
    login.enterUserName("Shourya.ns+DEMerge@gmail.com")
    login.clickContinue()
    login.enterPassword("Password@1111")
    login.clickLoginButton()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Email_xpath')).send_keys(
    #     "shourya.ns+DEMerge@gmail.com")
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Continue_xpath')).click()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Password_xpath')).send_keys("Password@110")
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Login_xpath')).click()
   # assert driver.find_element_by_id(ConfigReader.readElementLocators('Login','Error_message_id'))
    InitiateDriver.close_Browser()

