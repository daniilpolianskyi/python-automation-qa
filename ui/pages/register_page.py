from ui.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.confirm_password = page.locator("#confirmPassword")
        self.register_btn = page.locator("button[type='submit']")
        self.message = page.locator("#flash-message")

    def open(self):
        self.page.goto("/register")

    def register(self, user):
        self.fill(self.username, user.username)
        self.fill(self.password, user.password)
        self.fill(self.confirm_password, user.confirm_password)
        self.click(self.register_btn)

    def get_message_text(self):
        return self.get_text(self.message)
