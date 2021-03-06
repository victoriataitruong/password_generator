# import libraries
import random
import string
import pyperclip
import PySimpleGUI as sg

sg.theme("Darkbrown")
# defining the window's contents
layout = [[sg.Text("Random Password Generator", font=("Helvetica", 25, "bold"))],
          [sg.Text("Select Password Length", key='-OUTPUT1-', font=("Helvetica", 10, "bold"))],
          [sg.Spin([i for i in range(1, 11)], initial_value=1,
                   size=(30, 4), key='-INPUT-')],
          #   [sg.Input(key='-INPUT-' "sd")],
          [sg.Text(size=(40, 1), key='-OUTPUT-', font=("Helvetica", 25, "bold"))],
          [sg.Button('Generate', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")),
           sg.Button('Copy', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")
                     # defining the window's contents
                     ), sg.Button('Quit', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold"))]]

window = sg.Window('Victorias Password Generator', layout)

# display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    if event == 'Generate':
        useript = values['-INPUT-']
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all, useript)
        password = "".join(temp)
        print(password)
        sg.popup(password)
        window['-OUTPUT-'].update(password)

        window["-INPUT-"].update("1")

    if event == "Copy":
        op = window['-OUTPUT-'].get()
        pyperclip.copy(op)
        ####  Output a message to the window
        sg.popup("Password is copied to your clipboard")

    # see if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

# finish up by removing from the screen
window.close()