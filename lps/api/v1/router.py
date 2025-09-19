"""
API v1 Router

Main router for API version 1 that includes all endpoint routers.
"""

from fastapi import APIRouter

from .endpoints import (
    auth,
    content,
    layers,
    publications,
    users,
    workflows,
)

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(content.router, prefix="/content", tags=["Content"])
api_router.include_router(layers.router, prefix="/layers", tags=["Layers"])
api_router.include_router(workflows.router, prefix="/workflows", tags=["Workflows"])
api_router.include_router(publications.router, prefix="/publications", tags=["Publications"])