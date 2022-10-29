import turtle
import math

def main():
  window = turtle.Screen()
  window.setup(500, 500)
  
  fredTurtle = turtle.Turtle()
  fredTurtle.speed(8)
  drawAfro(fredTurtle, 2, 0, 25)
  faceCoords = drawHead(fredTurtle, 2, 0, 25)
  drawEye(fredTurtle, faceCoords[0]+40, 100)
  drawEye(fredTurtle, faceCoords[1]-40, 100)
  drawMouth(fredTurtle, faceCoords[0]+50, faceCoords[1]-50, 10, 60)
  window.exitonclick()

def drawAfro(turtle, scale, x, y):
    ''' 
  This function draws Bob Ross's afro.

  args: turtle-(Turtle) object to draw with
  scale-(int) scale factor compared to original size
  x-(int) x coordinate of crown of the head
  y-(int) y coordinate of crown of the head
  return: None
  
  '''
    turtle.color("#873e23")
    turtle.penup()
    turtle.goto(x, y+15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50*scale)
    turtle.end_fill()
  
  
def drawHead(turtle, scale, x, y):
  ''' 
  This function draws the base of a face/head. This simply     includes the face shape and the ears. 

  args: turtle-(Turtle) object to draw with
  scale-(int) scale factor compared to original size
  x-(int) x coordinate of crown of the head
  y-(int) y coordinate of crown of the head
  return: (List) widthRestraints: x coordinate of the left end of the head, x coordinate of right end of the head
  
  '''

#drawing head
  turtle.color("#ffdd99", "#ffdd99")
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(40*scale)
  turtle.end_fill()
  
#drawing ears
  turtle.penup()
  turtle.goto(-40*scale+5, 15+(40*scale))
  turtle.pd()
  turtle.begin_fill()
  turtle.circle(15)
  turtle.goto(40*scale-5, 15+(40*scale))
  turtle.circle(15)
  turtle.end_fill()

  widthRestraints = [x-(40*scale), x+(40*scale)]
  return widthRestraints

def drawEye(turtle, x, y):
  ''' 
  This function draws an eye at the specified coordinates.

  args: turtle-(Turtle) object to draw with
  x-(int) x coordinate of the top of the eye
  y-(int) y coordinate of the top of the eye
  return: None
  '''

  turtle.pu()
  turtle.goto(x, y)
  turtle.color("white")
  turtle.begin_fill()
  turtle.circle(15)
  turtle.end_fill()
  turtle.goto(x, y+8)
  turtle.color("black")
  turtle.begin_fill()
  turtle.circle(7)
  turtle.end_fill()

def drawMouth(turtle, leftRes, rightRes, bottomycor, length):
    ''' 
  This function draws an mouth within the specified restraints.

  args: turtle-(Turtle) object to draw with
  leftRes-(int) x coordinate of the left restraint of the mouth
  rightRes-(int) y coordinate of the right restraint of the mouth
  bottomycor-(int) y coordinate of the bottom of the mouth
  length-(int) how long the mouth is
  return: None
  '''
    midpoint = (rightRes - leftRes)/2
    turtle.pu()
    turtle.goto(leftRes, bottomycor+length)
    turtle.color("black")
    turtle.pd()
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(midpoint*2)
    turtle.goto(leftRes, bottomycor+length)
    turtle.setheading(270)
    turtle.circle(midpoint, 180)
    turtle.end_fill()
    
main()

