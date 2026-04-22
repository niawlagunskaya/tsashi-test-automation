from playwright.sync_api import Locator, Page, expect
from config.settings import settings
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_PATH = "/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.email_input: Locator = page.get_by_role("textbox", name="Email")
        self.password_input: Locator = page.get_by_role("textbox", name="Password")
        self.submit_button: Locator = page.get_by_role("button", name="Continue")
        self.login_form: Locator = page.locator("form")

    def open_login_page(self) -> None:
        self.open(self.LOGIN_PATH)
        expect(self.login_form).to_be_visible()

    def login(self, email: str, password: str) -> None:
        self.fill(self.email_input, email)
        self.fill(self.password_input, password)
        self.click(self.submit_button)

    def login_as_valid_user(self, email: str, password: str) -> None:
        self.open_login_page()
        self.login(email, password)
        expect(self.page).not_to_have_url(f"{settings.base_url}/login")
