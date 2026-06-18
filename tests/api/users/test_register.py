import pytest

from api.builders.user import RegisterUserBuilder

TEST_CASES = [
    {
        "name": "valid",
        "status_code": 201,
        "success": True,
        "status": 201,
        "message": "User account created successfully",

        "user": lambda: RegisterUserBuilder().random_name().random_email().random_password().build(),
    },
    {
        "name": "without_name_email_password",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "User name must be between 4 and 30 characters",

        "user": lambda: RegisterUserBuilder().build(),
    },
    {
        "name": "without_name",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "User name must be between 4 and 30 characters",

        "user": lambda: RegisterUserBuilder().random_email().random_password().build(),
    },
    {
        "name": "without_email",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "A valid email address is required",

        "user": lambda: RegisterUserBuilder().random_name().random_password().build(),
    },
    {
        "name": "without_password",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "Password must be between 6 and 30 characters",

        "user": lambda: RegisterUserBuilder().random_name().random_email().build(),
    }
]


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_register(api_client, case):
    payload = case["user"]()

    response = api_client.post("/users/register", payload.model_dump())
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]

    if case["status_code"] < 400:
        data = body["data"]
        assert "id" in data
        assert data["name"] == payload.name
        assert data["email"] == payload.email
