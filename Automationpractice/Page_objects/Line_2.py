import os

import openpyxl
from selenium.webdriver.common.by import By


class Page_2:
    def __init__(self,driver):
        self.driver = driver
        self.header = (By.CSS_SELECTOR,"#productCartTables > thead > tr")
        self.header_cell = (By.TAG_NAME,"tr")
        self.P_Table_cell = (By.TAG_NAME,"td")
        self.P_Table_row = (By.XPATH,"//*[@id='productCartTables']/tbody/tr")
        self.place_order = (By.XPATH,"//*[@id='root']/div/div/div/div/button")

    def page_2nd(self):

        row_cell = self.driver.find_elements(*self.header_cell)
        Row_text = [cell.text for cell in row_cell[1:]]

        text = []
        table_row = self.driver.find_elements(*self.P_Table_row)
        for row in table_row:
            table_cell = row.find_elements(*self.P_Table_cell)
            P_table_text = [cell.text for cell in table_cell[1:]]
            if P_table_text:
                text.append(P_table_text)

        book = openpyxl.load_workbook("Test_sheet/test_data.xlsx")
        sheet = book.active
        sheet.append(Row_text)

        for r in text:
            sheet.append(r)

        book.save("Test_sheet/test_data.xlsx")
        book.close()

        self.driver.find_element(*self.place_order).click()

