import pytest

from api.builders.user import LoginUserBuilder

TEST_CASES = [
    {
        "name": "valid",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Login successful",

        "user_build": lambda user: LoginUserBuilder().email(user.email).password(user.password).build(),
    },
    {
        "name": "invalid_email",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "Incorrect email address or password",

        "user_build": lambda user: LoginUserBuilder().random_email().password(user.password).build(),
    },
    {
        "name": "invalid_password",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "Incorrect email address or password",

        "user_build": lambda user: LoginUserBuilder().email(user.email).random_password().build(),
    },
    {
        "name": "without_email_password",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "A valid email address is required",

        "user_build": lambda user: LoginUserBuilder().build(),
    },
    {
        "name": "without_email",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "A valid email address is required",

        "user_build": lambda user: LoginUserBuilder().password(user.password).build(),
    },
    {
        "name": "without_password",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "Password must be between 6 and 30 characters",

        "user_build": lambda user: LoginUserBuilder().email(user.email).build(),
    }
]


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_login(api_client, user, case):
    payload = case["user_build"](user)

    response = api_client.post("/users/login", payload.model_dump())
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]

    if case["status_code"] < 400:
        data = body["data"]
        assert "id" in data
        assert "name" in data
        assert data["email"] == payload.email
        assert "token" in data
