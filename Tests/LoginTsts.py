from time import sleep
from Pages.Login import Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Pages.MainPage import MainPage
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            service = Service(ChromeDriverManager().install())
            cls.driver = webdriver.Chrome(service=service)
        except Exception:
            # Fallback در صورت بروز مشکل در webdriver_manager
            cls.driver = webdriver.Chrome()
        #cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_login1(self):
        # 1. رفتن به صفحه لاگین
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        # 2. اجرای ورود موفق
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login_button()

        # 3. تأیید صفحه اصلی
        main_page.check_main_page()
        sleep(1)

        # 4. *** کلید حل مشکل تداخل: خروج از سیستم ***
        login.logout()
        #sleep(1)  # انتظار برای بازگشت به صفحه لاگین

    def test_login2(self):
        # 1. بازگشت صریح به صفحه لاگین برای ایزوله‌سازی کامل
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)

        # 2. اجرای ورود ناموفق
        login.enter_username("Admin")
        login.enter_password("admin1234")  # پسورد اشتباه
        login.click_on_login_button()

        # 3. *** کلید حل مشکل Timeout: منتظر پیام خطا باشید نه صفحه اصلی ***
        error_text = login.check_login_error_message()

        # 4. تأیید پیام خطا
        self.assertIn("Invalid credentials", error_text, "پیام خطای ورود ناموفق یافت نشد.")
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()