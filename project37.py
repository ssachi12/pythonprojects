import PySimpleGUI as sg
import random

sg.theme('DarkBlue4')   # Add a touch of color
sg.set_options(font='Arial 16')  # Change the font

# All the stuff inside your window.
layout = [ [sg.Push(), sg.Text('Choose an option'), sg.Push()],
           [sg.Button(image_source='rock.jpg', key='rockUser'), sg.Button(image_source='paper.jpg', key='paperUser'),
            sg.Button(image_source='scissors.jpg', key='scissorsUser')],
            [sg.Push(), sg.Image('man.png'), sg.Text('VS'), sg.Image('computer.jpg'), sg.Push()],
           [sg.Push(), sg.Image(key='firstOutput'), sg.Image(key='computerOutput'), sg.Push()],
            [sg.Button('reset')]
          ]

# Create the Window
window = sg.Window('RPS', layout, icon = 'fist.ico')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    # Getting access to clicks and inputs from reading the window
    event, values = window.read()

    # if user closes window
    if event == sg.WIN_CLOSED:
        break

    # A list of options the computer will randomly choose from
    computerOptions = ['rock.png', 'paper.png', 'scissors.png']

    # Choose a random element from the list
    computerOption = random.choice(computerOptions)

    # Update the image in the window with the randomly generated image
    computer = window['computerOutput'].update(computerOption)

    # Checking for the user clicks and updating the user image with the chosen ones
    if event == 'rockUser':
        window['firstOutput'].update('rock.png')
        computer

    if event == 'paperUser':
        window['firstOutput'].update('paper.png')
        computer

    if event == 'scissorsUser':
        window['firstOutput'].update('scissors.png')
        computer

    # Clearing the generated images
    if event == 'reset':
        window['firstOutput'].update('')
        window['computerOutput'].update('')


window.close()