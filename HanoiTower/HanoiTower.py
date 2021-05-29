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

b12 = Button(window, text="To 2nd", font=("Helvetica", 10), command=lambda: clicked(b12))
b12.place(x=150, y=300, width=50, height=20)
b13 = Button(window, text="To 3rd", font=("Helvetica", 10), command=lambda: clicked(b13))
b13.place(x=210, y=300, width=50, height=20)
b21 = Button(window, text="To 1st", font=("Helvetica", 10), command=lambda: clicked(b21))
b21.place(x=360, y=300, width=50, height=20)
b23 = Button(window, text="To 3rd", font=("Helvetica", 10), command=lambda: clicked(b23))
b23.place(x=420, y=300, width=50, height=20)
b31 = Button(window, text="To 1st", font=("Helvetica", 10), command=lambda: clicked(b31))
b31.place(x=570, y=300, width=50, height=20)
b32 = Button(window, text="To 2nd", font=("Helvetica", 10), command=lambda: clicked(b32))
b32.place(x=630, y=300, width=50, height=20)

list_1st = [disc4, disc3, disc2, disc1]
list_2nd = []
list_3rd = []


isStarted = False


def start_click(b):
    global isStarted, list_1st, list_2nd, list_3rd, disc1, disc2, disc3, disc4
    if not isStarted:
        b.config(text="reset")
        isStarted = True
    else:
        reset()


def clicked(b):
    global count, b12, b13, b21, b23, b31, b32, list_1st, list_2nd, list_3rd, isStarted
    if isStarted:
        if (b == b12 or b == b13) and len(list_1st) > 0:
            top_d = list_1st[-1]
            if b == b12 and ((len(list_2nd) > 0 and compare_disc(top_d, list_2nd[-1])) or len(list_2nd) == 0):
                count += 1
                ct.config(text="count: " + str(count))
                list_2nd.append(top_d)
                list_1st.remove(top_d)
                move_disc()
            elif b == b13 and ((len(list_3rd) > 0 and compare_disc(top_d, list_3rd[-1])) or len(list_3rd) == 0):
                count += 1
                ct.config(text="count: " + str(count))
                list_3rd.append(top_d)
                list_1st.remove(top_d)
                move_disc()
        elif b == b21 or b == b23 and len(list_2nd) > 0:
            top_d = list_2nd[-1]
            if b == b21 and ((len(list_1st) > 0 and compare_disc(top_d, list_1st[-1])) or len(list_1st) == 0):
                count += 1
                ct.config(text="count: " + str(count))
                list_1st.append(top_d)
                list_2nd.remove(top_d)
                move_disc()
            elif b == b23 and ((len(list_3rd) > 0 and compare_disc(top_d, list_3rd[-1])) or len(list_3rd) == 0):
                count += 1
                ct.config(text="count: " + str(count))
                list_3rd.append(top_d)
                list_2nd.remove(top_d)
                move_disc()
        elif b == b31 or b == b32 and len(list_3rd) > 0:
            top_d = list_3rd[-1]
            if b == b31 and ((len(list_1st) > 0 and compare_disc(top_d, list_1st[-1])) or len(list_1st) == 0):
                count += 1
                ct.config(text="count: " + str(count))
                list_1st.append(top_d)
                list_3rd.remove(top_d)
                move_disc()
            elif b == b32 and ((len(list_2nd) > 0 and compare_disc(top_d, list_2nd[-1])) or len(list_2nd) == 0):
                count += 1
                ct.config(text="count: " + str(count))
                list_2nd.append(top_d)
                list_3rd.remove(top_d)
                move_disc()
        check_win()


def move_disc():
    global list_1st, list_2nd, list_3rd, x_1st, x_2nd, x_3rd, y_top, y_2nd, y_3rd, y_bottom, img1, img2, img3, img4, disc1, disc2, disc3, disc4
    li = [list_1st, list_2nd, list_3rd]
    for l in li:
        x = 0
        if l == list_1st:
            x = x_1st
        elif l == list_2nd:
            x = x_2nd
        else:
            x = x_3rd

        for i in range(0, len(l)-1):
            y = 0
            if i == 0:
                y = y_bottom
            elif i == 1:
                y = y_3rd
            elif i == 2:
                y = y_2nd
            elif i == 3:
                y = y_top
            move_image(x, y, l[i])


def move_image(x, y, d):
    global disc1, disc2, disc3, disc4, img1, img2, img3, img4, bg_canvas
    if d == disc1:
        bg_canvas.delete("d1")
        disc1 = bg_canvas.create_image(x, y, image=img1, tag="d1")
    elif d == disc2:
        bg_canvas.delete("d2")
        disc2 = bg_canvas.create_image(x, y, image=img2, tag="d2")
    elif d == disc3:
        bg_canvas.delete("d3")
        disc3 = bg_canvas.create_image(x, y, image=img3, tag="d3")
    elif d == disc4:
        bg_canvas.delete("d4")
        disc4 = bg_canvas.create_image(x, y, image=img4, tag="d4")


def compare_disc(top, bottom):
    global disc1, disc2, disc3, disc4
    if top == disc1:
        return True
    elif top == disc2 and (bottom == disc3 or bottom == disc4):
        return True
    elif top == disc3 and bottom == disc4:
        return True
    else:
        return False


def check_win():
    global list_3rd, disc1, disc2, disc3, disc4
    if list_3rd == [disc4, disc3, disc2, disc1]:
        messagebox.showinfo("Tower of Hanoi", message='Well done!')
        make_disabled()


def make_disabled():
    global b12, b13, b21, b23, b31, b32
    li = [b12, b13, b21, b23, b31, b32]
    for l in li:
        l.config(state=tk.DISABLED)


def reset():
    global count, list_1st, list_2nd, list_3rd, disc1, disc2, disc3, disc4
    count = 0
    ct.config(text="count: " + str(count))
    list_1st = [disc1, disc2, disc3, disc4]
    list_2nd = []
    list_3rd = []
    move_disc()
    make_abled()


def make_abled():
    global b12, b13, b21, b23, b31, b32
    buttons = [b12, b13, b21, b23, b31, b32]
    for b in buttons:
        b.config(state=tk.NORMAL)


bg_canvas.pack()
window.mainloop()

