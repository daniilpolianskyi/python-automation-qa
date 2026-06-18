import pytest

from ui.builders.user import RegisterUserBuilder

TEST_CASES = [
    # {
    #     "name": "random",
    #     "user_build": lambda: RegisterUserBuilder().random_username().random_password().random_confirm_password().build(),
    #     "url": "/login",
    #     "message": "Successfully registered, you can log in now.",
    # },
    {
        "name": "without_username_password_confirm_password",
        "user_build": lambda: RegisterUserBuilder().without_username().without_password().without_confirm_password().build(),
        "url": "/register",
        "message": "All fields are required.",
    },
    {
        "name": "without_username",
        "user_build": lambda: RegisterUserBuilder().without_username().random_password().random_confirm_password().build(),
        "url": "/register",
        "message": "All fields are required.",
    },
    {
        "name": "without_password",
        "user_build": lambda: RegisterUserBuilder().random_username().without_password().random_confirm_password().build(),
        "url": "/register",
        "message": "All fields are required.",
    },
    {
        "name": "without_confirm_password",
        "user_build": lambda: RegisterUserBuilder().random_username().random_password().without_confirm_password().build(),
        "url": "/register",
        "message": "All fields are required.",
    },
    {
        "name": "password_mismatch",
        "user_build": lambda: RegisterUserBuilder().random_username().random_password().mismatch_confirm_password().build(),
        "url": "/register",
        "message": "Passwords do not match.",
    },
]

@pytest.mark.parametrize(
    "case",
    TEST_CASES,
    ids=lambda case: case["name"]
)
def test_register(page, register_page, case):
    register_page.open()
    user = case["user_build"]()
    register_page.register(user)

    assert case["url"] in page.url
    assert register_page.get_message_text() == case["message"]
