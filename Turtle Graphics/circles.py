import turtle
ob=turtle.Turtle()
ob.speed(10)
pen_color=["lightpurple","purple","pink"]


def drawArt(dis,angle,x,y):
  d=dis
  c=0
  ob.up()
  ob.goto(x,y)
  ob.down()
  for i in range(1,400):
    ob.pencolor(pen_color[c])
    ob.circle(d)
    ob.left(angle)
    d-=1
    if d<10:
      d=dis
    c+=1
    if(c>len(pen_color)-1):
      c=0


drawArt(50,100,0,0)

