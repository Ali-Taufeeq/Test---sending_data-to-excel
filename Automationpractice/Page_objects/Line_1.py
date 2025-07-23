import time
from time import sleep

import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:
    def __init__(self,driver):
        self.driver = driver
        self.send_key = (By.CSS_SELECTOR,".search-keyword")
        self.Add1 = (By.XPATH,"//*[@id='root']/div/div[1]/div/div[4]/div[3]/button")
        self.Add2 = (By.XPATH,"//*[@id='root']/div/div[1]/div/div[6]/div[3]/button")
        self.Add3 = (By.XPATH,"//*[@id='root']/div/div[1]/div/div[2]/div[3]/button")
        self.cart_icon = (By.CSS_SELECTOR,"#root > div > header > div > div.cart > a.cart-icon > img")
        self.proceed = (By.CSS_SELECTOR,"#root > div > header > div > div.cart > div.cart-preview.active > div.action-block > button")

    def searching_btn(self):
        self.driver.find_element(*self.send_key).send_keys("n")
        time.sleep(2)
        self.driver.find_element(*self.Add1).click()
        self.driver.find_element(*self.Add2).click()
        self.driver.find_element(*self.Add3).click()
        time.sleep(5)
        self.driver.find_element(*self.cart_icon).click()
        self.driver.find_element(*self.proceed).click()

