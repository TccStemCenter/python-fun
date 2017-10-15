#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

ball = None
root = None

def main():
    global ball, root

    # create window
    root = Tk()

    # create canvas (for drawing) and place into root
    canvas = Canvas(root, width=400, height=400)

    # create ball
    ball = Ball(canvas, 8, 3, 1, 200, 200, "blue")

    # bind to keys
    for key in ("w", "s", "o", "l", "q"):
        root.bind(key, keylistener)

    # update root elements
    canvas.pack()
    animate()
    root.mainloop()


def keylistener(event):
    '''handles all key input

    :event: event passed by Tk mainloop
    '''
    if event.char == 'q':
        # exit out of application
        root.destroy()
        return
    if event.char == 'w':
        pass
    if event.char == 's':
        pass
    if event.char == 'o':
        pass
    if event.char == 'l':
        pass

def animate():
    '''animation loop (async)
    '''
    ball.updatePosition()
    root.after(20, animate)


class Ball():
    '''Ball for pong'''

    def __init__(self, canvas, radius, vx, vy, x = 0, y = 0, color="red"):
        '''initialize ball for a canvas with radius with velocity in
            x- and y-direction and, optionally, at (x,y) position

        :canvas: canvas to which to draw the ball
        :radius: radius of the ball
        :vx: velocity in x-direction
        :vy: velocity in y-direction
        :x: initial x-position (0 if not specified)
        :y: initial y-position (0 if not specified)

        '''
        self._radius = radius
        self._canvas = canvas
        self._vx = vx
        self._vy = vy
        self._oval = self._canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="")

    def updatePosition(self):
        coords = self._canvas.coords(self._oval)
        if self._vx > 0:
            if coords[2] + self._vx > self._canvas.winfo_reqwidth():
                self._vx *= -1
        else:
            if coords[0] + self._vx < 0:
                self._vx *= -1
        if self._vy > 0:
            if coords[3] + self._vy > self._canvas.winfo_reqheight():
                self._vy *= -1
        else:
            if coords[1] + self._vy < 0:
                self._vy *= -1
        self._canvas.move(self._oval, self._vx, self._vy)


class Paddle():

    '''Paddle for pong'''

    def __init__(self, canvas, xCenter, width, height, yInc, yCenter = None, color = "black"):
        '''init Paddle

        :xCenter: where the center paddle will lie in x-direction
        :width: width of paddle
        :height: height of paddle
        :yInc: how much to increment paddle when moved
        :yCenter: where to position center of paddle in y-direction (optional)
        :color: color of paddle (optional)
        '''
        self._canvas = canvas
        self._width = width
        self._height = height
        self._yInc = yInc
        self._color = color


if __name__ == '__main__':
    main()
