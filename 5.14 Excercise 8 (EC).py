

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(10)
    
def color(t,height): #new conditionals for bar color
    if height >= 200:
        t.color("red")
    elif height < 200 and height >= 100:
        t.color("yellow")
    else:
        t.color("green")
    draw_bar(t,height) #original function is now run here
        
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightblue")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for i in xs: 
    color(tess,i) #changed to use new function

wn.mainloop()
