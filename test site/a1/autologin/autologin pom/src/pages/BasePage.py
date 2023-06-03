from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:

    # Конструктор, в который передается веб-драйвер для работы с нашими страницами
    def __init__(self, driver):
        self.driver = driver

    # Метод для кликов по элементам страницы
    def click_element(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()

    # Метод для ввода текста
    def type_text(self, locator, text):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).send_keys(text)
