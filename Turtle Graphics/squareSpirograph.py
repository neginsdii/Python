from turtle import *
bgcolor("black")
speed(0)
up()
goto(-200,0)
down()
colors=["red","magenta","blue", "cyan","green","yellow","white"]
for i in range(5):
  for colour in colors:
    color(colour)
    pensize(3)
    left(11)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)