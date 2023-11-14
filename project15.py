import random
import string
import PySimpleGUI as sg


sg.theme('DarkBlue6')
sg.set_options(font='verdana 15')
layout=[
    [sg.Text('Uppercase: '),sg.Push(), sg.Input(size=15, key='-UP-')],
    [sg.Text('lowercase: '),sg.Push(), sg.Input(size=15, key='-LOW-')],
    [sg.Text('digits: '),sg.Push(),sg.Input(size=15 ,key='-DIG-')],
    [sg.Text('symbols: '),sg.Push(), sg.Input(size=15, key='-SYM-')],
    [sg.Button('Ok')],[sg.Button('Cancel')],
    [sg.Text('Password: '),sg.Push(), sg.Multiline(size=15,no_scrollbar=True, disabled=True, key='-PASS-')],
]

window=sg.Window('Password generator', layout)

while True:
    event, value =window.read()
    if event == 'Cancel' or event== sg.WINDOW_CLOSED:
        break
    if event == 'Ok':
        try:
            u_upper=int(value['-UP-'])
            upper = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(value['-LOW-'])
            lower = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(value['-DIG-'])
            digits = random.sample(string.digits, u_digits)
            u_symbols = int(value['-SYM-'])
            symbols = random.sample(string.punctuation, u_symbols)

            total = upper + lower + digits + symbols
            total = random.sample(total, len(total))
            total = ''.join(total)
            window['-PASS-'].update(total)
        except ValueError:
            window['-PASS-'].update("no valid number")


window.close()

