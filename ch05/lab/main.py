import pygame

''' PART A '''

n = 101
count = 0
#print("Start: 101")
while n!=1:
  if n%2==0:
    n/=2
  else:
    n=(3*n)+1
  count+=1
 # print(n)
  
#print("Count:", count)

''' PART B '''

upper_limit = 20
iters = {}

start = 2
for i in range(start, upper_limit):
  numIters = 0
  while i!=1:
    if i%2==0:
      i/=2
    else:
      i=(3*i)+1
    numIters+=1
  iters[start] = numIters
  start+=1


print(iters)
    
''' PART C '''


pygame.init()
display = pygame.display.set_mode()

font = pygame.font.Font(None, 50)

upper_limit = 20
iters = {}
max_so_far =0
max_val = 0
scale = 15

for i in range(2, upper_limit):
  count = 0
  n = i
  while n!=1:
    if n%2==0:
      n/=2
    else:
      n=(3*n)+1
    count+=1
  iters[i*scale] = count*scale
pygame.display.flip()
if len(iters) >= 2:
  pygame.draw.lines(display, "purple", False, list(iters.items()))
pygame.display.flip()
new_display = pygame.transform.flip(display, False, True)
display.blit(new_display , (0, 0))
pygame.display.flip()

if max_so_far < count:
  max_so_far = count
  max_val = count

rendered_message = font.render(str(max_so_far), False, "purple")
display.blit(rendered_message, (10, 10))

pygame.display.flip()