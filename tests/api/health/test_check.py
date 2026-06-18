import pytest

TEST_CASES = [
    {
        "name": "health_check",
        "status_code": 200,
        "success": True,
        "status": 200,
        "message": "Notes API is Running"
    }
]


@pytest.mark.parametrize("case", TEST_CASES, ids=lambda case: case["name"])
def test_check(api_client, case):
    response = api_client.get("/health-check")
    assert response.status_code == case["status_code"]

    body = response.json()
    assert body["success"] == case["success"]
    assert body["status"] == case["status"]
    assert body["message"] == case["message"]
