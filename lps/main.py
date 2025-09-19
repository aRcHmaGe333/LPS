"""
Main application entry point for LPS.

This module contains the FastAPI application factory and startup/shutdown logic.
"""

import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .api.v1.router import api_router
from .core.config import settings
from .core.logging import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan manager."""
    logger.info("Starting LPS application...")
    
    # Startup logic here
    logger.info("Application startup complete")
    
    yield
    
    # Shutdown logic here
    logger.info("Shutting down LPS application...")
    logger.info("Application shutdown complete")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Layered Publishing System - A comprehensive publishing platform",
        docs_url="/docs" if settings.debug else None,
        redoc_url="/redoc" if settings.debug else None,
        openapi_url="/openapi.json" if settings.debug else None,
        lifespan=lifespan,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=settings.cors_credentials,
        allow_methods=settings.cors_methods,
        allow_headers=settings.cors_headers,
    )

    # Add trusted host middleware for production
    if settings.is_production:
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["*"]  # Configure this properly in production
        )

    # Include API routes
    app.include_router(api_router, prefix=settings.api_v1_prefix)

    # Health check endpoint
    @app.get("/health")
    async def health_check():
        """Health check endpoint."""
        return {
            "status": "healthy",
            "version": settings.app_version,
            "environment": settings.environment,
        }

    # Root endpoint
    @app.get("/")
    async def root():
        """Root endpoint with basic information."""
        return {
            "name": settings.app_name,
            "version": settings.app_version,
            "description": "Layered Publishing System API",
            "docs_url": "/docs" if settings.debug else None,
            "health_url": "/health",
        }

    logger.info(f"FastAPI application created for {settings.app_name} v{settings.app_version}")
    return app


def run_server() -> None:
    """Run the application server."""
    uvicorn.run(
        "lps.main:create_app",
        factory=True,
        host=settings.host,
        port=settings.port,
        reload=settings.reload and settings.is_development,
        log_level=settings.log_level.lower(),
        access_log=True,
    )


if __name__ == "__main__":
    run_server()