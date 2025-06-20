import time, pytest, allure
from utilities.readProperties import ReadConfig
from utilities import randomString
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from pageObjects.LogoutPage import LogoutPage
from pageObjects.CheckoutPage import CheckoutPage

@allure.severity(allure.severity_level.CRITICAL)
class Test_EndToEnd:
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    productName = ReadConfig.getProductName()
    productQuantity = ReadConfig.getProductQuantity()
    totalPrice = ReadConfig.getTotalPrice()

    @pytest.mark.regression
    def test_end_to_end(self, setup):
        self.logger.info("*** End-to-End Test Execution Started ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # step1 Registration
        email = self.perform_registration()
        #step2 Logout
        self.perform_logout()
        # step3 Login with Registered email
        self.perform_login(email)
        # step4 Search and Add Product to Cart
        self.add_product_to_cart()
        # step5 Verify shopping cart
        self.verify_cart()
        # step6 Checkout (optional/demo only)
        self.perform_checkout_and_fill_guest_details()
        self.logger.info("*** End-to-End Test Completed Successfully ***")

    def perform_registration(self):
        self.logger.info("*** Starting Registration ***")
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)
        email = randomString.random_string_generator() + "@gmail.com"
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Doe")
        self.regpage.setEmail(email)
        self.regpage.setTelephone("9999999999")
        self.regpage.setPassword(self.password)
        self.regpage.setConfirmPassword(self.password)
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        conf_msg = self.regpage.getconfirmationmsg()
        assert conf_msg == "Your Account Has Been Created!", "Registration failed!"
        self.logger.info(f"Registration successful with email: {email}")
        return email

    def perform_logout(self):
        self.logger.info("*** Logging out ***")
        self.ma = MyAccountPage(self.driver)
        self.lo = LogoutPage(self.driver)
        self.ma.clickLogout()
        self.hp = self.lo.clickContinue()
        assert self.hp.isHomePageExists(), "Logout failed or did not return to home page"
        self.logger.info("Logout successful and home page visible")

    def perform_login(self, email):
        self.logger.info("*** Logging in with registered email ***")
        self.hp.clickMyAccount()
        self.hp.clickLogin()
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        assert self.lp.isMyAccountPageExists(), "Login failed"
        self.logger.info("Login successful")

    def add_product_to_cart(self):
        self.logger.info("*** Searching product and adding to cart ***")
        self.hp.enterProductName(self.productName)
        self.srp = self.hp.clickSearch()
        assert self.srp.is_search_results_page_exists(), "Search results page not opened"
        assert self.srp.is_product_exist(self.productName), "Product not found in search results"
        self.pp = self.srp.select_product(self.productName)
        self.pp.setQuantity(self.productQuantity)
        time.sleep(2)
        self.pp.addToCart()
        time.sleep(2)
        assert self.pp.checkConfMsg(), "Product not added to cart"
        self.logger.info("Product added to cart successfully")

    def verify_cart(self):
        self.logger.info("*** Verifying Shopping Cart ***")
        self.pp.clickItemsToNavigateToCart()
        self.scp = self.pp.clickViewCart()
        total = self.scp.get_total_price()
        assert total == self.totalPrice, f"Expected total: {self.totalPrice}, got: {total}"
        self.logger.info("Shopping cart verified")

    def perform_checkout_and_fill_guest_details(self):
        self.cp = CheckoutPage(self.driver)
        self.cp.chooseCheckoutOption()
        self.cp.setFirstName("Madhan")  # Fill guest details
        self.cp.setLastName("Mohan")
        self.cp.setAddress1("address1")
        self.cp.setAddress2("address2")
        self.cp.setCity("Delhi")
        self.cp.setPin("500070")
        self.cp.setCountry("India")
        self.cp.setState("Delhi")
        self.cp.clickOnContinueAfterBillingAddress()
        self.cp.setDeliveryMethodComment("testing...")
        time.sleep(1)
        self.cp.selectTermsAndConditions()
        time.sleep(1)
        self.cp.clickOnContinueAfterPaymentMethod()



















