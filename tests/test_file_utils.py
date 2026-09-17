from src.file_utils import (
    file_exists,
    read_text_file,
    write_text_file,
    get_file_size,
    get_file_size_mb,
    get_parent_directory,
    get_absolute_path,
    read_text_lines,
    get_file_size_kb,
    is_file_empty,
)


def test_file_exists(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert file_exists(str(file))


def test_file_does_not_exist(tmp_path):
    file = tmp_path / "missing.txt"

    assert not file_exists(str(file))


def test_read_text_file(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert read_text_file(str(file)) == "hello"


def test_write_text_file(tmp_path):
    file = tmp_path / "example.txt"

    write_text_file(str(file), "hello")

    assert file.read_text(encoding="utf-8") == "hello"


def test_get_file_size(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert get_file_size(str(file)) == 5

def test_get_file_size_mb(tmp_path):
    file = tmp_path / "data.bin"

    file.write_bytes(
        b"a" * (1024 * 1024)
    )

    assert get_file_size_mb(
        str(file)
    ) == 1.0

def test_get_parent_directory():
    assert get_parent_directory(
        "reports/data.csv"
    ) == "reports"

def test_get_absolute_path():
    from pathlib import Path

    result = get_absolute_path("example.txt")
    assert Path(result).is_absolute()

def test_read_text_lines(tmp_path):
    file = tmp_path / "lines.txt"

    file.write_text(
        "first\nsecond\nthird\n",
        encoding="utf-8",
    )

    assert read_text_lines(str(file)) == [
        "first",
        "second",
        "third",
    ]

def test_get_file_size_kb(tmp_path):
    file = tmp_path / "data.bin"

    file.write_bytes(
        b"a" * 2048
    )

    assert get_file_size_kb(
        str(file)
    ) == 2.0

def test_is_file_empty(tmp_path):
    empty_file = tmp_path / "empty.txt"
    content_file = tmp_path / "content.txt"

    empty_file.write_text("", encoding="utf-8")
    content_file.write_text("data", encoding="utf-8")

    assert is_file_empty(str(empty_file)) is True
    assert is_file_empty(str(content_file)) is False
