from examples.draw_sprial import drawSprial
from turtle import *
import turtle
from PIL import Image

# 绘制螺旋线
myTurtle = Turtle()
myWin = myTurtle.getscreen()

myTurtle.left(90)
myTurtle.up()
myTurtle.forward(150)
myTurtle.left(90)
myTurtle.forward(150)
myTurtle.right(180)
myTurtle.down()
drawSprial(myTurtle,300)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="results/sprial.eps")
im = Image.open("results/sprial.eps")
im.save("results/sprial.jpg")