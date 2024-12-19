from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("/Users/lekhraj/StudentAndroidApp/StudentAndroidApp/Testcases/testdata.ini")
    return config.get(section, key)
