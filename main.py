import json
import time
import utils
from getpass import getpass
global session_user


class Bookshelf:
    __file = "users.json"

    def __read_data(self):
        try:
            with open(self.__file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(self.__file, "w") as f:
                json.dump([], f, indent=3)
                data = []
        self.__users = data

    def __init__(self):
        self.__read_data()

    def __commit(self):
        with open(self.__file, "w") as f:
            json.dump(self.__users, f, indent=3)

    def __check_username_unique(self, username: str) -> bool:
        for user in self.__users:
            if user["username"] == username:
                return False
        else:
            return True

    def email_unique(self, email: str):
        for user in self.__users:
            if user["email"] == email:
                return True
        else:
            return False

    def register(self, username: str, password: str, full_name: str, email: str):
        if self.__check_username_unique(username):
            if self.email_unique(email):
                data = {
                    "id": time.time_ns(),
                    "full_name": full_name,
                    "email": email,
                    "password": password
                }
                hashed_password = utils.hash_password(password)
                data["password"] = str(hashed_password)
                self.__users.append(data)
                self.__commit()
                print("email  successfully registered")
                return True
            print("user successfully registered")
        else:
            print("username already registered")
            return False

    def __check_password(self, password: str, hashed_password: str):
        if utils.check_password(password, hashed_password):
            return True
        else:
            return False

    def __search_user(self, username: str):
        for user in self.__users:
            if user["username"] == username:
                return user
        else:
            return False

    def login(self, username, password) -> dict:
        user = self.__search_user(username)
        if user:
            if self.__check_password(password, user["password"]):
                print("welcome ! ")
                return user
            else:
                print("password wrong")
        else:
            print("user not found")
            self.__commit()


    def add_book(self, id: int, title: str, author: str, page_count: int):
        if id not in self.__users:
            self.__users.append({"id": time.time_ns(), "title": title, "author": author, "page_count": page_count})
            self.__commit()
            print("Book successfully added: ")
        else:
            print("Book already added: ")

    def my_book(self, id):
        for user in self.__users:
            if user["id"] == id:
                print("Id: ", user["id"])
                print("Username: ", user["username"])
                print("Done: ", user["done"])
                self.__users.append(user)
                self.__commit()

    def delete_book(self, id):
        for user in self.__users:
            if user["id"] == id:
                self.__users.remove(user)
                print("Book successfully deleted:")
                break
        else:
            print("you don't have permission")
            self.__commit()


session_user = None

if __name__ == '__main__':
    u = Bookshelf()
    print("login_book --->: ")
    print("register_book ---->: ")
    print("add_book ---->: ")
    print("my_book ---->:")
    print("delete_book --->: ")
    ch = input("choice : ? \n")
    match ch:
        case "login_book":
            username = input("username: ")
            password = getpass("password: ")
            session_user = u.login(username=username, password=password)
        case "register_book":
            username = input("username: ")
            full_name = input("full name: ")
            email = input("email address: ")
            password = getpass()
            u.register(username=username, password=password, full_name=full_name, email=email)
        case "add_book":
            id = time.time_ns()
            title = input("enter your title --->: ")
            author = input("enter your author --->")
            page_count = input("enter your page count --->: ")
            u.add_book(id=time.time_ns(), title=title, author=author, page_count=page_count)
        case "my_book":
            session_user = u.my_book(id=time.time_ns())
        case "delete_book":
            id = input("enter your id --->: ")
            u.delete_book(id=id)
