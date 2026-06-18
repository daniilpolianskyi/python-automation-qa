import pytest
from playwright.sync_api import sync_playwright

from config import config
from ui.builders.user import LoginUserBuilder, RegisterUserBuilder
from ui.pages.login_page import LoginPage
from ui.pages.register_page import RegisterPage


# Playwright

@pytest.fixture
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=config.UI_HEADLESS
    )
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(
        base_url=config.UI_BASE_URL
    )
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    page.set_default_timeout(config.UI_TIMEOUT)
    yield page
    page.close()


# Pages

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def register_page(page):
    return RegisterPage(page)

# User

@pytest.fixture
def login_user_builder():
    return LoginUserBuilder()

@pytest.fixture
def register_user_builder():
    return RegisterUserBuilder()
