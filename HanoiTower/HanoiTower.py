import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tower of Hanoi")
window.geometry("830x320")
window.resizable(False, False)

w = 900
h = 400

bg_canvas = Canvas(window, width=w, height=h, bg='white')

start_bt = Button(window, text="Game Start", command=lambda: start_click(start_bt))
start_bt.place(relx=0.05, rely=0.05)
start_bt.place(relwidth=0.2, relheight=0.1)

column1 = bg_canvas.create_rectangle(200, 150, 210, 300, fill='tan', tag="c1")
column2 = bg_canvas.create_rectangle(410, 150, 420, 300, fill='tan', tag="c2")
column3 = bg_canvas.create_rectangle(620, 150, 630, 300, fill='tan', tag="c3")
floor = bg_canvas.create_rectangle(0, 300, 900, 320, fill='tan', tag="fl")

count = 0
ct = Label(window, width=15, height=1, text="count: " + str(count), borderwidth=1, relief='groove')
ct.place(relx=0.85, rely=0.05)


x_1st = 205
x_2nd = 415
x_3rd = 625

y_top = 210
y_2nd = 235
y_3rd = 260
y_bottom = 285

img1 = PhotoImage(file='1.png')
disc1 = bg_canvas.create_image(x_1st, y_top, image=img1, tag="d1")
img2 = PhotoImage(file='2.png')
disc2 = bg_canvas.create_image(x_1st, y_2nd, image=img2, tag="d2")
img3 = PhotoImage(file='3.png')
disc3 = bg_canvas.create_image(x_1st, y_3rd, image=img3, tag="d3")
img4 = PhotoImage(file='4.png')
disc4 = bg_canvas.create_image(x_1st, y_bottom, image=img4, tag="d4")

b12 = Button(window, text=">", font=("Helvetica", 10), command=lambda: clicked(b12))
b12.place(x=150, y=300, width=50, height=20)
b13 = Button(window, text=">>", font=("Helvetica", 10), command=lambda: clicked(b13))
b13.place(x=210, y=300, width=50, height=20)
b21 = Button(window, text="<", font=("Helvetica", 10), command=lambda: clicked(b21))
b21.place(x=360, y=300, width=50, height=20)
b23 = Button(window, text=">", font=("Helvetica", 10), command=lambda: clicked(b23))
b23.place(x=420, y=300, width=50, height=20)
b31 = Button(window, text="<<", font=("Helvetica", 10), command=lambda: clicked(b31))
b31.place(x=570, y=300, width=50, height=20)
b32 = Button(window, text="<", font=("Helvetica", 10), command=lambda: clicked(b32))
b32.place(x=630, y=300, width=50, height=20)

list_1st = [disc4, disc3, disc2, disc1]
list_2nd = []
list_3rd = []


isStarted = False


def start_click(b):
    global isStarted
    if not isStarted:
        b.config(state=tk.DISABLED)
        isStarted = True


def clicked(b):
    global b12, b13, b21, b23, b31, b32, list_1st, list_2nd, list_3rd, isStarted
    if isStarted:
        if (b == b12 or b == b13) and len(list_1st) > 0:
            top_d = list_1st[-1]
            if b == b12 and ((len(list_2nd) > 0 and compare_disc(top_d, list_2nd[-1])) or len(list_2nd) == 0):
                move_disc(top_d, list_1st, list_2nd)
            elif b == b13 and ((len(list_3rd) > 0 and compare_disc(top_d, list_3rd[-1])) or len(list_3rd) == 0):
                move_disc(top_d, list_1st, list_3rd)
        elif (b == b21 or b == b23) and len(list_2nd) > 0:
            top_d = list_2nd[-1]
            if b == b21 and ((len(list_1st) > 0 and compare_disc(top_d, list_1st[-1])) or len(list_1st) == 0):
                move_disc(top_d, list_2nd, list_1st)
            elif b == b23 and ((len(list_3rd) > 0 and compare_disc(top_d, list_3rd[-1])) or len(list_3rd) == 0):
                move_disc(top_d, list_2nd, list_3rd)
        elif (b == b31 or b == b32) and len(list_3rd) > 0:
            top_d = list_3rd[-1]
            if b == b31 and (len(list_1st) == 0 or (len(list_1st) > 0 and compare_disc(top_d, list_1st[-1]))):
                move_disc(top_d, list_3rd, list_1st)
            elif b == b32 and len(list_2nd) == 0 or (len(list_2nd) > 0 and compare_disc(top_d, list_2nd[-1])):
                move_disc(top_d, list_3rd, list_2nd)
    check_win()


def move_disc(d, dl_from, dl_to):
    global list_1st, list_2nd, list_3rd, disc1, disc2, disc3, disc4, img1, img2, img3, img4, bg_canvas, x_1st, x_2nd, x_3rd, y_top, y_2nd, y_3rd, y_bottom, count, ct
    count += 1
    ct.config(text="count: " + str(count))

    x = 0
    y = 0
    no_fr = len(dl_from)
    no_to = len(dl_to)

    if no_fr == 4:
        y += 75
    elif no_fr == 3:
        if no_to == 0:
            y += 50
        elif no_to == 1:
            y += 25
    elif no_fr == 2:
        if no_to == 0:
            y += 25
        elif no_to == 1:
            y += 0
        elif no_to == 2:
            y -= 25
    elif no_fr == 1:
        if no_to == 0:
            y += 0
        elif no_to == 1:
            y -= 25
        elif no_to == 2:
            y -= 50
        elif no_to == 3:
            y -= 75

    dl_from.remove(d)
    dl_to.append(d)

    if dl_from == list_2nd and dl_to == list_3rd:
        x += 210
    elif dl_from == list_3rd and dl_to == list_2nd:
        x -= 210
    elif dl_from == list_3rd and dl_to == list_1st:
        x -= 420
    elif dl_from == list_1st and dl_to == list_3rd:
        x += 420
    elif dl_from == list_1st and dl_to == list_2nd:
        x += 210
    elif dl_from == list_2nd and dl_to == list_1st:
        x -= 210

    if d == disc1:
        bg_canvas.move(disc1, x, y)
    elif d == disc2:
        bg_canvas.move(disc2, x, y)
    elif d == disc3:
        bg_canvas.move(disc3, x, y)
    elif d == disc4:
        bg_canvas.move(disc4, x, y)


def compare_disc(top, bottom):
    global disc1, disc2, disc3, disc4
    if top == disc1:
        return True
    elif top == disc2 and (bottom != disc1):
        return True
    elif top == disc3 and bottom == disc4:
        return True
    else:
        return False


def check_win():
    if len(list_3rd) == 4:
        messagebox.showinfo("Tower of Hanoi", message='Well done!')
        make_disabled()


def make_disabled():
    global b12, b13, b21, b23, b31, b32
    li = [b12, b13, b21, b23, b31, b32]
    for l in li:
        l.config(state=tk.DISABLED)


def make_able():
    global b12, b13, b21, b23, b31, b32
    buttons = [b12, b13, b21, b23, b31, b32]
    for b in buttons:
        b.config(state=tk.NORMAL)


bg_canvas.pack()
window.mainloop()

