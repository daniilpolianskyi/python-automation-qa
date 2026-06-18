from faker import Faker

from api.models.profile import UpdateProfile

faker = Faker()


class UpdateProfileBuilder:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.company = ""

    def random_name(self):
        self.name = faker.user_name()
        return self

    def random_phone(self):
        self.phone = faker.numerify("+##########")
        return self

    def random_company(self):
        self.company = faker.company()
        return self

    def without_name(self):
        self.name = ""
        return self

    def without_phone(self):
        self.phone = ""
        return self

    def without_company(self):
        self.company = ""
        return self

    def build(self):
        return UpdateProfile(
            name=self.name,
            phone=self.phone,
            company=self.company
        )
