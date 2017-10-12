from tkinter import *

def keylistener(event):
    print(event)

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.create_oval(50, 50, 60, 60, fill="red")
canvas.pack()
root.bind("w", keylistener)
root.bind("s", keylistener)
root.bind("o", keylistener)
root.bind("l", keylistener)

def animate():
    # TODO: make useful code
    root.after(20, animate)

animate()
root.mainloop()
