import turtle

numSides = int(input("How many sides are there?"))
length = int(input("What's the length of each side?"))

canvas = turtle.Screen()
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("purple")

rotateAngle = 180-(((numSides-2)*180)/numSides)

for i in range(numSides):
  turtle1.forward(length)
  turtle1.right(rotateAngle)

canvas.exitonclick()
  


