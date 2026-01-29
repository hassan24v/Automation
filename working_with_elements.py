from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. ابتدا درایور را نصب و مسیر آن را به کلاس Service می‌دهیم
service_obj = Service(ChromeDriverManager().install())

# 2. حالا شیء service را به webdriver معرفی می‌کنیم
driver = webdriver.Chrome(service=service_obj)
driver.get("https://wikipedia.com")

# 1 > ID
el1 = driver.find_element("id","searchInput")
# print(el1)
el1.send_keys("Hello World")

# 2 > Xpath
el2 = driver.find_element('xpath',"//input[@type='search']")
# print(el2)
# assert el1 == el2
el3 = driver.find_element('xpath',"//*[type()='Italiano']")
el3.click()
sleep(3)

# 3 > Tag
el4 = driver.find_element("tag name",'select')
el4.click()
sleep(3)

# 4 > Link text
el5 = driver.find_element('link text','Download Wikipedia for Android or iOS')
el5.click()
sleep(3)

# 5 > Partial link text
el6 = driver.find_element('partial link text','Download')
el6.click()
sleep(3)

# 6 > Class name and css selector
el7 = driver.find_element('class name',"svg-search-icon")
el7.click()
sleep(3)

driver.find_element('css selector',".svg-search-icon").click()
sleep(3)
driver.find_element('css selector',"#searchInput").click()
sleep(3)

