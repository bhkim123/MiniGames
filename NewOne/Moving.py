from tkinter import *

root = Tk()
root.title('Game')
root.geometry("900x400")
root.resizable(False, False)

w = 900
h = 400

my_canvas = Canvas(root, width=w, height=h, bg='white')
my_canvas.pack()

current_x = w / 5
current_y = h / 2 - 10
#start point

my_character = ct = Label(root, width=2, height=1, text=" ", borderwidth=1, relief='groove', bg='black')
my_character.place(x=current_x, y=current_y)
#lefttop(1,1) rightbottom(880, 380)

def left(event):
    global current_x, current_y
    if 1 < current_x:
        current_x -= 10
        my_character.place(x=current_x, y=current_y)

def right(event):
    global current_x, current_y
    if 880 > current_x:
        current_x += 10
        my_character.place(x=current_x, y=current_y)

def up(event):
    global current_y, current_y
    if 1 < current_y:
        current_y -= 10
        my_character.place(x=current_x, y=current_y)

def down(event):
    global current_y, current_y
    if current_y < 380:
        current_y += 10
        my_character.place(x=current_x, y=current_y)


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()