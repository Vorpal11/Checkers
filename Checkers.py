import tkinter

is_clicking = False
piece = -5

def click(event):
    x, y = event.x, event.y
    global is_clicking
    global piece
    is_clicking = not is_clicking
    if is_clicking:
        for i in range(len(coords)):
            x_great = x > (coords[i][0] - 40)
            x_less  = x < (coords[i][0] + 40)
            y_great = y > (coords[i][1] - 40)
            y_less  = y < (coords[i][1] + 40)
            if x_great and x_less and y_great and y_less:
                piece = i
                break
            else:
                piece = -5

def motion(event):
    x, y = event.x, event.y
    if is_clicking:
        if piece >= 0:
            canvas.coords(ids[piece], x, y)
            coords[piece] = [x, y]

root = tkinter.Tk()
root.wm_title("Checkers")
canvas = tkinter.Canvas(root, width=850, height=639, background='gray')
canvas.grid(row=0, rowspan=2, column=1)
canvas.bind('<Motion>', motion)
canvas.bind("<Button-1>", click)
canvas.bind("<ButtonRelease-1>", click)
# add for release
black_piece_image = tkinter.PhotoImage(file="Black_Piece.png")
red_piece_image = tkinter.PhotoImage(file="Red_Piece.png")

n = 0

coords = []
ids = []

for i in range(0, 640, 80):
    for j in range(0, 640, 80):
        if n % 2 == 0:
            canvas.create_rectangle(j, i, j + 80, i + 80, fill='#ffffff')
            if n < 26:
                coords.append([j + 40, i + 40])
                ids.append(canvas.create_image(j + 40, i + 40, image=black_piece_image))
            elif n > 42:
                coords.append([j + 40, i + 40])
                ids.append(canvas.create_image(j + 40, i + 40, image=red_piece_image))
        else:
            canvas.create_rectangle(j, i, j + 80, i + 80, fill='#000000')
        n += 1
    n += 1

for id in ids:
    canvas.tag_raise(id)

root.mainloop()