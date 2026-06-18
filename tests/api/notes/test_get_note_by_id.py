import pytest

TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Note successfully retrieved",

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
def test_get_note_by_id(api_client, auth_api_client, create_notes, user_id, case):
    note = create_notes(1)[0]

    if case["auth"]:
        client = auth_api_client
    else:
        client = api_client

    response = client.get(f"/notes/{note['id']}")
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]

    if case["status_code"] < 400:
        data = body["data"]
        assert data["id"] == note["id"]
        assert data["title"] == note["title"]
        assert data["description"] == note["description"]
        assert data["category"] == note["category"]
        assert "completed" in data
        assert "created_at" in data
        assert "updated_at" in data
        assert data["user_id"] == user_id
