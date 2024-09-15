FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of todos."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write todos items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")

'''
This here means that the value of __name__ would be "__main__" while we run the
functions script whereas the value of __name__ would be "functions" when we 
call this script in the main file.
'''
