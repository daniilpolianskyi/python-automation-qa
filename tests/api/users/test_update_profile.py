import pytest

from api.builders.profile import UpdateProfileBuilder

TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Profile updated successful",

        "auth": True,
        "profile": lambda: UpdateProfileBuilder().random_name().random_phone().random_company().build(),
    },
    {
        "name": "unauth",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "No authentication token specified in x-auth-token header",

        "auth": False,
        "profile": lambda: UpdateProfileBuilder().random_name().random_phone().random_company().build(),
    },
    {
        "name": "valid",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Profile updated successful",

        "auth": True,
        "profile": lambda: UpdateProfileBuilder().random_name().random_phone().random_company().build(),
    },
    {
        "name": "without_name_phone_company",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "User name must be between 4 and 30 characters",

        "auth": True,
        "profile": lambda: UpdateProfileBuilder().without_name().without_phone().without_company().build(),
    },
    {
        "name": "without_name",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "User name must be between 4 and 30 characters",

        "auth": True,
        "profile": lambda: UpdateProfileBuilder().without_name().random_phone().random_company().build(),
    },
    {
        "name": "without_phone",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Profile updated successful",

        "auth": True,
        "profile": lambda: UpdateProfileBuilder().random_name().without_phone().random_company().build(),
    },
    {
        "name": "without_company",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Profile updated successful",

        "auth": True,
        "profile": lambda: UpdateProfileBuilder().random_name().random_phone().without_company().build(),
    },
    {
        "name": "without_phone_company",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Profile updated successful",

        "auth": True,
        "profile": lambda: UpdateProfileBuilder().random_name().without_phone().without_company().build(),
    },
]


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_update_profile(api_client, auth_api_client, case):
    payload = case["profile"]()

    if case["auth"]:
        response = auth_api_client.patch("/users/profile", payload.model_dump())
    else:
        response = api_client.patch("/users/profile", payload.model_dump())
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]

    if case["status_code"] < 400:
        data = body["data"]
        assert "id" in data
        assert data["name"] == payload.name
        assert data["phone"] == payload.phone
        assert data["company"] == payload.company
