from selenium.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from Library import ConfigReader
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from behave import *



def before_scenario(context,scenario):
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


def after_scenario(context,scenario):
    context.driver.quit()

