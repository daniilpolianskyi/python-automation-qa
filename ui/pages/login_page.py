from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username = self.page.locator("#username")
        self.password = self.page.locator("#password")
        self.login_btn = self.page.locator("#submit-login")
        self.message = self.page.locator("#flash-message")
        self.logout_btn = self.page.locator("a[href='/logout']")

    def open(self):
        self.page.goto("/login")

    def login(self, user):
        self.fill(self.username, user.username)
        self.fill(self.password, user.password)
        self.click(self.login_btn)

    def get_message_text(self):
        return self.get_text(self.message)
