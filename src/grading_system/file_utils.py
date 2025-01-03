import os
from typing import Callable


USE_ONLY_PY_FILES = lambda file_path: file_path.endswith(".py")
EXCLUDE_INIT_FILES = lambda file_path: not file_path.endswith("__init__.py")


def get_files(dir_path: str, file_filters: list[Callable]) -> list[str]:
    if not os.path.isdir(dir_path):
        raise ValueError(f"Указанный путь '{dir_path}' не является директорией или не существует.")

    files = []
    for root, _, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if all([file_filter(file_path) for file_filter in file_filters]):
                files.append(file_path)
    return files


def get_code_lines(file_path: str) -> list[str]:
    if not os.path.isfile(file_path):
        raise ValueError(f"Указанный путь '{file_path}' не является файлом или не существует.")

    with open(file_path, "r", encoding="utf-8") as f:
        code_lines = f.readlines()
    return code_lines
