import pygame, controls
from gun import Gun
from pygame.sprite import Group


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Жалкое подобие')
icon = pygame.image.load('Image/8386051.png')
pygame.display.set_icon(icon)
bg_color = (0, 0, 0)
gun = Gun(screen)
bullets = Group()

ranning = True
while ranning:
    controls.events(screen, gun, bullets)
    gun.update_gun()
    bullets.update()
    pygame.display.update()
    controls.screen_update(bg_color, screen, gun, bullets)
