# from functions import get_todos, write_todos

import functions
import time

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", current_time)
while True:
    # Get user input and strip and space characters from it
    user_action = input("Type add, show, edit, complete or exit:").strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)


    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(index + 1, item)

    elif user_action.startswith("edit"):

        try:

            todos = functions.get_todos()

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"The todo {todo_to_remove} is removed"

            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")
