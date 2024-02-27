

import turtle #turtle Import

#define function to use
def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

#turtle and screen creation
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Excercise 4.9-2")
bubb = turtle.Turtle()
bubb.color("hotpink")
bubb.pensize("3")

#loop to draw each sucessive square
size = 20
for i in range(5):
    draw_square(bubb, size)
    size = size + 20
    bubb.penup()
    bubb.goto(10 + (-size / 2),10 + (-size / 2))
    bubb.pendown()

wn.mainloop()
