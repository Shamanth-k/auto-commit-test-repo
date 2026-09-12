def is_valid_email(email):
    if not isinstance(email, str):
        return False

    if not email:
        return False

    return "@" in email and "." in email.split("@")[-1]


def is_valid_age(age):
    if not isinstance(age, int):
        return False

    return 0 <= age <= 120


def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())