from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from creds import phone_number
from creds import issa_password
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://a1.by')
#time.sleep(2)
browser.find_element(By.ID, 'personalInfoMenu').click()
browser.find_element(By.ID, 'loginButton').click()
#time.sleep(2)
browser.find_element(By.ID, 'pwd_choose').click()
browser.find_element(By.NAME, 'UserID').send_keys(phone_number)
browser.find_element(By.NAME, 'mobilePassword').send_keys(issa_password)
browser.find_element(By.ID, 'butt1').click()
browser.find_element(By.ID, 'personalInfoMenu').click()

time.sleep(15)
