from selenium.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from Library import ConfigReader
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from behave import *



def before_feature(context,feature):
    if ((ConfigReader.readConfigData('Details', 'Browser')) == "Chrome"):
        path = "./Driver/chromedriver.exe"
        context.driver = Chrome(executable_path=path)
    elif ((ConfigReader.readConfigData('Details', 'Browser')) == "Firefox"):
        path = "./Driver/geckodriver.exe"
        context.driver = Firefox(executable_path=path)
    elif ((ConfigReader.readConfigData('Details', 'Browser')) == "Ie"):
        path = "./Driver/IEDriverServer.exe"
        context.driver = Ie(executable_path=path)
    else:
        path = "./Driver/chromedriver.exe"
        context.driver = Chrome(executable_path=path)

    context.driver.maximize_window()
    context.driver.implicitly_wait(100)
    context.driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))

def before_scenario(context,scenario):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Email_xpath')).clear()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Email_xpath')).send_keys(
        "Shourya.ns+FA@gmail.com")
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Continue_xpath')).click()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Password_xpath')).clear()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Password_xpath')).send_keys(
        "Password@11")
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Login_xpath')).click()

def after_scenario(context,scenario):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators("Home", "Global_Header_xpath")).click()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators("Home", "Logout_option_xpath")).click()

def after_feature(context,feature):
    context.driver.close()

