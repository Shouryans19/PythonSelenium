from BaseFiles import InitiateDriver
from Library import ConfigReader
from Pages import LoginPage
from Pages import HomePage

def test_NavigateTo_DataMapping():
    driver = InitiateDriver.start_Browser()
    login = LoginPage.Login(driver)
    login.enterUserName("Shourya.ns+DEMerge@gmail.com")
    login.clickContinue()
    login.enterPassword("Password@11")
    login.clickLoginButton()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Email_xpath')).send_keys(
    #     "shourya.ns+DEMerge@gmail.com")
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Continue_xpath')).click()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Password_xpath')).send_keys("Password@11")
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Login_xpath')).click()
    home = HomePage.Home(driver)
    home.selectModule()
    home.verifydashBoard()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()
    # DM=driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Dashboard_xpath'))
    # assert DM.is_displayed()
    InitiateDriver.close_Browser()
