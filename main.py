from modules.functions import *


todos = get_todos()
while True:
    action = get_command(commands)

    #================================================
    if action[:3] == 'add':
        todo = action[3:].strip()
        if todo == "":
            print("Nothing to add.")
        else:
            print(f"{action[:3].upper()}ing...{todo.capitalize()}")
            todos.append(f"{todo.capitalize()}\n")
            # print(todos)
            save_todos(todos)
            print("Done.")

    # ================================================
    elif action[:4] == 'show':
        print(f"{action[:4].upper()}ing...")
        todos = get_todos()
        show_todos(todos)

    # ================================================
    elif action[:4] == 'edit':
        edit_str = action[4:].strip()
        if edit_str == "":
            print("No todo number found.")
            continue
        else:
            todo_num = int(edit_str) - 1
            new_todo = input("New todo: ")
            todos[todo_num] = f"{new_todo.capitalize()}\n"
            print(f"{action[:4].upper()}ing...")
            save_todos(todos)
            print("Done.")

    #================================================
    elif action[:4] == 'done':
        todo_str = action[4:].strip()
        if todo_str == "":
            print("No todo number found.")
            continue
        else:
            todo_num = int(todo_str) - 1
            todos.pop(todo_num)
            save_todos(todos)

    #================================================
    elif action[:4] == 'exit':
        print(f"{action[:4].upper()}ing...")
        print("Bye bye!")
        break

    # ================================================
    else:
        print("???")
