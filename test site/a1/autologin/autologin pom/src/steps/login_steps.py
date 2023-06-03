from src.pages.LoginPage import LoginPage

def login_step(driver, login, password):
    login_page = LoginPage(driver)
    assert login_page.open_login_page()
    assert login_page.click_user_menu()
    assert login_page.click_login_button()
    assert login_page.choose_check_box_password()
    assert login_page.set_phone_number(login)
    assert login_page.set_password(password)
    assert login_page.click_enter_login()
    return True
