from BaseFiles import InitiateDriver
from Library import ConfigReader
import time
from Pages import LoginPage
from Pages import HomePage

def test_create_Asset():
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
    home.clickAssets()
    home.clickaddnewButton()
    home.enterAssetName('AutoAsset2')
    home.selectManagingOrg('DEMerge')
    home.selectHostingLocation('Afghanistan')
    home.clicksaveButton()

    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()

    # driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','Assets_xpath')).click()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','AddNew_xpath')).click()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','Name_xpath')).send_keys("AutoAsset2")
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','ManagingOrg_dropdown_xpath')).send_keys('DEMerge')
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','Org_xpath')).click()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','HostingLocation_xpath')).send_keys('Afghanistan')
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','country_xpath')).click()
    # driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','save_xpath')).click()
    time.sleep(5)
    assert driver.find_element_by_xpath(ConfigReader.readElementLocators('Details_tab','name_xpath')).is_displayed()

    InitiateDriver.close_Browser()