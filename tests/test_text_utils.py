from src.file_utils import (
    file_exists,
    read_text_file,
    write_text_file,
    get_file_size,
    get_file_extension,
    safe_read_text_file,
    get_file_name,
)


def test_file_exists(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert file_exists(str(file)) is True


def test_file_does_not_exist(tmp_path):
    file = tmp_path / "missing.txt"

    assert file_exists(str(file)) is False


def test_read_text_file(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello world", encoding="utf-8")

    assert read_text_file(str(file)) == "hello world"


def test_write_text_file(tmp_path):
    file = tmp_path / "example.txt"

    write_text_file(str(file), "hello world")

    assert file.read_text(encoding="utf-8") == "hello world"


def test_get_file_size(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert get_file_size(str(file)) == 5


def test_get_file_extension(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert get_file_extension(str(file)) == ".txt"


def test_get_file_extension_python(tmp_path):
    file = tmp_path / "example.py"
    file.write_text("print('hello')", encoding="utf-8")

    assert get_file_extension(str(file)) == ".py"


def test_safe_read_existing_file(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert safe_read_text_file(str(file)) == "hello"


def test_safe_read_missing_file(tmp_path):
    file = tmp_path / "missing.txt"

    assert safe_read_text_file(
        str(file),
        default="fallback",
    ) == "fallback"


def test_get_file_name(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert get_file_name(str(file)) == "example.txt"


def test_get_file_name_nested_path(tmp_path):
    file = tmp_path / "data.json"
    file.write_text("{}", encoding="utf-8")

    assert get_file_name(str(file)) == "data.json"