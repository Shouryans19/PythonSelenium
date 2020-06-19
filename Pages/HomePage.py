from Library import ConfigReader


class Home:
    def __init__(self,obj):
        global driver
        driver=obj

    def selectModule(self):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()

    def verifydashBoard(self):
        DM = driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Dashboard_xpath'))
        assert DM.is_displayed()

    def clickAssets(self):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Assets_xpath')).click()

    def clickaddnewButton(self):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'AddNew_xpath')).click()

    def enterAssetName(self,AssetName):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'Name_xpath')).send_keys(AssetName)

    def selectManagingOrg(self,ManagingOrg):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'ManagingOrg_dropdown_xpath')).send_keys(
            ManagingOrg)
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'Org_xpath')).click()

    def selectHostingLocation(self,HL):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'HostingLocation_xpath')).send_keys(
            HL)
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'country_xpath')).click()

    def clicksaveButton(self):
        driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'save_xpath')).click()
