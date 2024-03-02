import pygame, controls
from gun import Gun


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Жалкое подобие')
icon = pygame.image.load('Image/8386051.png')
pygame.display.set_icon(icon)
bg_color = (0, 0, 0)
gun = Gun(screen)

ranning = True
while ranning:
    controls.events()
    pygame.display.update(gun)

    screen.fill(bg_color)
    gun.output_to_screen()
    pygame.display.flip()   # hugtvuhb




