import os
import logging
from typing import Optional, List, Dict, Any

logger = logging.getLogger(__name__)

def read_file(file_path: str) -> Optional[str]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except IOError as e:
        logger.error(f"Failed to read file {file_path}: {e}")
        return None

def write_file(file_path: str, content: str) -> bool:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            return True
    except IOError as e:
        logger.error(f"Failed to write to file {file_path}: {e}")
        return False

def get_file_extension(file_path: str) -> Optional[str]:
    _, ext = os.path.splitext(file_path)
    return ext.lower() if ext else None

def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    return {**dict1, **dict2}

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def validate_path(path: str) -> bool:
    return os.path.exists(path)

def create_directory(dir_path: str) -> bool:
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except OSError as e:
        logger.error(f"Failed to create directory {dir_path}: {e}")
        return False