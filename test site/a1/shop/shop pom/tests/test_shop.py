from src.pages.ShopPage import ShopPage


def test_choose_six_month_device(driver):
    shop_page = ShopPage(driver)

    # Открыть страницу магазина
    shop_page.open_shop_page()

    shop_page.move_to_down_page()

    # Выбрать случайную акцию
    shop_page.click_random_sales()

    # Выбрать случайный девайс
    shop_page.click_random_device()

    # Кликнуть на блок с условиями покупки
    shop_page.click_price_block()

    # Выбрать рассрочку на 6 месяцев
    shop_page.click_six_month()

    # Нажать кнопку войти
    shop_page.click_enter_button()
