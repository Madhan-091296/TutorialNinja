import os
import time
import pytest
import allure

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@allure.severity(allure.severity_level.MINOR)
class Test_LoginDDT:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = os.path.abspath(os.getcwd()) + '\\testData\\Tutorialninja_LoginData.xlsx'
    # path = '..\\testData\\Tutorialninja_LoginData.xlsx'

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********* Test Login DDT Started *********")
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        lst_status = []
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("********* Launching Application *********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyAccountPage(self.driver)
        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            self.targetpage = self.lp.isMyAccountPageExists()

            if self.exp == "Valid":
                if self.targetpage == True:
                    lst_status.append("Pass")
                    self.ma.clickLogout()
                else:
                    lst_status.append("Fail")

            elif self.exp == "Invalid":
                if self.targetpage == True:
                    lst_status.append("Fail")
                    self.ma.clickLogout()
                else:
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("********* Test Login DDT Finished *********")



