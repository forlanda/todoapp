import FreeSimpleGUI as sg
import globals
import modules.functions

def get_list_string(the_list):
    list_string = ""
    for index, item in enumerate(the_list):
        list_string += str(index+1) + " - " + item
    return list_string


add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
done_button = sg.Button("Done")
todo_input = sg.InputText()
todo_label = sg.Text("Enter to do:  ")

todos = modules.functions.get_todos()

todo_list_text = get_list_string(todos)
todo_list = sg.Text(todo_list_text,auto_size_text=True, key="-OUTPUT-")
layout = [[todo_label],
          [todo_input,add_button,edit_button,done_button],
          [todo_list]]
window = sg.Window("TODO App",layout)


while True:
    event, x = window.read()
    #show
    window['-OUTPUT-'].update(get_list_string(modules.functions.get_todos()))
    match event:
        case "Add":
            # window['-OUTPUT-'].update("Add clicked")
            if todo_input.get() == "":
                pass
            else:
                modules.functions.add_todo(todos,todo_input.get())
                window['-OUTPUT-'].update(get_list_string(modules.functions.get_todos()))
                todo_input.update("")
        case "Edit":
            window['-OUTPUT-'].update("Edit clicked")
        case "Done":
            try:
                todo = int(todo_input.get())-1
                modules.functions.done_todo(todos,todo)
                window['-OUTPUT-'].update(get_list_string(modules.functions.get_todos()))
                todo_input.update("")
            except ValueError:
                pass
        case sg.WINDOW_CLOSED:
            break
        case _:
            break

window.close()
