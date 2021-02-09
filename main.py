# Auto Tinder Swiper (swipes left only)

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

MY_PASS = # Your password constant
MY_EMAIL = # Your email constant
chrome_driver_path = "C:/Development/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/app/recs")
time.sleep(3)
login_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')
login_btn.click()

time.sleep(1)
login_fb = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
login_fb.click()

time.sleep(2)

# Switch windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_id("pass")
email.send_keys(MY_EMAIL)
password.send_keys(MY_PASS)
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
print(driver.title)

# Allow page to load
time.sleep(5)
tndr_location = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
tndr_location.click()

time.sleep(5)
notifications = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications.click()

time.sleep(5)
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

dislike_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')

try:
    while True:
        time.sleep(10)
        dislike_btn.click()
        time.sleep(5)
except:
    time.sleep(5)

finally:
    time.sleep(5)
    while True:
        dislike_btn.click()




