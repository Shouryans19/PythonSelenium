import configparser

def readConfigData(section,key):
    config=configparser.ConfigParser()
    config.read("./Configuration/Config.cfg")
    return config.get(section,key)

def readElementLocators(section,key):
    config = configparser.ConfigParser()
    config.read("./Configuration/Elements.cfg")
    return config.get(section, key)


