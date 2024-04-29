import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    # Констуктор, в который передается веб дрейвер для работы с нашими страницами
    def __init__(self, driver):
        self.driver = driver

    # Метод для клика по элементам стрианцы
    def click_element(self, locator):
        return (
            WebDriverWait(self.driver, 30)
            .until(EC.element_to_be_clickable(locator))
            .click()
        )

    # Метод для случайного клика по элементу страницы
    def click_random_element(self, locator):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )
        element = random.choice(elements)
        return element.click()

    def resolve_js(self):
        return self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);"
        )
