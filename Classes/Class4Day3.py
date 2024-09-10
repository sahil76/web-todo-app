

while True:
    # Get user input and strip and space characters from it
    user_action = input("Type add, show, edit, complete or exit:").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("../todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)
            # file = open("todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            with open("../todos.txt", "w") as file:
                file.writelines(todos)
        case 'show':
            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("../todos.txt", "r") as file:
                todos = file.readlines()

            # new_todos = []
            #
            # for todo in todos:
            #     new_item = todo.strip("\n")
            #     new_todos.append(new_item)

            # new_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(index+1, item)
        case 'edit':
            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("../todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Enter the number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            # file = open("todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            with open("../todos.txt", "w") as file:
                file.writelines(todos)

        case 'complete':
            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            with open("../todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Number of the todo to complete: "))
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            # file = open("todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            with open("../todos.txt", "w") as file:
                file.writelines(todos)

            message = f"The todo {todo_to_remove} is removed"

            print(message)

        case 'exit':
            break
        case _:
            print("You entered an unknown command!")