import pytest

from pages.login_page import LoginPage
from pages.events_page import EventsPage
from config.settings import settings

@pytest.mark.smoke
@pytest.mark.ui
def test_user_can_join_card_and_see_updated_state(page) -> None:
    login_page = LoginPage(page)
    events_page = EventsPage(page)

    # login
    login_page.login_as_valid_user(
        email=settings.test_user_email,
        password=settings.test_user_password,
    )

    # open events page
    events_page.open_events_page()
    events_page.select_plans_tab()

    # get first card
    card = events_page.get_first_card()

    # basic check
    assert card.is_visible()
    assert card.is_join_visible() is True

    # action
    card.click_join()

    assert card.is_leave_queue_visible() is True