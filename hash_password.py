import bcrypt

def hash_password(str:str):
    byte = str.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte, salt)
    return hashed


if __name__ == '__main__':
    password = input()
    print(hash_password(password))