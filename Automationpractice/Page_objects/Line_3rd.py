from logging import exception

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Country_dropdwn:
    def __init__(self,driver):
        self.driver = driver
        self.country_drp = (By.XPATH,"//*[@id='root']/div/div/div/div/div/select")
        self.Agree = (By.CSS_SELECTOR,"#root > div > div > div > div > input")
        self.proceed = (By.CSS_SELECTOR,"#root > div > div > div > div > button")
        self.success = (By.XPATH,"/html/body/div[1]/div/div/div/div/span")

    def country(self):
        drop_down = self.driver.find_element(*self.country_drp)
        select = Select(drop_down)
        select.select_by_visible_text("Afghanistan")

        self.driver.find_element(*self.Agree).click()
        self.driver.find_element(*self.proceed).click()
        Success_msg = self.driver.find_element(*self.success).text
        print(Success_msg)