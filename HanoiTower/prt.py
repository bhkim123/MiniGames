from tkinter import *

window = Tk()
window.title("Tower of Hanoi")
window.geometry("830x320")

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


img1 = PhotoImage(file='1.png')
disc1 = bg_canvas.create_image(205, 210, image=img1)
img2 = PhotoImage(file='2.png')
disc2 = bg_canvas.create_image(205, 235, image=img2)
img3 = PhotoImage(file='3.png')
disc3 = bg_canvas.create_image(205, 260, image=img3)
img4 = PhotoImage(file='4.png')
disc4 = bg_canvas.create_image(205, 285, image=img4)

def move_disc1(e):
    global img1
    img1 = PhotoImage(file='1.png')
    disc1 = bg_canvas.create_image(e.x, e.y, image=img1)

def move_disc2(e):
    global img2
    img2 = PhotoImage(file='2.png')
    disc2 = bg_canvas.create_image(e.x, e.y, image=img2)

def move_disc3(e):
    global img3
    img3 = PhotoImage(file='3.png')
    disc3 = bg_canvas.create_image(e.x, e.y, image=img3)

def move_disc4(e):
    global img4
    img4 = PhotoImage(file='4.png')
    disc4 = bg_canvas.create_image(e.x, e.y, image=img4)

def detect_move(e):
    pass

bg_canvas.bind('<B1-Motion>', detect_move)

isStarted = False
def start_click(b):
    global isStarted
    if not isStarted:
        b.config(text="reset")
        isStarted = True


window.mainloop()

