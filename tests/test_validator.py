from src.validator import (
    is_valid_email,
    is_valid_age,
    is_non_empty_string,
)


def test_valid_email():
    assert is_valid_email("user@example.com")


def test_invalid_email():
    assert not is_valid_email("invalid")


def test_valid_age():
    assert is_valid_age(25)


def test_invalid_age():
    assert not is_valid_age(150)


def test_non_empty_string():
    assert is_non_empty_string("hello")