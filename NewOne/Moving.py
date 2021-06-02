from tkinter import *

root = Tk()
root.title('Game')
root.geometry("900x400")
root.resizable(False, False)

w = 900
h = 400
x = w//2
y = h//2

my_canvas = Canvas(root, width=w, height=h, bg='black')
my_canvas.pack()

current_x = w//3
current_y = y//2

my_character = ct = Label(root, width=1, height=1, text="", borderwidth=1, relief='groove', bg='white')
my_character.place(x=current_x, y=current_y)

def left(event):
    global current_x, current_y
    current_x -= 5
    my_character.place(x=current_x, y=current_y)

def right(event):
    global current_x, current_y
    current_x += 5
    my_character.place(x=current_x, y=current_y)

def up(event):
    global current_y, current_y
    current_y -= 5
    my_character.place(x=current_x, y=current_y)

def down(event):
    global current_y, current_y
    current_y += 5
    my_character.place(x=current_x, y=current_y)


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()