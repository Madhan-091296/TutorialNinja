import configparser
import os
config = configparser.RawConfigParser()

config.read(os.path.abspath(os.getcwd())+'\\configurations\\config.ini')
class ReadConfig():
  @staticmethod
  def getApplicationURL():
      url=(config.get('commonInfo', 'baseURL'))
      return url
  @staticmethod
  def getUseremail():
      username=(config.get('commonInfo', 'email'))
      return username
  @staticmethod
  def getPassword():
      password=(config.get('commonInfo', 'password'))
      return password
  @staticmethod
  def getProductName():
      productname = (config.get('commonInfo', 'searchProductName'))
      return productname
  @staticmethod
  def getProductQuantity():
      productqty = (config.get('commonInfo', 'productQuantity'))
      return productqty
  @staticmethod
  def getTotalPrice():
      totalprice = (config.get('commonInfo', 'totalPrice'))
      return totalprice
  @staticmethod
  def getEnvironment():
      environment = (config.get('commonInfo', 'execution_env'))
      return environment
