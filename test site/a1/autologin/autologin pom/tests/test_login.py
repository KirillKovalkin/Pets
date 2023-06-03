from src.pages.LoginPage import LoginPage
from src.steps.login_steps import login_step
from selenium import webdriver

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login = "enter number"
    password = "enter password"

    # Open page
    login_page.open_login_page(),
    # Click user menu
    login_page.click_user_menu(),
    # Click login button
    login_page.click_login_button(),
    # Choose auth with pass
    login_page.choose_check_box_password(),
    # Set login
    login_page.set_phone_number(login),
    # Set Password
    login_page.set_password(password),
    # Click login button
    login_page.click_enter_login(),
    # return True
