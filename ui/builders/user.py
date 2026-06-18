from faker import Faker

from config import config
from ui.models.user import LoginUser, RegisterUser

faker = Faker()


class LoginUserBuilder:
    def __init__(self):
        self.username = ""
        self.password = ""

    def valid_username(self):
        self.username = config.UI_USERNAME
        return self

    def valid_password(self):
        self.password = config.UI_PASSWORD
        return self

    def random_username(self):
        self.username = faker.user_name()
        return self

    def random_password(self):
        self.password = faker.password()
        return self

    def without_username(self):
        self.username = ""
        return self

    def without_password(self):
        self.password = ""
        return self

    def build(self):
        return LoginUser(
            username=self.username,
            password=self.password
        )


class RegisterUserBuilder:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.confirm_password = ""

    def random_username(self):
        self.username = faker.user_name()
        return self

    def random_password(self):
        self.password = faker.password()
        return self

    def random_confirm_password(self):
        if not self.password:
            self.confirm_password = faker.password()
        else:
            self.confirm_password = self.password
        return self

    def mismatch_confirm_password(self):
        self.confirm_password = faker.password()
        return self

    def without_username(self):
        self.username = ""
        return self

    def without_password(self):
        self.password = ""
        return self

    def without_confirm_password(self):
        self.confirm_password = ""
        return self

    def build(self):
        return RegisterUser(
            username=self.username,
            password=self.password,
            confirm_password=self.confirm_password
        )
