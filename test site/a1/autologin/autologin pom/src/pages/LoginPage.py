from selenium import webdriver
from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage

# Класс с определеним локаторов

class LoginPageLocators:

    # 1) Дропдаун юзер меню
    user_menu = (By.ID, 'personalInfoMenu')

    # 2) Кнопка логина
    login_button = (By.ID, 'loginButton')

    # 3) Выбор чек-бокса по паролю
    check_box_password = (By.XPATH, "//*[contains(text(),'По паролю')]")
   
    # 4) Ввод номера телефона
    phone_number = (By.ID, 'itelephone_new')

    # 5) Ввод пароля
    password = (By.ID, 'ipassword')

    # 6) Кнопка войти
    enter_button = (By.ID, 'butt1')

# Класс с описанием методов страницы

class LoginPage(BasePage):

    #1 Дропнуть меню
    def click_user_menu(self):
        return self.click_element(LoginPageLocators.user_menu)

    #2 Нажать войти
    def click_login_button(self):
        return self.click_element(LoginPageLocators.login_button)
    
    #3 Выбрать чекбокс по паролю
    def choose_check_box_password(self):
        return self.click_element(LoginPageLocators.check_box_password)

    #4 Ввести номер телефона
    def set_phone_number(self, login):
        return self.type_text(LoginPageLocators.phone_number, login)

    #5 Ввести пароль
    def set_password(self, password):
        return self.type_text(LoginPageLocators.password, password)
    
    # 6 Нажать на кнопку войти в аккаунт
    def click_enter_login(self):
        return self.click_element(LoginPageLocators.enter_button)

    # Открывашка страницы
    def open_login_page(self):
        self.driver.get("https://a1.by/")
        return True

        
    


