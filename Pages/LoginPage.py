from Library import ConfigReader


class Login:
    def __init__(self,obj):
        global driver
        driver=obj

    def enterUserName(self,Username):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Email_xpath')).send_keys(Username)

    def clickContinue(self):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Continue_xpath')).click()

    def enterPassword(self,Password):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Password_xpath')).send_keys(
            Password)

    def clickLoginButton(self):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Login', 'Login_xpath')).click()

    def errorMessage(self):
        assert driver.find_element_by_id(ConfigReader.readElementLocators('Login', 'Error_message_id'))





