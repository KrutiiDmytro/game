import pygame, sys

def events(gun):
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ranning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                gun.rect.centr += 1