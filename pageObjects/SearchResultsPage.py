from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.ProductPage import ProductPage  # Ensure correct import path

class SearchResultsPage():
   search_page_header_xpath = "//div[@id='content']/h1"
   search_products_xpath = "//*[@id='content']/div[3]//img"
   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)
   def is_search_results_page_exists(self):
       try:
           header = self.driver.find_element(By.XPATH, self.search_page_header_xpath)
           return "Search -" in header.text
       except Exception:
           return False
   def is_product_exist(self, product_name):
       try:
           products = self.wait.until(
               EC.visibility_of_all_elements_located((By.XPATH, self.search_products_xpath))
           )
           for product in products:
               if product.get_attribute("title") == product_name:
                   return True
       except Exception as e:
           print(f"Error checking product existence: {e}")
       return False
   def select_product(self, product_name):
       try:
           products = self.wait.until(
               EC.visibility_of_all_elements_located((By.XPATH, self.search_products_xpath))
           )
           for product in products:
               if product.get_attribute("title") == product_name:
                   self.wait.until(EC.element_to_be_clickable(product)).click()
                   return ProductPage(self.driver)
           print(f"Product not found: {product_name}")
       except Exception as e:
           print(f"Error selecting product: {e}")
       return None