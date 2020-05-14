import turtle

window= turtle.Screen()
window.bgcolor("lightyellow")
new_trutle= turtle.Turtle()

turtle.speed(100)
b=80
for i in range(75):
  new_trutle.circle(b)
  new_trutle.left(5)