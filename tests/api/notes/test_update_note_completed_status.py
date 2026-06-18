import pytest

from api.builders.note import UpdateNoteCompleteStatusBuilder

TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Note successfully Updated",

        "auth": True,
        "note": lambda: UpdateNoteCompleteStatusBuilder().set_completed(True).build()
    },
    {
        "name": "unauth",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "No authentication token specified in x-auth-token header",

        "auth": False,
        "note": lambda: UpdateNoteCompleteStatusBuilder().set_completed(True).build()
    }
]


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_update_note_completed_status(api_client, auth_api_client, create_notes, case):
    created_note = create_notes(1)[0]
    note = case["note"]()

    if case["auth"]:
        client = auth_api_client
    else:
        client = api_client

    response = client.patch(f"/notes/{created_note['id']}", note.model_dump())
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]

    if case["status_code"] < 400:
        data = body["data"]
        assert data["completed"] == note.completed
