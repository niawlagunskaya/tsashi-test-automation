from playwright.sync_api import expect

from config.settings import settings
from pages.login_page import LoginPage

def test_user_can_log_in(page) -> None:
    login_page = LoginPage(page)

    login_page.login_as_valid_user(
        email=settings.test_user_email,
        password=settings.test_user_password
    )

    expect(page).not_to_have_url(f"{settings.base_url}{login_page.LOGIN_PATH}")