import os

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
@pytest.mark.sanity
class Test_001_AccountReg:
    # baseURL = "https://tutorialsninja.com/demo/index.php?route=common/home"
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    def test_account_reg(self,setup):
        self.logger.info("test_001_AccountRegistartion started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Launching Application")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.logger.info("Clicking on My Account")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("Providing customer details for registartion")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator()+"@gmail.com"
        # self.regpage.setEmail('suma@gmail.com')
        # self.regpage.setEmail(ReadConfig.getUseremail())
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword(ReadConfig.getPassword())
        self.regpage.setConfirmPassword(ReadConfig.getPassword())
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account Registration successful")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.getcwd()+"\\screenshots\\"+"test_account_reg.png"))
            self.driver.close()
            self.logger.info("Account Registration failed")
            assert False
        self.logger.info("test_001_AccountRegistartion finished")

