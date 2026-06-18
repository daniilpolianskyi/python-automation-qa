import pytest

TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "No notes found",

        "auth": True,
        "notes_amount": None
    },
    {
        "name": "unauth",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "No authentication token specified in x-auth-token header",

        "auth": False,
        "notes_amount": None
    },
    {
        "name": "empty_notes",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "No notes found",

        "auth": True,
        "notes_amount": 0
    },
    {
        "name": "single_note",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Notes successfully retrieved",

        "auth": True,
        "notes_amount": 1
    },
    {
        "name": "multiple_notes",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Notes successfully retrieved",

        "auth": True,
        "notes_amount": 3
    }
]


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_get_notes(api_client, auth_api_client, create_notes, user_id, case):
    if case["notes_amount"]:
        notes = list(reversed(create_notes(case["notes_amount"])))

    if case["auth"]:
        client = auth_api_client
    else:
        client = api_client

    response = client.get("/notes")
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]

    if case["notes_amount"]:
        data = body["data"]
        assert len(data) == case["notes_amount"]
        for n in range(case["notes_amount"]):
            assert data[n]["id"] == notes[n]["id"]
            assert data[n]["title"] == notes[n]["title"]
            assert data[n]["description"] == notes[n]["description"]
            assert data[n]["category"] == notes[n]["category"]
            assert "completed" in data[n]
            assert "created_at" in data[n]
            assert "updated_at" in data[n]
            assert data[n]["user_id"] == user_id
