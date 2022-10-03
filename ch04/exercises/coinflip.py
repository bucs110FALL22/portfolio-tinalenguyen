import turtle
import random

window = turtle.Screen()
window.bgcolor('white')

turt = turtle.Turtle()
turt.color('purple')

while turt.xcor() < 150 and turt.ycor() < 200 and turt.xcor() > -150 and turt.ycor() > -200:
  rand = random.randint(0, 1)
  if rand==1:
    turt.left(90)
  else:
    turt.right(90)
  turt.forward(50)
  window.delay(5)
  
turtle.done()
