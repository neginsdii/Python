from turtle import *

speed(0)
up()
goto(-200,0)
down()
radius=30
colors=["red","magenta","blue", "cyan","green","yellow","white"]

def draw_star(radius):
  for i in range(7):
    left(90)
    forward(radius)
    left(-150)
    forward(radius)


indexcolor=0
for index in range(15,100,4):
  draw_star(index)
  color(colors[indexcolor])
  indexcolor+=1
  if indexcolor>6:
    indexcolor=0
