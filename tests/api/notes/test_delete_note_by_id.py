import pytest

TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Note successfully deleted",

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
def test_delete_note_by_id(api_client, auth_api_client, create_notes, case):
    note = create_notes(1)[0]

    if case["auth"]:
        client = auth_api_client
    else:
        client = api_client

    response = client.delete(f"/notes/{note['id']}")
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]
