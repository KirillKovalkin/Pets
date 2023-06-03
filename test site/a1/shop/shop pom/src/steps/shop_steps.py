from src.pages.ShopPage import ShopPage
from selenium.webdriver.common.by import By

def shop_step(driver):
        shop_page = ShopPage(driver)
        assert shop_page.open_shop_page()
        assert shop_page.move_to_down_page()
        assert shop_page.click_random_sales()
        assert shop_page.click_random_device()
        assert shop_page.click_price_block()
        assert shop_page.click_six_month()
        assert shop_page.click_enter_button()
        return True