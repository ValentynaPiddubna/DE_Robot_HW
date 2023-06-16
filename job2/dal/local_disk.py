import os
from typing import Tuple


def get_directories() -> Tuple[str, str]:
    raw_dir = os.getenv('raw_dir')
    stg_dir = os.getenv('stg_dir')
    return raw_dir, stg_dir
