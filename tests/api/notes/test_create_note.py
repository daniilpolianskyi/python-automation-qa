import pytest

from api.builders.note import CreateNoteBuilder

TEST_CASES = [
    {
        "name": "auth",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Note successfully created",

        "auth": True,
        "note_build": lambda: CreateNoteBuilder().random_title().random_description().random_category().build(),
    },
    {
        "name": "unauth",
        "status_code": 401,
        "success": False,
        "status": 401,
        "message": "No authentication token specified in x-auth-token header",

        "auth": False,
        "note_build": lambda: CreateNoteBuilder().random_title().random_description().random_category().build(),
    },
    {
        "name": "valid",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Note successfully created",

        "auth": True,
        "note_build": lambda: CreateNoteBuilder().random_title().random_description().random_category().build(),
    },
    {
        "name": "without_title_description_category",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "Title must be between 4 and 100 characters",

        "auth": True,
        "note_build": lambda: CreateNoteBuilder().without_title().without_description().without_category().build(),
    },
    {
        "name": "without_title",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "Title must be between 4 and 100 characters",

        "auth": True,
        "note_build": lambda: CreateNoteBuilder().without_title().random_description().random_category().build(),
    },
    {
        "name": "without_description",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "Description must be between 4 and 1000 characters",

        "auth": True,
        "note_build": lambda: CreateNoteBuilder().random_title().without_description().random_category().build(),
    },
    {
        "name": "without_category",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "Category must be one of the categories: Home, Work, Personal",

        "auth": True,
        "note_build": lambda: CreateNoteBuilder().random_title().random_description().without_category().build(),
    },
    {
        "name": "with_invalid_category",
        "status_code": 400,
        "success": False,
        "status": 400,
        "message": "Category must be one of the categories: Home, Work, Personal",

        "auth": True,
        "note_build": lambda: CreateNoteBuilder().random_title().random_description().invalid_category().build(),
    }
]


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_create_note(api_client, auth_api_client, user_id, case):
    note = case["note_build"]()

    if case["auth"]:
        client = auth_api_client
    else:
        client = api_client

    response = client.post("/notes", note.model_dump())
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["message"] == case["message"]

    if case["status_code"] < 400:
        data = body["data"]
        assert "id" in data
        assert data["title"] == note.title
        assert data["description"] == note.description
        assert data["category"] == note.category
        assert data["completed"] == False
        assert "created_at" in data
        assert "updated_at" in data
        assert data["user_id"] == user_id
