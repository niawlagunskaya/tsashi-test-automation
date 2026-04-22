from pages.login_page import LoginPage
from pages.events_page import EventsPage
from config.settings import settings


def test_user_can_join_first_event_card(page) -> None:
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

    # action
    card.click_join()