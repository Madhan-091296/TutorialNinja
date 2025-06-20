from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.CheckoutPage import CheckoutPage  # Adjust import path as needed

class ShoppingCartPage():
   lbl_total_price_xpath = "//*[@id='content']/div[2]/div/table//strong[text()='Total:']//following::td"
   btn_checkout_xpath = "//a[text()='Checkout']"
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)
   def get_total_price(self):
       try:
           total_price_element = self.wait.until(
               EC.visibility_of_element_located((By.XPATH, self.lbl_total_price_xpath))
           )
           return total_price_element.text
       except Exception as e:
           print(f"Unable to retrieve total price: {e}")
           return None
   def click_on_checkout(self):
       try:
           checkout_button = self.wait.until(
               EC.element_to_be_clickable((By.XPATH, self.btn_checkout_xpath))
           )
           checkout_button.click()
           return CheckoutPage(self.driver)
       except Exception as e:
           print(f"Unable to click Checkout button: {e}")
           return None
