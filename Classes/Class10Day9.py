while True:
    # Get user input and strip and space characters from it
    user_action = input("Type add, show, edit, complete or exit:").strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        with open("../todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("../todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open("../todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(index + 1, item)

    elif user_action.startswith("edit"):

        try:
            with open("../todos.txt", "r") as file:
                todos = file.readlines()

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            with open("../todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            with open("../todos.txt", "r") as file:
                todos = file.readlines()

            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("../todos.txt", "w") as file:
                file.writelines(todos)

            message = f"The todo {todo_to_remove} is removed"

            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")