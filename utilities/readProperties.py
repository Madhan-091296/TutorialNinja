import configparser
import os
config = configparser.RawConfigParser()
config.read(os.path.dirname(os.getcwd())+'\\TutorialNinja\\configurations\\config.ini')
class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo','baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username = (config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password = (config.get('commonInfo', 'password'))
        return password
