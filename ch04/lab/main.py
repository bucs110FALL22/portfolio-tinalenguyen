import pygame

pygame.init()
screen = pygame.display.set_mode()
surface = pygame.display.get_surface()

screenDims = pygame.display.get_window_size()
width = screenDims[0]
height = screenDims[1]
center = [width/2, height/2]
print(width)
print(center)
pygame.draw.circle(surface, (255, 255, 0), center, height/2)
pygame.display.flip()
pygame.time.wait(3000)
