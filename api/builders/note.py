import random

from faker import Faker

from api.models.note import NoteCategory, CreateNote, UpdateNote, UpdateNoteCompleteStatus

faker = Faker()


class CreateNoteBuilder:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.category = ""

    def random_title(self):
        self.title = faker.sentence()
        return self

    def random_description(self):
        self.description = faker.sentence()
        return self

    def random_category(self):
        self.category = random.choice(list(NoteCategory))
        return self

    def without_title(self):
        self.title = ""
        return self

    def without_description(self):
        self.description = ""
        return self

    def without_category(self):
        self.category = ""
        return self

    def invalid_category(self):
        self.category = "Test"
        return self

    def build(self):
        return CreateNote(
            title=self.title,
            description=self.description,
            category=self.category
        )


class UpdateNoteBuilder:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.completed = False
        self.category = ""

    def random_title(self):
        self.title = faker.sentence()
        return self

    def random_description(self):
        self.description = faker.sentence()
        return self

    def random_completed(self):
        self.completed = faker.boolean()
        return self

    def random_category(self):
        self.category = random.choice(list(NoteCategory))
        return self

    def invalid_category(self):
        self.category = "Test"
        return self

    def build(self):
        return UpdateNote(
            title=self.title,
            description=self.description,
            completed=self.completed,
            category=self.category
        )


class UpdateNoteCompleteStatusBuilder:
    def __init__(self):
        self.completed = False

    def set_completed(self, completed):
        self.completed = completed
        return self

    def build(self):
        return UpdateNoteCompleteStatus(
            completed=self.completed
        )
