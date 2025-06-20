from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class CheckoutPage():
   lnk_chkout_xpath = "//a[text()='Checkout']"
   radio_new_xpath = "//input[@value='new']"
   btn_continue_xpath = "//input[@id='button-account']"
   txt_first_name_id = "input-payment-firstname"
   txt_last_name_id = "input-payment-lastname"
   txt_address1_id = "input-payment-address-1"
   txt_address2_id = "input-payment-address-2"
   txt_city_id = "input-payment-city"
   txt_pin_id = "input-payment-postcode"
   drp_country_id = "input-payment-country"
   drp_state_id = "input-payment-zone"
   btn_continue_billing_xpath = "//input[@id='button-payment-address']"
   btn_continue_delivery_xpath = "//input[@id='button-shipping-address']"
   txt_delivery_method_xpath = "//textarea[@name='comment']"
   btn_continue_shipping_xpath = "//input[@id='button-shipping-method']"
   chkbox_terms_xpath = "//input[@name='agree']"
   btn_continue_payment_xpath = "//input[@id='button-payment-method']"
   lbl_total_price_xpath = "//strong[text()='Total:']//following::td"
   btn_confirm_order_xpath = "//input[@id='button-confirm']"
   lbl_order_msg_xpath = "//*[@id='content']/h1"
   def __init__(self, driver):
       self.driver = driver
   def chooseCheckoutOption(self):
       self.driver.find_element(By.XPATH, self.lnk_chkout_xpath).click()
   def clickNewAddress(self):
       self.driver.find_element(By.XPATH, self.radio_new_xpath).click()
   def clickOnContinue(self):
       self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()
   def setFirstName(self, fname):
       self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(fname)
   def setLastName(self, lname):
       self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(lname)
   def setAddress1(self, address1):
       self.driver.find_element(By.ID, self.txt_address1_id).send_keys(address1)
   def setAddress2(self, address2):
       self.driver.find_element(By.ID, self.txt_address2_id).send_keys(address2)
   def setCity(self, city):
       self.driver.find_element(By.ID, self.txt_city_id).send_keys(city)
   def setPin(self, pin):
       self.driver.find_element(By.ID, self.txt_pin_id).send_keys(pin)
   def setCountry(self, country):
       Select(self.driver.find_element(By.ID, self.drp_country_id)).select_by_visible_text(country)
   def setState(self, state):
       Select(self.driver.find_element(By.ID, self.drp_state_id)).select_by_visible_text(state)
   def clickOnContinueAfterBillingAddress(self):
       self.driver.find_element(By.XPATH, self.btn_continue_billing_xpath).click()
   def clickOnContinueAfterDeliveryAddress(self):
       self.driver.find_element(By.XPATH, self.btn_continue_delivery_xpath).click()
   def setDeliveryMethodComment(self, comment):
       self.driver.find_element(By.XPATH, self.txt_delivery_method_xpath).send_keys(comment)
   def clickOnContinueAfterDeliveryMethod(self):
       self.driver.find_element(By.XPATH, self.btn_continue_shipping_xpath).click()
   def selectTermsAndConditions(self):
       self.driver.find_element(By.XPATH, self.chkbox_terms_xpath).click()
   def clickOnContinueAfterPaymentMethod(self):
       self.driver.find_element(By.XPATH, self.btn_continue_payment_xpath).click()
   def getTotalPriceBeforeConfOrder(self):
       return self.driver.find_element(By.XPATH, self.lbl_total_price_xpath).text
   def clickOnConfirmOrder(self):
       self.driver.find_element(By.XPATH, self.btn_confirm_order_xpath).click()
   def isOrderPlaced(self):
       return self.driver.find_element(By.XPATH, self.lbl_order_msg_xpath).text == "Your order has been placed!"
