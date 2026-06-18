import pytest


TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Account successfully deleted",

        "auth": True
    },
    {
        "name": "unauth",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "No authentication token specified in x-auth-token header",

        "auth": False
    }
]

@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_delete_user(api_client, auth_api_client, case):
    if case["auth"] is True:
        response = auth_api_client.delete("/users/delete-account")
    else:
        response = api_client.delete("/users/delete-account")
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]
