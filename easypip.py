import PySimpleGUI as sg
import os

sg.theme('Reddit')  # Add some color to the window

layout = [
    [sg.InputText('', size=(37,1), key='input_value')],
    [sg.InputOptionMenu(('Install Package', 'Install From VCS', 'Install From Requirements', 'Install From File', 'Install From Source',
                         'Make Package', 'Upgrade Package'), size=(32,1), key='-OPTION-')],
    [sg.Submit(size=(32,1))],]

window = sg.Window('Easy Pip', layout)
event, values = window.read()
    
def installPackage ():
    os.system(f'start cmd /k pip install {value}')

def installFromVCS ():
    os.system(f'start cmd /k python -m pip install {value}')

def installFromRequirements ():
    os.system(f'start cmd /k pip install -r {value}')

def installFromFile ():
    os.system(f'start cmd /k pip install {value}')

def installFromSource ():
    os.system(f'start cmd /k pip install {value}')

def makePackage ():
    os.chdir(f'{value}')
    os.system(f'start cmd /k python setup.py sdist bdist_wheel')

def upgradePackage ():
    os.system(f'start cmd /k pip install --upgrade {value}')

if event == 'Submit':
    value = values['input_value']
    option = values['-OPTION-']

if option == 'Install Package' :
    installPackage()

if option == 'Install From VCS' :
    installFromVCS()

if option == 'Install From File' :
    installFromFile()

if option == 'Install From Requirements' :
    installFromRequirements()

if option == 'Install From Source' :
    installFromSource()

if option == 'Make Package' :
    makePackage()

if option == 'Upgrade Package' :
    upgradePackage()


window.close()
