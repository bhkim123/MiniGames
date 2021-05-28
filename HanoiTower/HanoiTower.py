from tkinter import *

window = Tk()
window.title("Tower of Hanoi")
window.geometry("830x320")
window.resizable(False, False)

w = 900
h = 400

bg_canvas = Canvas(window, width=w, height=h, bg='white')
bg_canvas.pack()

start_bt = Button(window, text="Game Start", command=lambda: start_click(start_bt))
start_bt.place(relx=0.05, rely=0.05)
start_bt.place(relwidth=0.2, relheight=0.1)

column1 = bg_canvas.create_rectangle(200, 150, 210, 300, fill='tan')
column2 = bg_canvas.create_rectangle(410, 150, 420, 300, fill='tan')
column3 = bg_canvas.create_rectangle(620, 150, 630, 300, fill='tan')
floor = bg_canvas.create_rectangle(0, 300, 900, 320, fill='tan')

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
disc1 = bg_canvas.create_image(x_1st, 210, image=img1, tags=1)
img2 = PhotoImage(file='2.png')
disc2 = bg_canvas.create_image(x_1st, 235, image=img2, tags=2)
img3 = PhotoImage(file='3.png')
disc3 = bg_canvas.create_image(x_1st, 260, image=img3, tags=3)
img4 = PhotoImage(file='4.png')
disc4 = bg_canvas.create_image(x_1st, 285, image=img4, tags=4)

b12 = Button(window, text="To 2nd", font=("Helvetica", 10), command=lambda: clicked(b12)).place(x=150, y=300, width=50, height=20)
b13 = Button(window, text="To 3rd", font=("Helvetica", 10), command=lambda: clicked(b13)).place(x=210, y=300, width=50, height=20)

b21 = Button(window, text="To 1st", font=("Helvetica", 10), command=lambda: clicked(b21)).place(x=360, y=300, width=50, height=20)
b23 = Button(window, text="To 3rd", font=("Helvetica", 10), command=lambda: clicked(b23)).place(x=420, y=300, width=50, height=20)

b31 = Button(window, text="To 1st", font=("Helvetica", 10), command=lambda: clicked(b31)).place(x=570, y=300, width=50, height=20)
b32 = Button(window, text="To 2nd", font=("Helvetica", 10), command=lambda: clicked(b32)).place(x=630, y=300, width=50, height=20)

list_1st = [disc4, disc3, disc2, disc1]
list_2nd = []
list_3rd = []


def clicked(b):

    if (b == b12 or b == b13) and len(list_1st) > 0:
        top_d = list_1st[-1]
        if b == b12 and len(list_2nd) > 0 and (list_2nd[-1])["tag"] > top_d["tag"]:
            count += 1
            ct.config(text="count: " + str(count))
            list_2nd.append(top_d)
            list_1st.remove(top_d)
            move_disc()
        elif b == b13 and len(list_3rd) > 0 and (list_3rd[-1])["tag"] > top_d["tag"]:
            count += 1
            ct.config(text="count: " + str(count))
            list_3rd.append(top_d)
            list_1st.remove(top_d)
            move_disc()
    elif b == b21 or b == b23:
        pass
    else:
        pass

def move_disc():
    pass

isStarted = False

def start_click(b):
    global isStarted, list_1st, list_2nd, list_3rd, disc1, disc2, disc3, disc4
    if not isStarted:
        b.config(text="reset")
        isStarted = True
    else:
        reset()

def reset():
    global count, list_1st, list_2nd, list_3rd, disc1, disc2, disc3, disc4
    count = 0
    list_1st = [disc1, disc2, disc3, disc4]
    list_2nd = []
    list_3rd = []




window.mainloop()

