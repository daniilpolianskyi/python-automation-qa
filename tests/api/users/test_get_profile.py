import pytest


TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Profile successful",

        "auth": True,
    },
    {
        "name": "unauth",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "No authentication token specified in x-auth-token header",

        "auth": False,
    }
]

@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_get_profile(api_client, auth_api_client, user, case):
    if case["auth"]:
        response = auth_api_client.get("/users/profile")
    else:
        response = api_client.get("/users/profile")
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]

    if case["status_code"] < 400:
        data = body["data"]
        assert "id" in data
        assert data["name"] == user.name
        assert data["email"] == user.email
