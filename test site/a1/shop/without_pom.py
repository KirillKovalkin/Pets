from selenium import webdriver
from selenium.webdriver.common.by import By
import random

for i in range(50):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.a1.by/ru/c/shop")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    sales = driver.find_elements(By.XPATH, "//div[contains(@class, 'tabs-controls-item')]")
    random.choice(sales).click()

    more = driver.find_elements(By.XPATH, "//div[@class='tabs-content-pane active']//div[@class='product-listing-item-btn']")
    random.choice(more).click()

    driver.find_element(By.XPATH, "//label[@for='i-priceBlock_selector_0']").click()
    driver.find_element(By.XPATH, "//div[contains(text(), '6 мес')]").click()

    mobile = driver.find_element(By.XPATH, "//h1[@class='h h--1 pdp-header-heading']").text
    pay = driver.find_element(By.XPATH, "//span[@class='select2-selection__rendered']").text
    print ("Выбран " + mobile + " условия " + pay)

    driver.find_element(By.XPATH, "//div[@id='CURRENT_CONTRACT']//div[@class='live-filter-content-item active']//button").click()
    driver.quit()
  
