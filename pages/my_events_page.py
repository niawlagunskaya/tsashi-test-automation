from playwright.sync_api import Locator, expect
from pages.base_page import BasePage
from components.event_card import EventCard

class MyEventsPage(BasePage):
    MY_EVENTS_PATH ="/my-events"
    def __init__(self, page: Page) -> None:
        super().__init__(page)

