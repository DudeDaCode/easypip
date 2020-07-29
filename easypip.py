import os
import tkinter as tk

root= tk.Tk()

root.wm_title("easypip")

canvas1 = tk.Canvas(root, width = 300, height = 100, bg = '#e9d700', relief = 'raised')
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(100, 50, window=entry1)

def installPackage ():
    package = entry1.get()
    os.system(f'start cmd /k pip install {package}') 
    
button1 = tk.Button(text='      Install      ', command=installPackage, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(225, 50, window=button1)

root.mainloop()
