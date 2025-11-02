import pytest
import webservice
from fastapi.testclient import TestClient
from webservice.health import app


@pytest.mark.asyncio
async def test_health_check() -> None:
    # Test the function directly

    result = await webservice.health_check()
    assert result == {"status": "ok"}


@pytest.mark.asyncio
async def test_health_endpoint() -> None:
    # Test the FastAPI endpoint using TestClient (simpler approach)

    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
