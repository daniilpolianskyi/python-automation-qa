import pytest

from api.api_clients.api_client import APIClient
from api.builders.note import CreateNoteBuilder, UpdateNoteBuilder, UpdateNoteCompleteStatusBuilder
from api.builders.profile import UpdateProfileBuilder
from api.builders.user import LoginUserBuilder, RegisterUserBuilder


# API Client

@pytest.fixture
def api_client():
    api_client = APIClient()
    yield api_client
    api_client.close()


@pytest.fixture
def auth_api_client(api_client, token):
    auth_api_client = APIClient()
    auth_api_client.set_token(token)
    yield auth_api_client
    auth_api_client.close()


# Auth

@pytest.fixture
def user(api_client):
    user = RegisterUserBuilder().random_name().random_email().random_password().build()
    api_client.post("/users/register", user.model_dump())
    yield user
    try:
        login = api_client.post("/users/login", user.model_dump())
        token = login.json()["data"]["token"]
        api_client.set_token(token)
        api_client.delete("/users/delete-account")
    except Exception:
        pass


@pytest.fixture
def token(api_client, user):
    login = api_client.post("/users/login", user.model_dump())
    token = login.json()["data"]["token"]
    return token


@pytest.fixture
def user_id(auth_api_client, user, token):
    auth_api_client.set_token(token)
    user_id = auth_api_client.get("/users/profile").json()["data"]["id"]
    return user_id


# Generators

@pytest.fixture
def create_notes(auth_api_client):
    def _create(amount):
        notes = []
        for _ in range(amount):
            note = CreateNoteBuilder().random_title().random_description().random_category().build()
            response = auth_api_client.post("/notes", note.model_dump())
            notes.append(response.json()["data"])
        return notes

    return _create


# Builders

@pytest.fixture
def login_user_builder():
    return LoginUserBuilder()


@pytest.fixture
def register_user_builder():
    return RegisterUserBuilder()


@pytest.fixture
def update_profile_builder():
    return UpdateProfileBuilder()


@pytest.fixture
def create_note_builder():
    return CreateNoteBuilder()


@pytest.fixture
def update_note_builder():
    return UpdateNoteBuilder()


@pytest.fixture
def update_note_complete_status_builder():
    return UpdateNoteCompleteStatusBuilder()
