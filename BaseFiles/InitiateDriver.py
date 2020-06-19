from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import ie


from Library import ConfigReader

def start_Browser():
    global driver
    if((ConfigReader.readConfigData('Details','Browser'))== "Chrome"):
        path = "./Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
    elif ((ConfigReader.readConfigData('Details','Browser'))== "Firefox"):
        path = "./Driver/geckodriver.exe"
        driver = Firefox(executable_path=path)
    elif ((ConfigReader.readConfigData('Details','Browser'))== "ie"):
        path = "./Driver/IEDriverServer.exe"
        driver = ie(executable_path=path)
    else:
        path = "./Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)

    driver.maximize_window()
    driver.implicitly_wait(100)
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    return driver

def close_Browser():
    driver.close()