from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("/Users/lekhraj/EmbibeStudentApp/pythonProject2/Testcases/testdata.ini")
    return config.get(section, key)
