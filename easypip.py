import os
import tkinter as tk

root= tk.Tk()

root.wm_title("easypip")

canvas1 = tk.Canvas(root, width = 350, height = 100, bg = '#FFD43B', relief = 'raised')
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(175, 25, window=entry1)

def installPackage ():
    package = entry1.get()
    os.system(f'start cmd /k pip install {package}')

def installFromRepo ():
    link = entry1.get()
    os.system(f'start cmd /k python -m pip install git+{link}')

def installFromRequirements ():
    os.system('pip install -r requirements.txt')
    
button1 = tk.Button(text='      Install      ', command=installPackage, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(65, 75, window=button1)

button2 = tk.Button(text='      Link     ', command=installFromRepo, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(180, 75, window=button2)

button3 = tk.Button(text='      Text     ', command=installFromRequirements, bg='#306998', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(295, 75, window=button3)


root.mainloop()
