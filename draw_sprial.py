from turtle import *
import turtle
from PIL import Image

# 绘制螺旋线
def drawSprial(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSprial(myTurtle, lineLen-5)


myTurtle = Turtle()
myWin = myTurtle.getscreen()

myTurtle.left(90)
myTurtle.up()
myTurtle.forward(200)
myTurtle.left(90)
myTurtle.forward(200)
myTurtle.right(180)
myTurtle.down()

drawSprial(myTurtle,400)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="results/sprial.eps")
im = Image.open("results/sprial.eps")
im.save("results/sprial.jpg")