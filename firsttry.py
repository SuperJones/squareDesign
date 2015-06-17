import turtle
 
def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
 
def drawFour(t, sz, scoot):
    for i in range(6):
        drawSquare(t, sz)
		#put penup in comments so that I could see the line being drawn and 
		#try to figure out what is going wrong.
        #t.penup()  
        t.backward(scoot)
        t.right(90)
        t.forward(scoot)
        t.left(90)
        #t.pendown()
        sz = sz + sz
        scoot = scoot + scoot
       
wn = turtle.Screen()
wn.bgcolor("lightgreen")
 
alex = turtle.Turtle()
alex.color("hotpink")
 
drawFour(alex, 20, 10)
 
wn.exitonclick()