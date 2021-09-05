from turtle import *
import turtle
from PIL import Image

# 绘制螺旋线
# myTurtle = Turtle()
# myWin = myTurtle.getscreen()

def drawSprial(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSprial(myTurtle, lineLen-5)

# drawSprial(myTurtle,100)
#
# ts = turtle.getscreen()
# ts.getcanvas().postscript(file="../results/sprial.eps")
# im = Image.open("../results/sprial.eps")
# im.save("results/sprial.jpg")