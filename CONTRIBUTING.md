# Contributing to LPS

We welcome contributions to the Layered Publishing System! This guide will help you get started.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/aRcHmaGe333/LPS.git
   cd LPS
   ```

2. **Run the setup script**
   ```bash
   ./scripts/setup.sh
   ```

3. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

4. **Start the development server**
   ```bash
   python -m lps.main
   ```

## Development Workflow

### Code Style

We use the following tools to maintain code quality:

- **Black** - Code formatting
- **isort** - Import sorting  
- **flake8** - Linting
- **mypy** - Type checking

Run all checks:
```bash
black .
isort .
flake8 .
mypy lps
```

### Testing

We use pytest for testing:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=lps

# Run specific test file
pytest tests/test_api.py

# Run specific test
pytest tests/test_api.py::TestAuthEndpoints::test_demo_login
```

### Pre-commit Hooks

Install pre-commit hooks to automatically check code before commits:

```bash
pre-commit install
```

## Project Structure

```
LPS/
├── lps/                    # Main application code
│   ├── api/               # REST API endpoints
│   │   └── v1/           # API version 1
│   │       ├── endpoints/ # Individual endpoint modules
│   │       └── router.py  # Main API router
│   ├── core/              # Core functionality
│   │   ├── config.py      # Configuration management
│   │   └── logging.py     # Logging setup
│   ├── models/            # Data models (SQLAlchemy)
│   ├── services/          # Business logic services
│   ├── utils/             # Utility functions
│   ├── cli.py             # Command line interface
│   └── main.py            # Application entry point
├── tests/                 # Test suite
├── docs/                  # Documentation
├── scripts/               # Setup and utility scripts
├── docker/                # Docker configurations
└── examples/              # Example implementations
```

## Contributing Guidelines

### 1. Fork and Clone

Fork the repository on GitHub and clone your fork locally.

### 2. Create a Branch

Create a feature branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes

- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass

### 4. Commit Messages

Use clear, descriptive commit messages:
```
feat: add user authentication system
fix: resolve pagination bug in content API
docs: update API documentation
test: add tests for workflow endpoints
```

### 5. Submit a Pull Request

1. Push your branch to your fork
2. Create a pull request on GitHub
3. Describe your changes clearly
4. Reference any related issues

## Code Guidelines

### Python Style

- Follow PEP 8
- Use type hints
- Write docstrings for all functions and classes
- Keep functions small and focused
- Use descriptive variable names

### API Design

- Follow RESTful conventions
- Use appropriate HTTP status codes
- Include comprehensive error handling
- Document all endpoints
- Maintain backward compatibility

### Database

- Use SQLAlchemy ORM
- Write database migrations
- Follow naming conventions
- Add indexes for performance

### Testing

- Write unit tests for all functions
- Add integration tests for API endpoints
- Use meaningful test names
- Test both success and error cases
- Aim for high test coverage

## Documentation

- Update README.md for significant changes
- Add docstrings to all Python code
- Update API documentation in `docs/api.md`
- Include examples in documentation
- Keep documentation current with code changes

## Issue Reporting

When reporting issues:

1. Use a clear, descriptive title
2. Provide steps to reproduce the problem
3. Include error messages and stack traces
4. Specify your environment (OS, Python version, etc.)
5. Check if the issue already exists

## Feature Requests

For new features:

1. Describe the feature clearly
2. Explain the use case and benefits
3. Consider the impact on existing functionality
4. Be open to discussion and feedback

## Security

- Never commit secrets or sensitive data
- Report security vulnerabilities privately
- Follow secure coding practices
- Keep dependencies updated

## Getting Help

- Read the documentation first
- Search existing issues
- Ask questions in discussions
- Join our community channels

## Recognition

Contributors will be recognized in:

- The CONTRIBUTORS.md file
- Release notes for significant contributions
- The project README

Thank you for contributing to LPS! 🎉