import ast
FILE_SECURE = "container.txt"


def to_open(file_def=FILE_SECURE):
    with open(file_def, "r") as file:
        dict_string = file.read()
        dictionary = ast.literal_eval(dict_string)
        return dictionary


def to_close(var_dict, file_def=FILE_SECURE):
    with open(file_def, "w") as file:
        dict_str = str(var_dict)
        file.write(dict_str)

