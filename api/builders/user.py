import uuid

from faker import Faker

from api.models.user import LoginUser, RegisterUser

faker = Faker()


class LoginUserBuilder:
    def __init__(self):
        self.user = LoginUser(
            email="",
            password=""
        )

    def email(self, email):
        self.user.email = email
        return self

    def password(self, password):
        self.user.password = password
        return self

    def random_email(self):
        self.user.email = f"{uuid.uuid4()}@email.com"
        return self

    def random_password(self):
        self.user.password = faker.password()
        return self

    def build(self):
        return self.user


class RegisterUserBuilder:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""

    def random_name(self):
        self.name = faker.user_name()
        return self

    def random_email(self):
        self.email = f"{uuid.uuid4()}@email.com"
        return self

    def random_password(self):
        self.password = faker.password()
        return self

    def build(self):
        return RegisterUser(
            name=self.name,
            email=self.email,
            password=self.password
        )
