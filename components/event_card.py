from playwright.sync_api import Locator, expect


class EventCard:
    def __init__(self, card: Locator) -> None:
        self.card = card
        self.join_button = card.get_by_role("button", name="Join")
        self.open_button = card.get_by_role("button", name="Open")
        self.leave_queue_button = card.get_by_role("button", name="Leave queue")

    def is_visible(self) -> bool:
        expect(self.card).to_be_visible()
        return self.card.is_visible()

    def get_title_text(self) -> str:
        title = self.card.locator("h2, h3").first.text_content()
        return title.strip() if title else ""

    def click_join(self) -> None:
        expect(self.join_button).to_be_visible()
        expect(self.join_button).to_be_enabled()
        self.join_button.click()

    def has_leave_queue_button(self) -> bool:
        expect(self.leave_queue_button).to_be_visible()
        return self.leave_queue_button.is_visible()
