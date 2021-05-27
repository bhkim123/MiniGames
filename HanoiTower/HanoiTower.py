import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Tower of Hanoi")
window.geometry("500x300")
window.resizable(False, False)
window.config(bg='white')

start_bt = Button(window, text="Game Start", command=lambda: start_click(start_bt))
start_bt.place(relx=0.05, rely=0.05)
start_bt.place(relwidth=0.2, relheight=0.1)

column1 = Canvas(window, width=10, height=130, bg='tan')
column1.place(x=130, y=170)

column2 = Canvas(window, width=10, height=130, bg='tan')
column2.place(x=260, y=170)

column3 = Canvas(window, width=10, height=130, bg='tan')
column3.place(x=390, y=170)

floor = Canvas(window, width=400, height=15, bg='tan')
floor.place(x=50, y=285)




count = 0
ct = Label(window, width=10, height=1, text="count: " + str(count), borderwidth=1, relief='groove')
ct.place(x=400, y=30)

disc1 = Canvas(window, width=90, height=10, bg='black')
disc2 = Canvas(window, width=70, height=10, bg='gray')
disc3 = Canvas(window, width=50, height=10, bg='blue')
disc4 = Canvas(window, width=30, height=10, bg='red')



isStarted = False


def move_disc(d):
    my_label.config(text="coordinates: x-> " + str(d.x) + " y-> " + str(d.y))

my_label = Label(window, text='')
my_label.pack(pady=20)

disc1.bind('<B1-Motion>', move_disc)
disc1.place(relx=0.18, rely=0.91)

disc2.place(relx=0.2, rely=0.87)
disc3.place(relx=0.22, rely=0.83)
disc4.place(relx=0.24, rely=0.79)


def start_click(b):
    global isStarted
    if not isStarted:
        b.config(text="reset")
        isStarted = True


window.mainloop()