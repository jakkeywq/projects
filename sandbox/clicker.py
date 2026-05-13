from tkinter import *
import random

root = Tk()
root.geometry('400x300')
root.title('Клікєр')

coins = 0
click_power = 1

level = 0
lvl_up = [
    [10, 2],
    [100, 5],
    [500, 10]
]

label1 = Label(root, text=f'Монеток - {coins}')
label1.place(x=160, y = 100)

def click():
    global coins
    global click_power

    coins += click_power

    label1.config(text=f'Монеток - {coins}')

def upgrade():
    global coins
    global click_power 
    global level
    global lvl_up

    if coins >= lvl_up[level][0]:
        coins -= lvl_up[level][0]
        click_power = lvl_up[level][1]

        level += 1
        label1.config(text=f'Монеток - {coins}')

btn_click = Button(root, text=':)', command=click, width=8)
btn_click.place(anchor=CENTER, y=200, x=200)

btn_upgrade = Button(root, text='Покращити!', command=upgrade)
btn_upgrade.place(anchor=CENTER, y=250, x=200)

root.mainloop()