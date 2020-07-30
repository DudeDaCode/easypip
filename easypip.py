import os
import tkinter as tk

root= tk.Tk()

root.wm_title("easypip")

canvas1 = tk.Canvas(root, width = 200, height = 450, bg = '#FFD43B', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='easypip v1.4', bg = '#FFD43B')
label1.config(font=('calibri', 10))
canvas1.create_window(100, 25, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(100, 50, window=entry1)

def installPackage ():
    package = entry1.get()
    os.system(f'start cmd /k pip install {package}')

def installFromVCS ():
    link = entry1.get()
    os.system(f'start cmd /k python -m pip install {link}')

def installFromRequirements ():
    textfile = entry1.get()
    os.system(f'start cmd /k pip install -r {textfile}')

def installFromFile ():
    directory = entry1.get()
    os.system(f'start cmd /k pip install {directory}')

def installFromSource ():
    sourcedir = entry1.get()
    os.system(f'start cmd /k pip install {sourcedir}')

def makePackage ():
    packagedir = entry1.get()
    os.chdir(f'{packagedir}')
    os.system(f'start cmd /k python setup.py sdist bdist_wheel')

def upgradePackage ():
    upackage = entry1.get()
    os.system(f'start cmd /k pip install --upgrade {upackage}')


    
button1 = tk.Button(text='      Install      ', command=installPackage, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=button1)

button2 = tk.Button(text='      Link     ', command=installFromVCS, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 150, window=button2)

button3 = tk.Button(text='      Text     ', command=installFromRequirements, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 200, window=button3)

button4 = tk.Button(text='      From Archive     ', command=installFromFile, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 250, window=button4)

button5 = tk.Button(text='      From Source     ', command=installFromSource, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 300, window=button5)

button6 = tk.Button(text='      Make Package     ', command=makePackage, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 350, window=button6)

button7 = tk.Button(text='      Upgrade     ', command=upgradePackage, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 400, window=button7)


root.mainloop()
