"""Test API endpoints."""

import pytest
from fastapi.testclient import TestClient


class TestAuthEndpoints:
    """Test authentication endpoints."""

    def test_login_endpoint_exists(self, client: TestClient):
        """Test that login endpoint exists."""
        response = client.post("/api/v1/auth/token", data={
            "username": "test",
            "password": "test"
        })
        # Should not return 404
        assert response.status_code != 404

    def test_demo_login(self, client: TestClient):
        """Test demo login functionality."""
        response = client.post("/api/v1/auth/token", data={
            "username": "demo",
            "password": "demo"
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_invalid_login(self, client: TestClient):
        """Test invalid login credentials."""
        response = client.post("/api/v1/auth/token", data={
            "username": "invalid",
            "password": "invalid"
        })
        assert response.status_code == 401


class TestContentEndpoints:
    """Test content management endpoints."""

    def test_list_content(self, client: TestClient):
        """Test list content endpoint."""
        response = client.get("/api/v1/content/")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data

    def test_get_content_not_found(self, client: TestClient):
        """Test get content with non-existent ID."""
        response = client.get("/api/v1/content/nonexistent")
        assert response.status_code == 200  # Returns "not implemented" message
        data = response.json()
        assert data["status"] == "not_implemented"


class TestLayerEndpoints:
    """Test layer management endpoints."""

    def test_list_layers(self, client: TestClient):
        """Test list layers endpoint."""
        response = client.get("/api/v1/layers/")
        assert response.status_code == 200
        data = response.json()
        assert "example_layers" in data
        assert len(data["example_layers"]) == 5


class TestWorkflowEndpoints:
    """Test workflow endpoints."""

    def test_list_workflows(self, client: TestClient):
        """Test list workflows endpoint."""
        response = client.get("/api/v1/workflows/")
        assert response.status_code == 200
        data = response.json()
        assert "example_workflows" in data
        assert len(data["example_workflows"]) == 3


class TestPublicationEndpoints:
    """Test publication endpoints."""

    def test_list_publications(self, client: TestClient):
        """Test list publications endpoint."""
        response = client.get("/api/v1/publications/")
        assert response.status_code == 200

    def test_list_distribution_channels(self, client: TestClient):
        """Test list distribution channels endpoint."""
        response = client.get("/api/v1/publications/channels")
        assert response.status_code == 200
        data = response.json()
        assert "example_channels" in data
        assert len(data["example_channels"]) == 4

    def test_analytics_overview(self, client: TestClient):
        """Test analytics overview endpoint."""
        response = client.get("/api/v1/publications/analytics/overview")
        assert response.status_code == 200
        data = response.json()
        assert "example_overview" in data