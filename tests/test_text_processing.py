from src.text_utils import (
    normalize_text,
    reverse_text,
    word_count,
    uppercase_text,
    character_count,
    contains_word,
)

def test_contains_word_empty_word():
    assert contains_word(
        "hello world",
        "",
    ) is False

def test_uppercase_text_empty_string():
    assert uppercase_text("") == ""
