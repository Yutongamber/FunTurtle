from turtle import *
import turtle
from PIL import Image

def drawTriangle(points, color, myturtle):
    myturtle.fillcolor(color)
    myturtle.up()
    myturtle.goto(points[0])
    myturtle.down()
    myturtle.begin_fill()
    myturtle.goto(points[1])
    myturtle.goto(points[2])
    myturtle.goto(points[0])
    myturtle.end_fill()

def getMid(p1, p2):
    return ( (p1[0] + p2[0])/2 , (p1[1] + p2[1])/2 )

def sierpinski(points, degree, myTurtle):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]

    drawTriangle(points, colormap[degree], myTurtle)

    if degree > 0:
        sierpinski([points[0],
                   getMid(points[0], points[1]),
                   getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                   getMid(points[1], points[0]),
                   getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                   getMid(points[2], points[0]),
                   getMid(points[2], points[1])],
                   degree-1, myTurtle)

myturtle = Turtle()
myWin = myturtle.getscreen()
mypoints = [(-300, -150), (0, 300), (300, -150)]
sierpinski(mypoints, 5, myturtle)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="results/triangle.eps")
im = Image.open("results/triangle.eps")
im.save("results/triangle.jpg")