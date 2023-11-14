import PySimpleGUI as sg
import json
sg.set_options(font=("vardana"))
#2 layout
layout=[
    [sg.Text('enter word'), sg.InputText(size=(24,14), key='-W-'), sg.Button('Go')],
    [sg.Multiline(50,20 ,disabled=True, key='-OUT-')]
]
#3 window

window=sg.Window('Dictionary', layout)

#4 events, values,loop

while True:
    event, values=window.read()
    if event== sg.WIN_CLOSED:
        break
    if event == 'Go':
       w = values['-W-'].lower()
       total=[]
       with open('dict.json', 'r') as f:
           data=json.load(f)
           for i,j in data.items():
                if i==w:
                    total.append(j)


       if len(total) > 0:
           window['-OUT-'].update(j)
       else:
           window['-OUT-'].update("nothing found")


#close
window.close()
