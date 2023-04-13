import file_manager

local_dict = file_manager.to_open()


def login_check(login, di=local_dict):
    if login in di:
        return False
    else:
        return True
