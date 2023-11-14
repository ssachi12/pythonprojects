import PySimpleGUI as sg
# 1st layout

layout=[
    [sg.Text('height in meters'),sg.Input(key='-H-'),sg.Text('Weight in kg'), sg.Input(key='-W-')],
    [sg.Button('ok'),sg.Button('Cancel')],
    sg.Text(key='-OUT-')
]

#3 - Window
window =sg.Window('My ago', layout)

#event loop
while True:
    event, values= window.read()
    if event ==sg.WIN_CLOSED or event == 'Cancel':
        break
    if event== 'ok':
       h=float(values['-H-'])
       w=float(values['-W-'])
       bmi = round(w/h,2)

       window['-OUT-'].update(f"your bmi is{bmi}")
#close
window.close()