import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Tower of Hanoi")
window.geometry("830x320")
window.resizable(False, False)
window.config(bg='white')

bg_canvas = Canvas(window, width=900, height=300, bg='white')

start_bt = Button(window, text="Game Start", command=lambda: start_click(start_bt))
start_bt.place(relx=0.05, rely=0.05)
start_bt.place(relwidth=0.2, relheight=0.1)

column1 = bg_canvas.create_rectangle(200, 200, 210, 300, fill='tan')
column2 = bg_canvas.create_rectangle(410, 200, 420, 300, fill='tan')
column3 = bg_canvas.create_rectangle(620, 200, 630, 300, fill='tan')
floor = bg_canvas.create_rectangle(0, 300, 900, 320, fill='tan')

count = 0
ct = Label(window, width=15, height=1, text="count: " + str(count), borderwidth=1, relief='groove')
ct.place(relx=0.85, rely=0.05)

bg_canvas.pack()


img1 = PhotoImage(file="1.png")
disc1 = bg_canvas.create_image(0, 0, image=img1)
#disc1 = Label(window, image=img1, bg='black', width=60, height=20).place(x=100, y=100)
#disc2 = Label(window, image=img1, bg='darkorange', width=80, height=20).place(x=90, y=120)
#disc3 = Label(window, image=img1, bg='green', width=100, height=20).place(x=80, y=140)
#disc4 = Label(window, image=img1, bg='darkblue', width=120, height=20).place(x=70, y=160)

isStarted = False


def move_disc(e):
    global img1
    my_label.config(text="coordinates: x-> " + str(e.x) + " y-> " + str(e.y))
    disc1 = bg_canvas.create_image(e.x, e.y, image=img1)


my_label = Label(window, text='')
my_label.pack()

bg_canvas.bind('<B1-Motion>', move_disc)


def start_click(b):
    global isStarted
    if not isStarted:
        b.config(text="reset")
        isStarted = True


window.mainloop()
