#!/bin/bash

# LPS Development Environment Setup Script

set -e

echo "🚀 Setting up LPS Development Environment"

# Check if Python 3.11+ is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.11"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION or higher is required. Found: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION detected"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -e ".[dev]"

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs uploads media static

# Create environment file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔐 Creating environment file..."
    cat > .env << EOF
# LPS Environment Configuration
APP_NAME=LPS
APP_VERSION=0.1.0
DEBUG=true
ENVIRONMENT=development

# API Configuration
HOST=0.0.0.0
PORT=8000
API_V1_PREFIX=/api/v1

# Security
SECRET_KEY=your-secret-key-change-this-in-production-$(date +%s)
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL=postgresql://lps:lps@localhost/lps

# Redis
REDIS_URL=redis://localhost:6379/0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# Logging
LOG_LEVEL=INFO

# File Storage
UPLOAD_DIR=uploads
MAX_FILE_SIZE=10485760

# CORS
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]
EOF
fi

# Check if Docker is available
if command -v docker &> /dev/null; then
    echo "🐳 Docker detected - you can use docker-compose for full environment"
    echo "   Run: docker-compose up -d"
else
    echo "⚠️  Docker not found - you'll need to set up PostgreSQL and Redis manually"
fi

echo ""
echo "🎉 LPS development environment setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Start the development server: python -m lps.main"
echo "3. Or use the CLI: lps serve"
echo "4. Visit http://localhost:8000/docs for API documentation"
echo ""
echo "For Docker setup:"
echo "1. docker-compose up -d"
echo "2. Visit http://localhost:8000"