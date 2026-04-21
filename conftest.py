import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from config.settings import settings

def _launch_browser(playwright: Playwright) -> Browser:
    browser_name = settings.browser_name

    if browser_name == "chromium":
        return playwright.chromium.launch(headless=settings.headless)
    if browser_name == "firefox":
        return playwright.firefox.launch(headless=settings.headless)
    if browser_name == "webkit":
        return playwright.webkit.launch(headless=settings.headless)

    raise ValueError(f"Unsupported browser: {browser_name}")

@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser = _launch_browser(playwright_instance)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    browser.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_default_timeout(settings.default_timeout_ms)
    yield page


