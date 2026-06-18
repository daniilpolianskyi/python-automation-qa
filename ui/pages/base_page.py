from playwright.sync_api import Locator


class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator: Locator):
        locator.wait_for(state="visible")
        locator.scroll_into_view_if_needed()
        locator.click()

    def fill(self, locator: Locator, value: str):
        locator.wait_for(state="visible")
        locator.scroll_into_view_if_needed()
        locator.fill(value)

    def get_text(self, locator: Locator):
        locator.wait_for(state="visible")
        locator.scroll_into_view_if_needed()
        return locator.inner_text()
