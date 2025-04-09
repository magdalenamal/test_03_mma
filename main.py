from notatnik import add_user
from utils.model import users
from utils.controller import get_user_info


def main():
        while True:
                print("=====MENU=====")
                print("0 - Zakończ program")
                print("1 - Wyświetl znajomych")
                print("2 - Dodaj znajomego")
                print("==============")

                choice = input("Wybierz opcję Menu")
                if choice == "0":break
                if choice == "1":get_user_info(users[1:])
                if choice == "2":add_user(users)

if __name__ == '__main__':
    main()