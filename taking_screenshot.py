from subprocess import check_output

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pathlib import Path
import os
from selenium.webdriver.chrome.options import Options

check_option = Options()
#check_option.add_argument("--incognito")
check_option.add_argument("--headless")

# 1. ابتدا درایور را نصب و مسیر آن را به کلاس Service می‌دهیم
service_obj = Service(ChromeDriverManager().install())

# 2. حالا شیء service را به webdriver معرفی می‌کنیم
driver = webdriver.Chrome(service=service_obj)


driver.get("https://www.yahooe.com/")
sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(10)
current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'screenshot.png')
driver.save_screenshot(file_name)

