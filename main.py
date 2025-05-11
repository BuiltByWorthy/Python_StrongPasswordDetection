import re


def is_strong_password_old(password: str) -> bool:
    #  At least 8 characters.
    if not re.search(r"\w{8,}", password):
        return False

    # Contains uppercase characters.
    if not re.search(r"[A-Z]+", password):
        return False

    # Contains lowercase characters.
    if not re.search(r"[a-z]+", password):
        return False

    # At least one digit.
    if not re.search(r"\d+", password):
        return False

    return True


def is_strong_password(password: str) -> bool:
    return bool(re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}", password))


def determine_password_strength(password: str) -> str:
    return f"Password Strength: {"Strong" if is_strong_password(password) else "Weak"}"


password = input("Enter password > ")
print(determine_password_strength(password))
