from selenium.webdriver.common.by import By
# WebDriverWait را اضافه می‌کنیم تا پایداری افزایش یابد
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self,driver):
        self.driver = driver
        self.dashbord_lable_class =  (By.XPATH, "//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name']"
        )
        self.wait = WebDriverWait(driver, 10)  # تعریف WebDriverWait

    def check_main_page(self):
        #استفاده صحیح از Unpacking (*): اکنون self.driver.find_element(*self.dashbord_lable_class)
        #به درستی تاپل را به دو آرگومان جداگانه (نوع و مقدار) شکسته و به متد ارسال می‌کند. این مشکل سینتکسی حل شده است.
        self.driver.find_element(*self.dashbord_lable_class)