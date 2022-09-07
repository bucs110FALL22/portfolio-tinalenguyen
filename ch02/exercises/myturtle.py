import turtle

canvas = turtle.Screen()
turtleOne = turtle.Turtle()

turtleOne.shape("turtle")
turtleOne.color("purple")

for i in range(5):
  turtleOne.forward(50)
  turtleOne.right(90)


turtleOne.color("red")
turtleOne.up()
turtleOne.left(180)
turtleOne.forward(30)
turtleOne.pendown()

for i in range(5):
  turtleOne.forward(50)
  turtleOne.right(90)

canvas.exitonclick()
