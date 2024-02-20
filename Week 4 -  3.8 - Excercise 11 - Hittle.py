#import turtle and set up screen
import turtle             
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Wazzap dude")

#creation of turtle waluigi
waluigi = turtle.Turtle()
waluigi.color("purple")
waluigi.pensize(2)
waluigi.hideturtle()

#waluigi instructions
waluigi.left(36)
for i in range(5):
    waluigi.left(144)
    waluigi.forward(300)

wn.mainloop()
 
