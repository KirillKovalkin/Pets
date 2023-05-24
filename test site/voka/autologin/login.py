from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_data import number, password
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://voka.tv/')
# time.sleep(3)
browser.find_element(By.CLASS_NAME, 'account').click()
#time.sleep(5)
browser.find_element(By.NAME, 'username').send_keys(number)
browser.find_element(By.NAME, 'password').send_keys(password)
browser.find_element(By.CLASS_NAME, 'bpQmxk').click()
browser.find_element(By.ID, 'menu_item_tv-v').click()

time.sleep(15)
