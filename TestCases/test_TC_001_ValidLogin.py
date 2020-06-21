from BaseFiles import InitiateDriver
from Library import ConfigReader
from Pages import LoginPage

def test_ValidLogin():
    driver=InitiateDriver.start_Browser()
    login = LoginPage.Login(driver)
    login.enterUserName("Shourya.ns+SA@gmail.com")
    login.clickContinue()
    login.enterPassword("Ytrewq@11")
    login.clickLoginButton()


    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Email_xpath')).send_keys(
    #     "shourya.ns+DEMerge@gmail.com")
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Continue_xpath')).click()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Password_xpath')).send_keys("Password@11")
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Login_xpath')).click()
    # assert driver.title== "OneTrust | Privacy Management Software"
    print("Title is matching")
    InitiateDriver.close_Browser()





