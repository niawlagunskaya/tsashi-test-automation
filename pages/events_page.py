from playwright.sync_api import Page, Locator, expect

from pages.base_page import BasePage
from components.event_card import EventCard

class EventsPage(BasePage):
    EVENTS_PATH="/events"
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading: Locator = page.get_by_role("heading", name="Events")
        self.plans_tab: Locator = page.get_by_text("1:1 plans", exact=True)

    def open_events_page(self) -> None:
        self.open(self.EVENTS_PATH)
        expect(self.heading).to_be_visible()

    def select_plans_tab(self) -> None:
        expect(self.plans_tab).to_be_visible()
        self.plans_tab.click()

    def get_card_by_title(self, title: str) -> EventCard:
        card = self.page.locator("div").filter(
            has=self.page.get_by_text(title, exact=True)
        ).first
        expect(card).to_be_visible()
        return EventCard(card)

    def get_first_card(self):
        cards = self.page.locator("div").filter(
            has=self.page.get_by_role("button", name="Join")
        )
        first_card = cards.first
        return EventCard(first_card)
