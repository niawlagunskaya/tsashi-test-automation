import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    base_url: str
    test_user_email: str
    test_user_password: str
    browser_name: str
    headless: bool
    default_timeout_ms: int

def _get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value

settings = Settings(
    base_url=_get_required_env("BASE_URL").rstrip("/"),
    test_user_email=_get_required_env("TEST_USER_EMAIL"),
    test_user_password=_get_required_env("TEST_USER_PASSWORD"),
    browser_name=os.getenv("BROWSER", "chromium").lower(),
    headless=os.getenv("HEADLESS", "false").lower() == "true",
    default_timeout_ms=int(os.getenv("DEFAULT_TIMEOUT_MS", "10000")),
)














BASE_URL = os.getenv("BASE_URL")
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER_PASSWORD")
