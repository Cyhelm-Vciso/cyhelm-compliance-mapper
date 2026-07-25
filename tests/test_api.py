from fastapi.testclient import TestClient

from cyhelm.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_filter_mapping():
    response = client.get("/v1/mappings", params={"framework": "ISO27001", "control": "A.5.9"})
    assert response.status_code == 200
    assert response.json()[0]["target_control"] == "ID.AM-01"


def test_missing_mapping_is_404():
    assert client.get("/v1/mappings/ISO27001/unknown").status_code == 404
