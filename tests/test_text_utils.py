from src.text_utils import normalize_text, reverse_text, word_count


def test_normalize_text():
    assert normalize_text("  hello   world  ") == "hello world"


def test_reverse_text():
    assert reverse_text("hello") == "olleh"


def test_word_count():
    assert word_count("hello world") == 2

def test_word_count_empty_string():
    assert word_count("") == 0
