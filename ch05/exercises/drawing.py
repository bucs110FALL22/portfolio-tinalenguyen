import turtle
import math

window = turtle.Screen()

def drawEqShape(turtleObj, num_sides, side_length):
  for i in range(num_sides):
    theta = 180 - (((num_sides-2)*180)/num_sides)
    turtleObj.forward(side_length)
    turtleObj.right(theta)
    window.delay(100)
    



newTurt = turtle.Turtle()
newTurt.shape('turtle')
newTurt.color('green')
newTurt.pendown()
num_sides = int(input("How many sides?"))
side_length  = int(input("What is the side length?"))
drawEqShape(newTurt, num_sides, side_length)