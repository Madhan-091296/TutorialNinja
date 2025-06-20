import os
import allure
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@allure.severity(allure.severity_level.CRITICAL)
class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_account_reg(self,setup):
        self.logger.info("********* Test Account Registration Started *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("********* Launching Application *********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.logger.info("********* Clicking on My Account --> Register *********")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)
        self.logger.info("********* Adding Customer Details *********")
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator()+"@gmail.com"
        self.regpage.setEmail(self.email)
        # self.regpage.setEmail('testttttttttttttttt@gmail.com')
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        #Validations
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("********* Account Registration is Passed *********")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.getcwd())+"\\screenshots\\"+"test_account_reg.png")
            assert False

        self.logger.info("********* Test Account Registration Finished *********")