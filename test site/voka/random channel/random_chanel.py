from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import datetime
import os

today = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
os.mkdir('screenshots_' + today )

for i in range(3):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://voka.tv/ru-RU/tv-v/tv-v2")
    browser.find_element(By.XPATH, "//section[@data-testid='card_collection'][1]/div/a").click()
    time.sleep(1)
    elements = browser.find_elements(By.XPATH, "//*[@class='_Foz4 VvSJ7']")
    element = random.choice(elements).click()
    time.sleep(3)
    now = datetime.now().strftime("%H:%M:%S")
    browser.save_screenshot('screenshots_' + today + '/' + now + '.png')
    browser.quit()
