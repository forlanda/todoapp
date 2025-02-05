from globals import *


def get_todos(filename=todos_filename):
    """
    Gets the list of todo items
    :param filename: name of the file that contains the todo list
    :return: returns the todo list.
    """
    with open(filename, "r") as file:
        line_list = file.readlines()
    return line_list


def get_todos_str():
    the_list = get_todos()
    the_list_str = ""
    for i, item in the_list:
        the_list_str += f"{i+1} - {item}\n"
    return the_list_str


def save_todos(the_list, filename=todos_filename):
    """
    Saves todo items into a file
    :param filename: this is the filename of the todo list
    :param the_list: this is a list of todo items
    :return: none
    """
    with open(filename, 'w') as file:
        file.writelines(the_list)


def get_command(cmd_list):
    """
    Gets a string of commands which is used for the command prompt.
    :param cmd_list: is a copy of the command list
    :return: a concatenated string os commands
    """
    cmd_strings = ""
    for cmd in cmd_list:
        cmd_strings += f"{cmd} | "
    while True:
        user_action = input(f"{cmd_strings} -->  ")
        if user_action:
            return user_action
        else:
            print("Didn't see a command.")


def show_todos(the_list):
    """
    Shows the list of items stripped of white characters

    :param the_list: is a list type, defaults to 'todos'
    :return: none
    """
    for i, todo in enumerate(the_list):
        print(f"{i + 1} - {todo.strip()}")

def add_todo(the_list, todo):
    the_list.append(f"{todo.capitalize()}\n")
    save_todos(the_list)


def done_todo(the_list, todo):
    try:
        if todo in range(len(the_list)):
            the_list.pop(todo)
            save_todos(the_list)
    except ValueError:
        pass


def todo_exists(the_list, todo):
    try:
        if todo in range(len(the_list)):
            return True
        else:
            return False
    except ValueError:
        pass