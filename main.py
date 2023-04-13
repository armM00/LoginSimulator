import file_manager
import encryptor
import lgn_checker
import pass_checker

while True:
    welcome = input("You want to login or signup? L/S:  ").lower().strip()

    if welcome != "l" and welcome != "s":
        print(" \nPlease enter L or S ")
        continue

    holy_dictionary = file_manager.to_open()

    user_login = input("Enter your login: ")
    user_password = input("Enter your password: ")

    user_login_encrypted = encryptor.encrypt(user_login)
    user_password_encrypted = encryptor.encrypt(user_password)

    match welcome:
        case "l":   # Login

            if user_login_encrypted not in holy_dictionary or \
                    holy_dictionary[user_login_encrypted] != user_password_encrypted:
                print("Invalid login and/or password. Please try again. \n")
                continue
            else:
                print("You've logged in successfully")
                break

        case "s":   # Sign up
            password_check = pass_checker.password_check(user_password)

            login_check = lgn_checker.login_check(user_login)

            if login_check and password_check:
                holy_dictionary[user_login_encrypted] = user_password_encrypted
                print("You have registered successfully!")
                file_manager.to_close(holy_dictionary)
                break

            elif not password_check:
                print("Password must be at least 8 characters long, and "
                      "contain 1 uppercase,and  1 numeric character.\n")
                continue

            elif not login_check:
                print("The login has been taken. Try with another login.\n")
                continue
