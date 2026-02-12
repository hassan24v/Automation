from selenium.webdriver.common.by import By
# WebDriverWait را اضافه می‌کنیم تا پایداری افزایش یابد
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import *

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # تعریف WebDriverWait

    def enter_username(self, username):
        # استفاده از سینتکس جدید: find_element(By.NAME, value)
        # منتظر می‌مانیم تا فیلد کاربر قابل رویت باشد
        user_field = self.wait.until(EC.presence_of_element_located(username_textbox_name))
        user_field.send_keys(username)

    def enter_password(self, password):
        # استفاده از سینتکس جدید: find_element(By.NAME, value)
        pass_field = self.wait.until(EC.presence_of_element_located(password_textbox_name))
        pass_field.send_keys(password)

    def click_on_login_button(self):
        # استفاده از سینتکس جدید و منتظر ماندن برای قابلیت کلیک
        login_btn = self.wait.until(EC.element_to_be_clickable(login_button_clickable))
        login_btn.click()

    def logout(self):
        # فرض بر این است که پس از Login موفق، ما به صفحه اصلی هستیم و باید Logout کنیم.
        # برای OrangeHRM، باید روی آیکون پروفایل در نوار بالا کلیک کنیم
        profile_icon = (By.XPATH, "//*[@class='oxd-userdropdown-name']")
        logout_link = (By.XPATH, "//*[@class='oxd-userdropdown-link']")

        self.wait.until(EC.element_to_be_clickable(profile_icon)).click()
        self.wait.until(EC.element_to_be_clickable(logout_link)).click()

        # پس از Logout، باید به صفحه لاگین برگردیم و منتظر یکی از المان‌های صفحه لاگین باشیم.
        #self.wait.until(EC.presence_of_element_located(username_textbox_name))

        # *** متد جدید: بررسی پیام خطا ***

    def check_login_error_message(self):
        # 1. تعریف کامل لوکیتور XPATH
        error_xpath = "//*[@class='oxd-text oxd-text--p oxd-alert-content-text']"

        # 2. ساختن By.XPATH و ارسال آن به عنوان یک آرگومان به EC
        error_locator = (By.XPATH, error_xpath)

        # منتظر می‌مانیم تا پیام خطا نمایش داده شود
        error_element = self.wait.until(
        EC.visibility_of_element_located(error_locator)  # فقط یک آرگومان (error_locator)
        )
        return error_element.text

        # منتظر می‌مانیم تا پیام خطا نمایش داده شود
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH,"//*[@class='oxd-text oxd-text--p oxd-alert-content-text']")
            ))
        return error_element.text