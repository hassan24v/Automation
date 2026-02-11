from selenium.webdriver.common.by import By

#لوکیتورهای مورد نیاز برای صفحه لاگین
username_textbox_name = (By.NAME, "username")
password_textbox_name = (By.NAME, "password")
login_button_xpath = (By.XPATH, "//button[@type='submit' and normalize-space(text())='Login']")
login_button_clickable = (By.XPATH, "//button[@type='submit']")

#لوکیتورهای مورد نیاز برای صفحه اصلی پس از لاگین
dashbord_lable_class =  (By.XPATH, "//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")