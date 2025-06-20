from pageObjects.HomePage import HomePage
import allure
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

@allure.severity(allure.severity_level.NORMAL)
class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("********* Test Login Started *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("********* Launching Application *********")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.logger.info("********* Clicking on My Account --> Login *********")
        self.hp.clickMyAccount()
        self.hp.clickLogin()
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.targetpage = self.lp.isMyAccountPageExists()
        if self.targetpage == True:
            assert True
        else:
            assert False

        self.logger.info("********* Test Login Finished *********")