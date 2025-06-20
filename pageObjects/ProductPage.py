from selenium.webdriver.common.by import By
from pageObjects.ShoppingCartPage import ShoppingCartPage

class ProductPage():
   txt_quantity_name = "quantity"
   btn_add_to_cart_id = "button-cart"
   cnf_msg_xpath = "//div[contains(text(),'Success: You have added')]"
   btn_items_id = "cart"
   lnk_view_cart_xpath = "//strong[normalize-space()='View Cart']"
   def __init__(self, driver):
       self.driver = driver
   def setQuantity(self, qty):
       qty_box = self.driver.find_element(By.NAME, self.txt_quantity_name)
       qty_box.clear()
       qty_box.send_keys(qty)
   def addToCart(self):
       self.driver.find_element(By.ID, self.btn_add_to_cart_id).click()
   def checkConfMsg(self):
       return self.driver.find_element(By.XPATH, self.cnf_msg_xpath).is_displayed()
   def clickItemsToNavigateToCart(self):
       self.driver.find_element(By.ID, self.btn_items_id).click()
   def clickViewCart(self):
       try:
           self.driver.find_element(By.XPATH, self.lnk_view_cart_xpath).click()
           return ShoppingCartPage(self.driver)
       except Exception as e:
           print(f"Unable to click View Cart link:  {e}")
           return None