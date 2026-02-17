import secrets
import string

def generate_password(length=16,
                      use_lower=True,
                      use_upper=True,
                      use_digits=True,
                      use_symbols=True):
    
    character_pool = ""

    if use_lower:
        character_pool += string.ascii_lowercase
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(secrets.choice(character_pool) for _ in range(length))

    return password, len(character_pool)
