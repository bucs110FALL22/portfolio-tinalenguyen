import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((300, 300))
screen.fill('blue')
surface = pygame.display.get_surface()

screenDims = pygame.display.get_window_size()
width = screenDims[0]
height = screenDims[1]

pygame.draw.circle(surface, 'pink', (150, 150), 150)
pygame.draw.line(surface, 'black', (0, 150), (300, 150))
pygame.draw.line(surface, 'black', (150, 0), (150, 300))
pygame.display.flip()

''' THROWING TEN RANDOM DARTS '''

for i in range(10):
  randX = random.randint(0, width)
  randY = random.randint(0, height)

  distance_from_center = math.hypot(randX-(width/2), randY-(height/2)) #the distance formula
  is_in_circle = distance_from_center <= width/2 #screen width
  #print(is_in_circle)
  if is_in_circle:
    pygame.draw.circle(surface, 'green', (randX, randY), 5)
    pygame.display.flip()
  else:
    pygame.draw.circle(surface, 'red', (randX, randY), 5)
  pygame.display.flip()
  pygame.time.wait(1000)

''' USER GAMBLES ON TWO PLAYERS '''

screen.fill('blue')
pygame.draw.circle(surface, 'pink', (150, 150), 150)
pygame.draw.line(surface, 'black', (0, 150), (300, 150))
pygame.draw.line(surface, 'black', (150, 0), (150, 300))


pygame.draw.rect(surface, 'purple', pygame.Rect(30, 30, 60, 60))
pygame.draw.rect(surface, 'orange', pygame.Rect(200, 30, 60, 60))
pygame.display.flip()

print("Click on a colored square!")

clicked = False
chosen = ""
while not clicked:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      coords = pygame.mouse.get_pos()
      #print(coords)
      if coords[0] < 90 and coords[0] > 30 and coords[0] < 90 and coords[0] > 30:
        chosen = "purple"
       # print(chosen)
        clicked = True
      if coords[0] < 260 and coords[0] > 200 and coords[1] < 90 and coords[1] > 30:
        chosen = "orange"        
       # print(chosen)
        clicked = True
      
''' SIMULATED GAME OF TEN ROUNDS '''

screen.fill('blue')
pygame.draw.circle(surface, 'pink', (150, 150), 150)
pygame.draw.line(surface, 'black', (0, 150), (300, 150))
pygame.draw.line(surface, 'black', (150, 0), (150, 300))
pygame.display.flip()

orangePoints = 0
purplePoints = 0
turn = "purple"
for i in range(20):
  randX = random.randint(0, width)
  randY = random.randint(0, height)
  distance_from_center = math.hypot(randX-(width/2), randY-(height/2)) 
  is_in_circle = distance_from_center <= width/2 

  if is_in_circle:
    if turn == "purple":
      pygame.draw.circle(surface, 'purple', (randX, randY), 5)
      pygame.display.flip()
      purplePoints+=1
      turn = "orange"
    else: 
      pygame.draw.circle(surface, 'orange', (randX, randY), 5)
      pygame.display.flip()
      orangePoints+=1
      turn = "purple"
  else:
    pygame.draw.circle(surface, 'red', (randX, randY), 5)
    pygame.display.flip()
    if turn == "purple":
      turn = "orange"
    else: 
      turn = "purple"
  pygame.time.wait(1000)
  
if orangePoints > purplePoints:
  winner = "orange"
  result = "Orange won!"

elif orangePoints == purplePoints:
  result = "They tied!"

else:
  winner = "purple"
  result = "Purple won!"

print(result)

if result == chosen:
  print("You were right!")
elif result == "They tied!":
  print("You were half right!")
else:
  print("You were wrong!")

print("Orange's points: ", orangePoints)
print("Purple's points: ", purplePoints)
pygame.time.wait(3000)
