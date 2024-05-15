import bcrypt


def hash_password(str:str):
    byte = str.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte, salt)
    return hashed


def check_password(password: str, hashed_password: str):
    bpassword = password.encode("utf-8")
    bhpassword = hashed_password.encode("utf-8")
    if bcrypt.checkpw(bpassword, bhpassword):
        return True
    else:
        return False