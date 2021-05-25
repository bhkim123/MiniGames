import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

window = tk.Tk()
window.title("TicTacToe")
window.geometry("600x700")
window.resizable(False, False)

# Buttons
start_bt = Button(window, text="Game Start", command=lambda: start_click(start_bt))
start_bt.place(relx=0.4, rely=0.93)
start_bt.place(relwidth=0.2, relheight=0.05)

with_com = IntVar()
multi_play = Checkbutton(window, text="Want to play with computer", variable=with_com, onvalue=1, offvalue=0)
multi_play.place(relx=0.25, rely=0.83)
multi_play.place(relwidth=0.5, relheight=0.1)

bt1 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt1))
bt1.place(x=0, y=0, width=200, height=200)
bt2 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt2))
bt2.place(x=200, y=0, width=200, height=200)
bt3 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt3))
bt3.place(x=400, y=0, width=200, height=200)
bt4 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt4))
bt4.place(x=0, y=200, width=200, height=200)
bt5 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt5))
bt5.place(x=200, y=200, width=200, height=200)
bt6 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt6))
bt6.place(x=400, y=200, width=200, height=200)
bt7 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt7))
bt7.place(x=0, y=400, width=200, height=200)
bt8 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt8))
bt8.place(x=200, y=400, width=200, height=200)
bt9 = Button(window, text="empty", font=("Helvetica", 10), command=lambda: clicked(bt9))
bt9.place(x=400, y=400, width=200, height=200)

# Functions

isStarted = False
isWin = False
click_count = 0


def start_click(b):
    global isStarted
    if not isStarted:
        b.config(text="reset")
        isStarted = True
    else:
        reset()


def clicked(b):
    global isStarted, click_count, isWin, with_com
    if isStarted:
        click_count += 1
        if click_count % 2 == 0:
            b["text"] = "O"
        else:
            b["text"] = "X"
        b["font"] = ("Helvetica", 50)
        b["state"] = tk.DISABLED

        winner = check_win()

        if isWin:
            messagebox.showinfo("TicTacToe", winner + " Win!")
            make_disabled()
            isWin = False
            return
        else:
            check_count()
            if click_count % 2 == 1 and click_count < 8 and with_com.get() == 1:
                random_pick()


def make_disabled():
    global bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9
    buttons = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9]
    for b in buttons:
        b.config(state=tk.DISABLED)


def check_win():
    global bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, isWin
    if bt1["text"] == bt2["text"] == bt3["text"] == "O" or bt1["text"] == bt2["text"] == bt3["text"] == "X":
        isWin = True
        return bt1["text"]
    elif bt4["text"] == bt5["text"] == bt6["text"] == "O" or bt4["text"] == bt5["text"] == bt6["text"] == "X":
        isWin = True
        return bt4["text"]
    elif bt7["text"] == bt8["text"] == bt9["text"] == "O" or bt7["text"] == bt8["text"] == bt9["text"] == "X":
        isWin = True
        return bt7["text"]
    elif bt1["text"] == bt4["text"] == bt7["text"] == "O" or bt1["text"] == bt4["text"] == bt7["text"] == "X":
        isWin = True
        return bt1["text"]
    elif bt2["text"] == bt5["text"] == bt8["text"] == "O" or bt2["text"] == bt5["text"] == bt8["text"] == "X":
        isWin = True
        return bt2["text"]
    elif bt3["text"] == bt6["text"] == bt9["text"] == "O" or bt3["text"] == bt6["text"] == bt9["text"] == "X":
        isWin = True
        return bt3["text"]
    elif bt1["text"] == bt5["text"] == bt9["text"] == "O" or bt1["text"] == bt5["text"] == bt9["text"] == "X":
        isWin = True
        return bt1["text"]
    elif bt3["text"] == bt5["text"] == bt7["text"] == "O" or bt3["text"] == bt5["text"] == bt7["text"] == "X":
        isWin = True
        return bt3["text"]


def random_pick():
    global bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9
    able_buttons = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9]
    empty_bt = []
    for b in able_buttons:
        if b["text"] == "empty":
            empty_bt.append(b)
    num = random.randrange(0, len(empty_bt))
    clicked(empty_bt[num])


def reset():
    global bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9, click_count, isWin
    buttons = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9]
    click_count = 0
    isWin = False
    for b in buttons:
        b.config(text="empty", font=("Helvetica", 10), state=tk.NORMAL)


def check_count():
    global click_count, isWin
    if click_count == 9 and not isWin:
        messagebox.showinfo("TicTacToe", "No winner")
        make_disabled()


window.mainloop()
