def password_check(password):
    if len(password) >= 8 and any(i.isdigit() for i in password) and any(i.isupper() for i in password):
        return True
    else:
        return False

