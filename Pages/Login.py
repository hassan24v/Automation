from selenium.webdriver.common.by import By
# WebDriverWait را اضافه می‌کنیم تا پایداری افزایش یابد
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # تعریف WebDriverWait

        # Locators: (همانطور که تعریف کرده‌اید)
        self.username_textbox_name = (By.NAME, "username")
        self.password_textbox_name = (By.NAME, "password")
        self.login_button_xpath = (By.XPATH, "//button[@type='submit' and normalize-space(text())='Login']")

        # عنصر مرجع برای اطمینان از بارگذاری صفحه
        self.login_button_clickable = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        # استفاده از سینتکس جدید: find_element(By.NAME, value)
        # منتظر می‌مانیم تا فیلد کاربر قابل رویت باشد
        user_field = self.wait.until(EC.presence_of_element_located(self.username_textbox_name))
        user_field.send_keys(username)

    def enter_password(self, password):
        # استفاده از سینتکس جدید: find_element(By.NAME, value)
        pass_field = self.wait.until(EC.presence_of_element_located(self.password_textbox_name))
        pass_field.send_keys(password)

    def click_on_login_button(self):
        # استفاده از سینتکس جدید و منتظر ماندن برای قابلیت کلیک
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button_clickable))
        login_btn.click()
