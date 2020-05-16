from turtle import *

bgcolor("black")
up()
goto(-200,0)
down()
colors=["red","magenta","blue", "cyan","green","yellow","white"]
for i in range(3):
  for colour in colors:
    color(colour)
    pensize(3)
    circle(150)
    forward(20)
