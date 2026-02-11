from selenium.webdriver.common.by import By
# WebDriverWait را اضافه می‌کنیم تا پایداری افزایش یابد
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators import *


class MainPage:
    def __init__(self,driver):
        self.driver = driver
        self.dashbord_lable_class =  dashbord_lable_class
        self.wait = WebDriverWait(driver, 10)  # تعریف WebDriverWait

    def check_main_page(self):
        #self.driver.find_element(dashbord_lable_class)
        self.wait.until(EC.visibility_of_element_located(self.dashbord_lable_class))
