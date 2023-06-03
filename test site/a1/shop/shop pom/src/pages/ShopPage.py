from src.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import random

class ShopLocators:

    # Выбор акции
    choose_sales = (By.XPATH, "//div[contains(@class, 'tabs-controls-item')]")

    # Выбор устройства по кнопке Подробнее
    choose_more_info = (By.XPATH, "//div[@class='tabs-content-pane active']//div[@class='product-listing-item-btn']")

    # Выбор дропдауна с условиями продажи
    choose_dropdown_price = (By.XPATH, "//label[@for='i-priceBlock_selector_0']")

    # Выбор 6 месячной рассрочки
    choose_dropdown_options = (By.XPATH, "//div[contains(text(), '6 мес')]")

    # Выбрать название девайся
    choose_device_text = (By.XPATH, "//h1[@class='h h--1 pdp-header-heading']")
    
    # Выбор цены девайса
    choose_price_text = (By.XPATH, "//span[@class='select2-selection__rendered']")

    # Нажатие на кнопку войти
    choose_enter = (By.XPATH, "//div[@id='CURRENT_CONTRACT']//div[@class='live-filter-content-item active']//button")



class ShopPage(BasePage):

    # Открываем страницу
    def open_shop_page(self):
        self.driver.get("https://www.a1.by/ru/c/shop")
        return True

    # Кликаем по случайной акции
    def click_random_sales(self):
        self.click_random_element(ShopLocators.choose_sales)
        return True

    # Резолвим js
    def move_to_down_page(self):
        self.resolve_js()
        return True
        
    # Кликаем по случайному девайсу
    def click_random_device(self):
        self.click_random_element(ShopLocators.choose_more_info)
        return True

    # Открываем блок с улсовиями приобритения
    def click_price_block(self):
        self.click_element(ShopLocators.choose_dropdown_price)
        return True

    # Выбираем 6 месяцев
    def click_six_month(self):
        self.click_element(ShopLocators.choose_dropdown_options)
        return True

    # Нажимаем кнопку входа
    def click_enter_button(self):
        self.click_element(ShopLocators.choose_enter)
        return True