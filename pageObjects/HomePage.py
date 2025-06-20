from selenium.webdriver.common.by import By
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchResultsPage import SearchResultsPage


class HomePage:
   lnk_myaccount_xpath = "//span[normalize-space()='My Account']"
   lnk_register_xpath = "//a[normalize-space()='Register']"
   lnk_login_linktext = "Login"
   txt_searchbox_xpath = "//input[@placeholder='Search']"
   btn_search_xpath = "//div[@id='search']//button[@type='button']"
   def __init__(self, driver):
       self.driver = driver
   def clickMyAccount(self):
       self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
   def clickRegister(self):
       self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()
       return AccountRegistrationPage(self.driver)
   def clickLogin(self):
       self.driver.find_element(By.LINK_TEXT, self.lnk_login_linktext).click()
       return LoginPage(self.driver)
   def enterProductName(self, productName):
       self.driver.find_element(By.XPATH, self.txt_searchbox_xpath).send_keys(productName)
   def clickSearch(self):
       self.driver.find_element(By.XPATH, self.btn_search_xpath).click()
       return SearchResultsPage(self.driver)
   def isHomePageExists(self):
       try:
           return self.driver.title == "Your Store"
       except:
           return False