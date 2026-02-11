from time import sleep
from Login import Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage

service_obj = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(3)

login = Login(driver = driver)
main_page = MainPage(driver = driver)

login.enter_username("Admin")
login.enter_password("admin123")
login.click_on_login_button()
main_page.check_main_page()
sleep(1)


