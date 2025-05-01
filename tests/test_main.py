def test_root_route(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert "status" in response.json()
