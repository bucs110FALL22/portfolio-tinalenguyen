import turtle #1. import modules
import random
import pygame
import math


#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
randNum1 = random.randrange(1, 100)
randNum2 = random.randrange(1, 100)

michelangelo.forward(randNum1) 
leonardo.forward(randNum2)

michelangelo.goto(-100, 20)
leonardo.goto(-100,-20)

for i in range(11):
  randNum1 = random.randrange(0, 10)
  randNum2 = random.randrange(0, 10)

  michelangelo.forward(randNum1) 
  leonardo.forward(randNum2)

michelangelo.goto(-100, 20)
leonardo.goto(-100,-20)


# PART B - complete part B here

pygame.init()
window = pygame.display.set_mode()

# equilateral triangle
# for i in range(4):
#   theta = (2.0 * math.pi * s)

window.exitonclick()

