import turtle 

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
 
wn = turtle.Screen()
wn.bgcolor("lightgreen")
 
alex = turtle.Turtle()
alex.color("hotpink")
 
sideLen = 20
for i in range(6):
    drawSquare(alex,sideLen)
    alex.penup()
    alex.backward(10)
    alex.left(90)
    alex.forward(10)
    alex.pendown()
    sideLen = sideLen + 20
 
wn.exitonclick()