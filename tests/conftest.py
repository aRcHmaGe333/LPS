"""Test configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient

from lps.main import create_app
from lps.core.config import settings


@pytest.fixture
def app():
    """Create test application."""
    # Ensure debug mode is enabled for tests
    settings.debug = True
    return create_app()


@pytest.fixture
def client(app):
    """Create test client."""
    return TestClient(app)


@pytest.fixture
def test_user():
    """Create test user data."""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123"
    }


@pytest.fixture
def test_content():
    """Create test content data."""
    return {
        "title": "Test Content",
        "body": "This is test content for the LPS system.",
        "layer_id": "content",
        "status": "draft"
    }