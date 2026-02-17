import string

def validate_password(password,
                      use_lower,
                      use_upper,
                      use_digits,
                      use_symbols):
    
    if use_lower and not any(c in string.ascii_lowercase for c in password):
        return False
    if use_upper and not any(c in string.ascii_uppercase for c in password):
        return False
    if use_digits and not any(c in string.digits for c in password):
        return False
    if use_symbols and not any(c in string.punctuation for c in password):
        return False

    return True
