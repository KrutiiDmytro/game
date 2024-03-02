import pygame, sys

def events(gun):
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ranning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # to right
            if event.key == pygame.K_d:
                gun.mright = True
            # to left
            elif event.key == pygame.K_a:
                gun.mleft = True
        elif event.type == pygame.KEYUP:
            # to right
            if event.key == pygame.K_d:
                gun.mright == False
            # to left
            elif event.key == pygame.K_a:
                gun.mleft == False

                gun.mright == False