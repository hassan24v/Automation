from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 1. ابتدا درایور را نصب و مسیر آن را به کلاس Service می‌دهیم
service_obj = Service(ChromeDriverManager().install())

# 2. حالا شیء service را به webdriver معرفی می‌کنیم
driver = webdriver.Chrome(service=service_obj)

# Browser Action 1 > Open Web
driver.get("https://www.google.com/")
sleep(1)

# Browser Action 2 > Title
window_title = driver.title
print(window_title)

#sleep(2)
#driver.find_element('name',"q").send_keys("wikipedia")
#sleep(3)
#driver.quit()

# Browser Action 3 > Back
# driver.get("https://www.wikipedia")
# sleep(1)
# driver.back()
# sleep(1)

# Browser Action 4 > Forward
# driver.forward()
# sleep(1)

# Browser Action 5 > Refresh
# driver.refresh()
# sleep(1)

# Browser Action 6 > Refresh
# driver.refresh()
# sleep(1)

# Browser Action 7 > Open new window and switch to it (Tab)
# driver.switch_to.new_window('tab')
# sleep(3)
# a = driver.title
# print(a)  # در خروجی چیزی نشون نمیده چون تب جدیدی که باز میشه صفحه خالیه

# Browser Action 7 > Open new window and switch to it (Window)
# driver.switch_to.new_window('window')
# driber.get("https://www.yahoo.com") # در پنجره جدید سایت یاهو را باز می کند
# sleep(3)

# Browser Action 8 > Current window
# yahoo_window = driver.current_window_handle
# print('yahoo_handle' + str(yahoo_window))


# Browser Action 9 > All handles
# all_handles = driver.window_handles
# print('all_handle' + str(all_handles))

# Browser Action 10 > Switch
# driver.switch_to.window(all_handles[0])

# Browser Action 11 > Close tab
# driver.close()
# sleep(3)

# Browser Action 12 > Quit session
# driver.quit()

# Browser Action 13 > Window size
# window_size = driver.get_window_size()
# print(window_size)
# width = window_size['width']
# print(width)
# height = window_size['width']
# print(height)

# Browser Action 14 > Set window size
# driver.set_window_size(800, 600)
# size = driver.set_window_size(800, 600)
# assert size["width"]==1050
# print(size)

# Browser Action 15 > Get window position
# current_position = driver.get_window_position()
# print(current_position)

# Browser Action 16 > Set window position
# driver.set_window_position(400,500)
# sleep(3)
# assert driver.set_window_position["x"]==400

# Browser Action 17 > minimize window
# driver.minimize_window()
# sleep(1)

# Browser Action 18 > maximize window
# driver.maximize_window()
# sleep(1)

# Browser Action 19 > Full screen window
# driver.fullscreen_window()
# sleep(1)

