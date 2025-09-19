"""
LPS - Layered Publishing System

A comprehensive, scalable publishing platform that supports multiple content layers,
approval workflows, and distribution channels.
"""

__version__ = "0.1.0"
__author__ = "LPS Team"
__email__ = "team@lps.dev"
__description__ = "Layered Publishing System - A comprehensive publishing platform"

from .core.config import settings
from .core.logging import setup_logging

# Initialize logging when the package is imported
setup_logging()

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__description__",
    "settings",
    "setup_logging",
]