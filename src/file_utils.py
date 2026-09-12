"""File Utils utilities."""

from pathlib import Path


def file_exists(path: str) -> bool:
    return Path(path).is_file()


def read_text_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write_text_file(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def get_file_size(path: str) -> int:
    return Path(path).stat().st_size