# utils.py

import os
import re
import logging
from typing import Union, List

def slugify(text: str) -> str:
    """Converts text to a slug."""
    return re.sub(r'\W+', '-', text).lower()

def get_absolute_path(path: str) -> str:
    """Resolves the absolute path of a given path."""
    return os.path.abspath(os.path.join(os.getcwd(), path))

def get_project_root() -> str:
    """Resolves the project root directory."""
    return get_absolute_path('..')

def get_log_level(level: str) -> int:
    """Returns the log level based on the provided string."""
    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    return levels.get(level.upper(), logging.INFO)

def get_logger(name: str, level: str = 'INFO') -> logging.Logger:
    """Returns a logger instance with the specified name and level."""
    logger = logging.getLogger(name)
    logger.setLevel(get_log_level(level))
    return logger

def is_valid_email(email: str) -> bool:
    """Checks if the provided email is valid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password(password: str) -> bool:
    """Checks if the provided password is valid."""
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    return bool(re.match(pattern, password))

def is_empty(value: Union[str, List]) -> bool:
    """Checks if the provided value is empty."""
    return value in [None, '', [], {}, ()]