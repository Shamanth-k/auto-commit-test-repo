"""Text Utils utilities."""

def normalize_text(text):
    return " ".join(text.strip().split())


def reverse_text(text):
    return text[::-1]


def word_count(text):
    normalized = normalize_text(text)

    if not normalized:
        return 0

    return len(normalized.split())