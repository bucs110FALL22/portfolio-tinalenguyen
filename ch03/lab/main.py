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

''' Race 1: Single call for  each turtle using independent random values between 1 and 100 ''' 

randNum1 = random.randrange(1, 100)
randNum2 = random.randrange(1, 100)

michelangelo.forward(randNum1) 
leonardo.forward(randNum2)

#reset 
michelangelo.goto(-100, 20)
leonardo.goto(-100,-20)

''' Race 2: Advancing each turtle 10 times by independent random values '''
for i in range(11): 
  randNum1 = random.randrange(0, 10)
  randNum2 = random.randrange(0, 10)

  michelangelo.forward(randNum1) 
  leonardo.forward(randNum2)

#reset
michelangelo.goto(-100, 20)
leonardo.goto(-100,-20)

window.exitonclick()

# PART B - complete part B here

pygame.init()
screen = pygame.display.set_mode()
surface = pygame.display.get_surface()

''' Equilateral Triangle '''

coords = []
num_sides = 3
side_length = 20
offset = 20
x = 0
y = 0

rectt = pygame.Rect((0, 0), (50,50))
pygame.draw.rect(screen, "white", rectt)
# for i in range(4):
  
#   theta = (2.0 * math.pi * num_sides) / num_sides
#   print(theta)
#   x += side_length * math.cos(theta) + offset
#   y += side_length * math.sin(theta) + offset
#   coords.append((x, y))

# print("coords: ", coords)
# pygame.draw.polygon(screen, "purple", coords)
pygame.time.wait

 
