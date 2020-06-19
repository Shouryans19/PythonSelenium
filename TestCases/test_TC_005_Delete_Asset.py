from BaseFiles import InitiateDriver
from Library import ConfigReader
import time

def test_delete_Asset():
    driver = InitiateDriver.start_Browser()
    driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Email_xpath')).send_keys(
        "shourya.ns+DEMerge@gmail.com")
    driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Continue_xpath')).click()
    driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Password_xpath')).send_keys("Password@11")
    driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Login_xpath')).click()
    driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()
    driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','Assets_xpath')).click()
    time.sleep(5)
    driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','search_xpath')).send_keys("AutoAsset2")
    time.sleep(3)
    driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','Asset_link')).click()
    driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','Inventory_details_cm')).click()
    driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','Delete_menu')).click()
    driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','Delete_Modal_xpath')).click()
    time.sleep(5)
    assert driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','No_records_found')).is_displayed()

    InitiateDriver.close_Browser()