import pytest

from ui.builders.user import LoginUserBuilder

TEST_CASES = [
    {
        "name": "valid",
        "user_build": lambda: LoginUserBuilder().valid_username().valid_password().build(),
        "url": "/secure",
        "message": "You logged into a secure area!",
        "is_logout_btn_visible": True,
    },
    {
        "name": "invalid_username",
        "user_build": lambda: LoginUserBuilder().random_username().valid_password().build(),
        "url": "/login",
        "message": "Your username is invalid!",
        "is_logout_btn_visible": False,
    },
    {
        "name": "invalid_password",
        "user_build": lambda: LoginUserBuilder().valid_username().random_password().build(),
        "url": "/login",
        "message": "Your password is invalid!",
        "is_logout_btn_visible": False,
    },
    {
        "name": "without_username_password",
        "user_build": lambda: LoginUserBuilder().without_username().without_password().build(),
        "url": "/login",
        "message": "Your username is invalid!",
        "is_logout_btn_visible": False,
    },
    {
        "name": "without_username",
        "user_build": lambda: LoginUserBuilder().without_username().valid_password().build(),
        "url": "/login",
        "message": "Your username is invalid!",
        "is_logout_btn_visible": False,
    },
    {
        "name": "without_password",
        "user_build": lambda: LoginUserBuilder().valid_username().without_password().build(),
        "url": "/login",
        "message": "Your password is invalid!",
        "is_logout_btn_visible": False,
    },
]

@pytest.mark.parametrize(
    "case",
    TEST_CASES,
    ids=lambda case: case["name"]
)
def test_login(page, login_page, case):
    login_page.open()
    user = case["user_build"]()
    login_page.login(user)

    assert case["url"] in page.url
    assert login_page.get_message_text() == case["message"]
    assert login_page.logout_btn.is_visible() == case["is_logout_btn_visible"]
