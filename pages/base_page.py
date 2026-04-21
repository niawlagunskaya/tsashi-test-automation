from playwright.sync_api import Locator, Page, expect

from config.settings import settings

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path:str = "") -> None:
        normalized_path = path if path.startswith("/") or path =="" else f"/{path}"
        self.page.goto(f"{settings.base_url}{normalized_path}")

    def click(self, locator: Locator) -> None:
        expect(locator).to_be_visible()
        expect(locator).to_be_enabled()
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        expect(locator).to_be_visible()
        locator.fill(value)

    def get_text(self, locator: Locator) -> str:
        expect(locator).to_be_visible()
        text = locator.text_content()
        return text.strip() if text else ""

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    def wait_for_url_contains(self, value: str) -> None:
        expect(self.page).to_have_url(lambda current_url: value in current_url)

    def get_current_url(self) -> str:
        return self.page.url