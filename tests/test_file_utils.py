from src.file_utils import (
    file_exists,
    read_text_file,
    write_text_file,
    get_file_size,
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