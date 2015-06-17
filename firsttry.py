import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
def Instruct(t, sz, axis):
    drawSquare(t, sz)
    t.penup()
    t.goto(axis, axis)
    t.pendown()
    sz = sz + 20
    axis = axis -10
    
    
        
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("hotpink")


Insrtuct(alex, 20, -10.0)

wn.exitonclick()