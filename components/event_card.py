from playwright.sync_api import Locator, expect

class EventCard:
    def __init__(self, card: Locator):
        self.card = card
        self.join_button = card.get_by_role("button", name="Join")
        self.open_button = card.get_by_role("button", name="Open")

    def is_visible(self) -> bool:
        expect(self.card).to_be_visible()
        return self.join_button.is_visible()

    def has_title(self, title: str) -> None:
        expect(self.card.get_by_text(title, exact=True)).to_be_visible()

    def click_join(self) -> None:
        expect(self.join_button).to_be_visible()
        # expect(self.open_button).to_be_enabled()
        self.join_button.click()

    def click_open(self) -> None:
        expect(self.open_button).to_be_visible()
        expect(self.open_button).to_be_enabled()
        self.open_button.click()